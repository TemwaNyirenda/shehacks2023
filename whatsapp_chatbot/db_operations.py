# !/usr/bin/python

import sqlite3

import whatsapp_chatbot.time_operations as time_operations

def find_user_in_db(user_num):
    conn = sqlite3.connect('database/user_selection.sqlite')
    print("\nOpened database successfully - finding user in database")

    select_return = conn.execute("SELECT * FROM user_selection")

    for row in select_return:
        if user_num == row[1]:
            print("\nUser in database")
            conn.close()
            print("\nClosed database")
            return row


    print("\nUser not in database")
    conn.close()
    print("\nClosed database - finding user in database")
    return None


def insert_user_into_db(user_num):
    conn = sqlite3.connect('database/user_selection.sqlite')
    cursor = conn.cursor()
    print("\nOpened database successfully - inserting user in database")

    cursor.execute("INSERT INTO user_selection(whatsapp_number, last_reply_time) VALUES ('" + user_num + "', '" + time_operations.get_current_time_for_db() + "')")

    conn.commit()
    print("\nSuccessfully inserted user into database")

    conn.close()
    print("\nClosed database - inserting user in database")


"""
    format of column value list example:
    ["current_question = 2", "language = 3", "last_reply_time = *time*"]
"""
def update_user_data(user_num, column_value_list):
    conn = sqlite3.connect('database/user_selection.sqlite')
    cursor = conn.cursor()
    print("\nOpened database successfully - updating user in database")

    

    update_string = "UPDATE user_selection SET " + ", ".join(column_value_list) + \
        ", " + "last_reply_time = \"" + time_operations.get_current_time_for_db() + "\"" + \
        " WHERE whatsapp_number = \"" + user_num + "\""
    

    cursor.execute(update_string)

    conn.commit()
    print("\nSuccessfully updated user into database")

    conn.close()
    print("\nClosed database - updating user in database")


def delete_user_data(user_num):
    conn = sqlite3.connect('database/user_selection.sqlite')
    cursor = conn.cursor()
    print("\nOpened database successfully - deleting user from database")

    

    delete_string = "DELETE FROM user_selection WHERE whatsapp_number = \"" + user_num + "\""
    

    cursor.execute(delete_string)

    conn.commit()
    print("\nSuccessfully deleted user from database")

    conn.close()
    print("\nClosed database - deleting user from database")


if __name__ == "__main__":
#    print(find_user_in_db("+27000000000"))
#    insert_user_into_db("+27444444444")
    # update_user_data("+27222222222", ["current_question = 700", "language = 700"])
#    insert_user_into_db("+27555555555")
   delete_user_data("+27555555555")


    