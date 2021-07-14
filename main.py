import datetime
import os
import quickstart

CALENDAR_ID = os.environ.get("CAL_ID")
service = quickstart.initialize()


# A function which writes numbers representing the amount of days ahead you should be studying
def generate_fibonacci_file(fib_number):
    fibonacci_list = [1, 1]
    modified_list = [1, 2]
    with open('fibonacci.txt', 'w') as file:
        for i in range(2):
            file.write(str(modified_list[i]) + "\n")
        for i in range(2, fib_number):
            fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])
            # As for this program, we care about the amount fo days to study in the future relative to the first day
            modified_list.append(fibonacci_list[-1] + modified_list[-1])
            file.write(str(modified_list[-1]) + "\n")


# The input to this function represents the date in the future we would like to calculate
def calculate_days_ahead(fib_number):
    next_date = (datetime.date.today() + datetime.timedelta(days=fib_number))
    return next_date


# If the user misclicked at any point the program will cease execution
def output_confirmation(summary):
    if summary == "":
        print("Understood, the program will cease execution!\n")
        exit(0)


# Query the user as to what they would like to study or delete
def ask_user_for_summary(task):
    print(f"\nWhat would you like to {task}?\n"
          "\nIf this was a misclick simply click the \"Enter\" key to exit the program\n")


# The Google Calendar is updated with the entries that the user requests using the Fibonacci Study Plan
def create_study_plan():
    if not os.path.exists("fibonacci.txt"):
        generate_fibonacci_file(9)

    ask_user_for_summary("study")
    user_summary = input()
    output_confirmation(user_summary)
    user_description = input("\nPlease enter a description or press the \"Enter\" key to skip this step\n")
    print("\nPlease wait a moment while your request is processed\n")

    with open('fibonacci.txt', 'r') as file:
        for line in file:
            days_ahead = int(line)
            actual_date = calculate_days_ahead(days_ahead)
            event = {
                'summary': "Study " + user_summary,
                'description': user_description,
                'start': {
                    'date': str(actual_date),
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'date': str(actual_date),
                    'timeZone': 'America/Los_Angeles',
                },
            }
            event = service.events().insert(calendarId=CALENDAR_ID,
                                            body=event).execute()


# All entries with the summary the user provides as input are deleted starting after the day this program is called
def delete_study_plan():
    min_value = datetime.datetime.now(datetime.timezone.utc)
    min_value = min_value.isoformat()
    page_token = None
    ask_user_for_summary("delete")
    summary_to_delete = input("")
    output_confirmation(summary_to_delete)
    print("\nPlease wait a moment while your request is processed\n")
    try:
        while True:
            events = service.events().list(calendarId=CALENDAR_ID, pageToken=page_token, showDeleted=False,
                                           timeMin=min_value).execute()
            for event in events['items']:
                if event['summary'] == summary_to_delete:
                    service.events().delete(calendarId=CALENDAR_ID, eventId=event['id']).execute()
            page_token = events.get('nextPageToken')
            if not page_token:
                break
    except KeyError:
        print(f"Error at event {event}")


def create_lines():
    for i in range(80):
        print("-", end="")
    print()


# The User Interface which aids the user in utilizing the create plan and study plan functions
def study_interface():
    print("\nWhat would you like to do?\n")
    create_lines()
    print("1. Add entries into your Google Calendar according to the Fibonacci Study Plan\n\n"
          "2. Delete entries already inserted into your Google Calendar\n\n"
          "3. Exit")
    create_lines()
    print()
    user_input = input()
    if user_input == str(1):
        create_study_plan()
    elif user_input == str(2):
        delete_study_plan()
    elif user_input == str(3):
        print("\nAlright, this program will cease execution. Have a nice day!\n")
        exit(0)
    else:
        print("Sorry that is not an acceptable input, please run the program and try again")


study_interface()
