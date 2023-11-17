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
        value_action = ""

def new_user():
    new_user_name = input("What do you want your new username to be? ")
    new_user_name_link = APIurl + new_user_name
    new_user_name_link_object = requests.post(APIurl + newUserSyntax + new_user_name)
    
    try:
        new_user_name_link_object.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        # Handle the error as needed
    
    print_new_link(new_user_name_link)

def print_new_link(new_link):
    print(new_link)

if __name__ == "__main__":
    main()
