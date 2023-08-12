import whatsapp_chatbot.db_operations as db_operations
import whatsapp_chatbot.retrieve_data_from_api as retrieve_data

from_country_group_choice = ""
from_country = ""
to_country_group_choice = ""
to_country = ""
chosen_product = ""
product_data = []
amount = 0


def execute_current_question(user_data, user_request):

    current_question = user_data[2]

    if current_question == 0:
        return execute_question_0(user_data, user_request)
    elif current_question == 1:
        return execute_question_1(user_data, user_request)
    elif current_question == 2:
        return execute_question_2(user_data, user_request)
    elif current_question == 3:
        return execute_question_3(user_data, user_request)
    elif current_question == 4:
        return execute_question_4(user_data, user_request)
    elif current_question == 6:
        return execute_question_6(user_data, user_request)
    elif current_question == 7:
        return execute_question_7(user_data, user_request)
    elif current_question == 8:
        return execute_question_8(user_data, user_request)
    elif current_question == 9:
        return execute_question_9(user_data, user_request)
    elif current_question == 10:
        return execute_question_10(user_data, user_request)
    elif current_question == 11:
        return execute_question_11(user_data, user_request)
    else:
        print("\n** INTERNAL ERROR: Incorrect current question retrieved from user data **\n")


def get_current_question_message(current_question_num):

    if current_question_num == 0:
        return question_0_message()

    elif current_question_num == 1:
        return question_1_message()

    elif current_question_num == 2:
        return question_2_message()
        
    elif current_question_num == 3:
        return question_3_message()
       
    elif current_question_num == 4:
        return question_4_message()
        
    elif current_question_num == 5:
        return question_5_message()
        
    elif current_question_num == 6:
        return question_6_message()
    
    elif current_question_num == 7:
        return question_7_message()
    
    elif current_question_num == 8:
        return question_8_message()
    
    elif current_question_num == 9:
        return question_9_message()
    
    elif current_question_num == 10:
        return question_10_message()
    
    elif current_question_num == 11:
        return question_11_message()
    
    elif current_question_num == 12:
        return question_12_message()
    
    else:
        return "Haven't coded up to that point"
    

def question_0_message():
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
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(0)


    if user_choice == 1:
        db_operations.update_user_data(user_data[1], ["current_question = 1"])
        return get_current_question_message(1)
    elif user_choice == 2:
        db_operations.delete_user_data(user_data[1])
        return "Unfortunately, you need to setup your preferences in order to use the chatbot"
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(0)


def question_1_message():
    return "Awesome! First you need to select what format you would like the chatbot to reply in:\n\
1. Text"


def execute_question_1(user_data, user_request):

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(1)


    if user_choice == 1:
        db_operations.update_user_data(user_data[1], ["current_question = 2", "reply_as_text = 1"])
        return get_current_question_message(2)
    elif user_choice == 2:
        db_operations.update_user_data(user_data[1], ["current_question = 2", "reply_as_text = 2"])
        return get_current_question_message(2)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(1)


def question_2_message():
    return "Great! Next can you select the language that you want the chatbot to use:\n" + \
"\n".join(db_operations.get_list_of_languages())


def execute_question_2(user_data, user_request):

    num_lang_choices = len(db_operations.get_list_of_languages())

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(2)



    if user_choice in range(1, num_lang_choices + 1):
        db_operations.update_user_data(user_data[1], ["current_question = 3", "language = " + str(user_choice)])
        return get_current_question_message(3)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(2)


def question_3_message():
    return "Thank you! You've set up your preferences.\n\
Would you like to continue?\n\
1. Yes\n\
2. No"


def execute_question_3(user_data, user_request):

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(3)



    if user_choice == 1:
        db_operations.update_user_data(user_data[1], ["current_question = 4"])
        return get_current_question_message(4)
    elif user_choice == 2:
        return "Okay, come back whenever you're available"
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(3)
    

def question_4_message():
    return "Welcome to Mukuru Maverick's Main Menu\n\
---\n\
Would you like to:\n\
1. Learn more about Mukuru\n\
2. Use Mukuru's Remittance Calculator"


def execute_question_4(user_data, user_request):

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(4)



    if user_choice == 1:
        return get_current_question_message(5)
    elif user_choice == 2:
        db_operations.update_user_data(user_data[1], ["current_question = 6"])
        return get_current_question_message(6)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(4)


def question_5_message():
    return "Mukuru helps you move money around Africa.\n\
Sending cash for instant collection\n\
or topping up a bank account or mobile wallet,\n\
has never been easier.\n\
We use the latest mobile and web-based technologies\n\
to give you the best experience possible."


def question_6_message():
    return "Okay, first we need you to select the country you're sending from.\n\
Please select the group that your country falls under:\n" + \
list_query(retrieve_data.retrieve_countries_dict().keys())


def execute_question_6(user_data, user_request):
    global from_country_group_choice

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(6)


    # if user_choice == 1:
    #     country_group = "A, B, C"
    # elif user_choice == 2:
    #     country_group = "D, E, F"
    # elif user_choice == 3:
    #     country_group = "G, H, I"
    # elif user_choice == 4:
    #     country_group = "J, K, L"
    # elif user_choice == 5:
    #     country_group = "M, N, O"
    # elif user_choice == 6:
    #     country_group = "P, Q, R"
    # elif user_choice == 7:
    #     country_group = "S, T, U"
    # elif user_choice == 8:
    #     country_group = "V, W, X"
    # elif user_choice == 9:
    #     country_group = "Y, Z"   

    country_group_list = list(retrieve_data.retrieve_countries_dict().keys())
    country_group_list.sort()
    print("\t\t" + str(country_group_list))
    from_country_group_choice = country_group_list[user_choice - 1]

    if user_choice >= 1 and user_choice <= 9:
        db_operations.update_user_data(user_data[1], ["current_question = 7", "from_country_selection = \"" + from_country_group_choice + "\""])
        return get_current_question_message(7)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(6)


