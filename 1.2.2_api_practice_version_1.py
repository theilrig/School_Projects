import requests

APIurl = "https://cs-api.pltw.org/"
newUserSyntax = "newuser/"

def main():
    action_prompt()

def action_prompt():
    user_action = input("Would you like to make a new user or do you have an existing user: ").lower().strip()
    
    while user_action not in ("new user", "existing user"):
        print("Please input either new user or existing user")
        user_action = input("Would you like to make a new user or do you have an existing user: ").lower().strip()
    
    if user_action == "new user":
        new_user()
    else:
        existing_user()

    command_prompt()

def new_user():
    global user_name
    user_name = input("What do you want your new username to be? ")
    new_user_name_link = APIurl + user_name
    new_user_name_link_object = requests.post(APIurl + newUserSyntax + user_name)
    
    try:
        new_user_name_link_object.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
    
    print_new_link(new_user_name_link)


def print_new_link(new_link):
    print(new_link)



def existing_user():
   global user_name
   user_name = input("What is your user name: ")
   


def command_prompt():
    global user_name
    global user_name_link
    global accepted_commands
    user_name_link = APIurl+user_name
    print(f"Your link is: {user_name_link}")
    accepted_commands = ["help", "stop", "add text", "all info", "vote item","interview", "user wipe"]
    command = input("What would you like to do. List help for set of commands: ").strip().lower()
    while command not in (accepted_commands):
        print("Please use an accepted command")
        command = input("What would you like to do. List help for set of commands: ").strip().lower()
    
    while command not in ("stop"):
        if command == "help":
            for i in range(len(accepted_commands)):
                print(accepted_commands[i])
                i += 1
        if command == "add text":
            add_text()
        command_prompt()

def add_text():
    add_text_syntax = "?text="
    posted_text = str(input("What would you like to post: "))
    requests.post(user_name_link+add_text_syntax+posted_text)

if __name__ == "__main__":
    main()
