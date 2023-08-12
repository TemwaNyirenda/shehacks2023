import os.path
import json

twilio_cred_file_path = "/home/girlcode/Desktop/mukuru_wtc_hackathon_2023/twilio_cred.json"


def get_twilio_cred():

    validate_file_path()


    while True:
        
        with open(twilio_cred_file_path, "r") as read_cred:

            try:
                twilio_cred = json.load(read_cred)
                return twilio_cred["account_sid"], twilio_cred["auth_token"]
            except:
                error_message = "Could not read file \"" + twilio_cred_file_path + "\" as json file"
                get_new_twilio_cred_file_path(error_message)

    


def validate_file_path():

    while True:
        check_file = os.path.isfile(twilio_cred_file_path)

        if check_file:
            print("Twilio credentials file exists")
            break

        error_message = "Could not find Twilio credentials file in \"" + twilio_cred_file_path + "\""
        get_new_twilio_cred_file_path(error_message)


def get_new_twilio_cred_file_path(message):
    global twilio_cred_file_path
    print("\n*** " + message + " ***")
    print("*** Please enter a new file path for the Twilio cred ***\n")

    twilio_cred_file_path = input()


if __name__ == "__main__":
    get_twilio_cred()