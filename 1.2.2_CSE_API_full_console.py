import requests
import json

APIurl = "https://cs-api.pltw.org/"
indexing_reminder = "The first string listed is indexed as string 1: "
boolean_list = ["yes", "y", "n" "no"]

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
    newUserSyntax = "newuser/"
    global user_name
    user_name = input("What do you want your new username to be? ")
    new_user_name_link_object = requests.post(APIurl + newUserSyntax + user_name)
    
    try:
        new_user_name_link_object.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")

def existing_user():
   global user_name
   user_name = input("What is your user name: ")

def command_prompt():
    global user_name
    global user_name_link
    user_name_link = APIurl+user_name
    print(f"Your link is: {user_name_link}")
    full_command_list = ["help", "stop", "add text", "all info", "vote item","documentation","interview", "user wipe"]
    command = input("What would you like to do. List help for set of commands: ").strip().lower()
    while command not in (full_command_list):
        print("Please use an accepted command")
        command = input("What would you like to do. List help for set of commands: ").strip().lower()
    while True:
        if command == "help":
            readable_command_print(full_command_list)
        elif command == "add text":
            add_text(input("What would you like to post: "))
        elif command == "all info":
            all_info()
        elif command == "vote item":
            vote_item(input(f"What string do you want to vote.{indexing_reminder}").lower().strip())
        elif command == "documentation":
            grab_documentation()
        elif command == "interview":
            interview()
        elif command == "user wipe":
            user_wipe_confirmation()
        elif command == "stop":
            finished()
            break
        command_prompt()

def add_text(posted_text):
    add_text_syntax = "?text="
    requests.post(user_name_link+add_text_syntax+posted_text)

def all_info():
    all_user_info = requests.get(user_name_link)
    try:
        all_user_info.raise_for_status()
        user_info_json = all_user_info.json()
        print(json.dumps(user_info_json, indent=2))
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON: {json_err}")

def vote_item(item_id):
    vote_item_syntax = "/increment?id="
    requests.post(user_name_link+vote_item_syntax+item_id)

def grab_documentation():
    print("This is the API documentation")
    print("https://instructional-resources.s3.amazonaws.com/PLTW_Computer_Science/30161_ComputerScienceEssentials/English_External_Files/CSE_API_Reference.pdf")

def interview():
    interview_command = input("What interview command would you like to use. Type in help for help: ").lower().strip()
    acceptable_interview_command = ["add question", "all questions", "answer question","help","stop"]
    while interview_command not in (acceptable_interview_command):
        print("Use an accepted command")
        interview()
    while True:
        if interview_command == "help":
            readable_command_print(acceptable_interview_command)
        elif interview_command == "add question":
            add_question()
        elif interview_command == "answer question":
            answer_question()
        elif interview_command == "all questions":
            all_info()
        elif interview_command == "stop":
            finished()
            break
        interview()

def add_question():
    add_text(input("What yes or no question would you like to add: "))
    interview()

def answer_question():
    question_id = input(f"What question do you want to answer, make sure to give its precise string id {indexing_reminder}")
    question_answer = input("Is your answer yes or no: ").lower().strip()
    while question_answer not in (boolean_list):
        question_answer = input("Is your answer yes or no: ").lower().strip()
    if question_answer == "yes" or "y":
        vote_item(question_id)
    else: 
        print("Your answer won't change the value but still counts")
    interview()


def readable_command_print(command_list):
    for i in range(len(command_list)):
        print(command_list[i])
        i += 1

def user_wipe_confirmation():
    confirmation = input("Are you sure: ").lower().strip()
    while confirmation not in (boolean_list):
        user_wipe_confirmation
    if confirmation == "yes" or "y":
        user_wipe()
    else: 
        command_prompt()

def user_wipe():
    user_wipe_syntax = "/reset?password="
    possible_passwords = range(999, 10000)

    for attempted_password in possible_passwords:
        attempt_object = requests.post(f"{user_name_link}{user_wipe_syntax}{attempted_password}")
    try:
        attempt_object.raise_for_status()
        all_info()
        print("The data has been wiped")
    except requests.exceptions.HTTPError as err:
        print(f"Error wiping data: {err}")

def finished():
    print("The program has stopped")

if __name__ == "__main__":
    main()