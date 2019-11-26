#Write a function that converts hours into seconds.
def hour_to_second():
    ask_user_number = int(input('Enter the number of hours you want to convert to seconds: '))
    num_seconds = ask_user_number*3600
    print(str(ask_user_number)+' hour(s) is equal to '+str(num_seconds)+' seconds.')
hour_to_second()
