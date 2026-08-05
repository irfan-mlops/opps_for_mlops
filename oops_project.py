class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        # self.main_menu()


    def main_menu(self):
        user_input = str(input("""
        Welcome to Chatbook!
        how would you like to proceed?
        Please choose an option:
        1. press 1 for signup
        2. press 2 for login
        3. press 3 for write a post
        4. press 4 for read a post
        5. press any other key for exit: """))
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Thank you for using Chatbook!")
            exit()  
    
    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"Welcome {self.username}! You have successfully signed up.")

user1 = chatbook()