def question_7_message():
    from_country_group = from_country_group_choice
    return "Please select a country:\n" + \
list_query(retrieve_data.retrieve_countries_dict()[from_country_group])   


def execute_question_7(user_data, user_request):
    global from_country

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(7)
    
    from_country_group = user_data[6]

    country_list = retrieve_data.retrieve_countries_dict()[from_country_group]

    if user_choice >= 1 and user_choice <= len(country_list):
        choosen_country = country_list[user_choice - 1]
        from_country = choosen_country
        print("\t\tchosen country " + choosen_country)
        db_operations.update_user_data(user_data[1], ["current_question = 8", "from_country_selection = \"" + choosen_country + "\""])
        return get_current_question_message(8)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(7)


def question_8_message():
    return "Next we need you to select the country you're sending to.\n\
Please select the group that your country falls under:\n" + \
list_query(retrieve_data.retrieve_countries_dict().keys())


def execute_question_8(user_data, user_request):
    global to_country_group_choice

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(6)


    # if user_choice == 1:
    #     country_group = "A, B, C"
    # elif user_choice == 2:
    #     country_group = "D, E, F"
    # elif user_choice == 3:
    #     country_group = "G, H, I"
    # elif user_choice == 4:
    #     country_group = "J, K, L"
    # elif user_choice == 5:
    #     country_group = "M, N, O"
    # elif user_choice == 6:
    #     country_group = "P, Q, R"
    # elif user_choice == 7:
    #     country_group = "S, T, U"
    # elif user_choice == 8:
    #     country_group = "V, W, X"
    # elif user_choice == 9:
    #     country_group = "Y, Z"   

    country_group_list = list(retrieve_data.retrieve_countries_dict().keys())
    country_group_list.sort()
    to_country_group_choice = country_group_list[user_choice - 1]

    if user_choice >= 1 and user_choice <= 9:
        db_operations.update_user_data(user_data[1], ["current_question = 9", "to_country_selection = \"" + to_country_group_choice + "\""])
        return get_current_question_message(9)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(6)


def question_9_message():
    to_country_group = to_country_group_choice
    return "Please select a country:\n" + \
list_query(retrieve_data.retrieve_countries_dict()[to_country_group])   


def execute_question_9(user_data, user_request):
    global to_country
    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(9)
    
    to_country_group = user_data[7]

    country_list = retrieve_data.retrieve_countries_dict()[to_country_group]

    if user_choice >= 1 and user_choice <= len(country_list):
        choosen_country = country_list[user_choice - 1]
        to_country = choosen_country
        print("\t\tchosen country " + choosen_country)
        db_operations.update_user_data(user_data[1], ["current_question = 10", "to_country_selection = \"" + choosen_country + "\""])
        return get_current_question_message(10)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(9)
    

def question_10_message():
    products_list = retrieve_data.get_list_available_products(from_country, to_country)

    if not products_list:
        return "There is no products available\n\
Send anything to go back to the main menu\n"
    
    return "Please select an available product:\n" + \
list_query(products_list)   


def execute_question_10(user_data, user_request):
    global chosen_product

    products_list = retrieve_data.get_list_available_products(user_data[6], user_data[7])

    if not products_list:
        db_operations.update_user_data(user_data[1], ["current_question = 4"])
        return "There is no products available\n\
Going back to the main menu\n" + get_current_question_message(4)

    if (not products_list):
        db_operations.update_user_data(user_data[1], ["current_question = 4"])
        return "No products available\n" + get_current_question_message(4)

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(10)
    

    if user_choice >= 1 and user_choice <= len(products_list):
        chosen_product = products_list[user_choice - 1]
        print("\t\tchosen product " + chosen_product)
        db_operations.update_user_data(user_data[1], ["current_question = 11", "chosen_product = \"" + chosen_product + "\""])
        return get_current_question_message(11)
    else:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(10)

    
def question_11_message():
    global product_data

    product_data = retrieve_data.get_chosen_product_data(chosen_product)
    return "The currency that you will send will be " + product_data['payInCurrencyCode'] + "\n\
and the recepient will receive in " + product_data['payOutCurrencyCode'] +"\n\
The fee will be " + product_data['fee']['currencyCode'] + " " + str(product_data['fee']['amount']) + "\n\
And the rate will be " + str(product_data['rate']['rate']) + "\n\
Please the amount you want to send:"


def execute_question_11(user_data, user_request):
    global amount

    incoming_msg = user_request.values.get('Body', '')
    try:
        user_choice = int(incoming_msg)
    except:
        return "I don't understand \"" +incoming_msg +"\"\n---\n" + get_current_question_message(11)
    
    amount = user_choice

    if amount < product_data['fee']['amount']:
        return "Amount you'll send is less than the fees\nPlease send a new amount\n---\n" + get_current_question_message(11)
    
    db_operations.update_user_data(user_data[1], ["current_question = 4"])
    return get_current_question_message(12)


def question_12_message():
    return "The recepient will recieve " + product_data['payOutCurrencyCode'] + " " + str(calculate_receipient_amount())


def list_query(query):
    query_list_string = ""

    q_num = 1
    for q in query:
        query_list_string += str(q_num) + ". " + q + "\n"
        q_num += 1

    
    return query_list_string

def calculate_receipient_amount():
    print(amount)
    print(product_data['fee']['amount'])
    print(product_data['rate']['rate'])
    return round((amount - product_data['fee']['amount']) * product_data['rate']['rate'])
