from _datetime import datetime


def get_data_of_user_100_birthday():
    user_name = input("Write your name")
    user_age = input("Write your age")

    current_data = datetime.now()
    current_year = current_data.year
    old_in = (100 - int(user_age)) + current_year

    print("So ", user_name, "you are " , user_age, "years old.\nSo your 100 birthday will be in  ", old_in)


get_data_of_user_100_birthday()