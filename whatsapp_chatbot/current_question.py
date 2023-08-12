import whatsapp_chatbot.db_operations as db_operations

def execute_current_question(user_data, user_request):
    current_question = user_data[2]

    if current_question == 0:
        return execute_question_0(user_data, user_request)
    else:
        print("\n** INTERNAL ERROR: Incorrect current question retrieved from user data **\n")


def get_current_question_message(current_question_num):
    if current_question_num == 0:
        return "Welcome to Mukuru Maverick's Whatsapp Chatbot!!!\n\
---\n\
Before we continue, let's setup your chatbot preferences.\n\
Would you like to continue:\n\
1. Yes\n\
2. No"


def execute_question_0(user_data, user_request):

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "** \"" + incoming_msg + "\" is an invalid choice **\n\
Choose * 1 * for Yes, choose * 2 * for No\n\
(Please only reply with the number of your choice)"


    if user_choice == 1:
        db_operations.update_user_data(user_data[1], ["current_question = 1"])
        return "Awesome! First you need to select what format you would like the chatbot to reply in:\n\
1. Text\n\
2. Voice Notes"
    elif user_choice == 2:
        db_operations.delete_user_data(user_data[1])
        return "Unfortunately, you need to setup your preferences in order to use the chatbot"
    else:
        return "** \"" + incoming_msg + "\" is an invalid choice **\n\
Choose * 1 * for Yes, choose * 2 * for No\n\
(Please only reply with the number of your choice)"

def get_user_message(user_request):
    return user_request.values.get('Body', '')
