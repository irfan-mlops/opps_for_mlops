class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.main_menu()


    def main_menu(self):
        user_input = str(input("""
        Welcome to Chatbook!
        how would you like to proceed?
        Please choose an option:
        1. press 1 for signup
        2. press 2 for login
        3. press 3 for write a post
        4. press 4 for send_massage
        5. press any other key for exit: """))
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.send_message()
        else:
            print("Thank you for using Chatbook!")
            exit()  
    
    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.username = self.username
        self.password = self.password
        print(f"Welcome {self.username}! You have successfully signed up.")
        print("\n")
        self.main_menu()

    def login(self):
        if self.username == "" and self.password == "":
            print("Please Signup First by pressing 1 in the main menu")
            print("\n")
            self.main_menu()
        else:
            self.username = input("Enter your username: ")
            self.password = input("Enter your password: ")
            if self.username == self.username and self.password == self.password:
                print(f"Welcome {self.username}! You have successfully logged in.")
                print("\n")
                self.logged_in = True
                self.main_menu()
            else:
                print("Invalid username or password")
                print("\n")
                self.main_menu()

    def write_post(self):
        if self.logged_in == False:
            print("Please Login First by pressing 2 in the main menu")
            print("\n")
        else:
            self.post = input("Enter your post: ")
            print(f"Your post has been successfully written.")
            print(self.post)
            print("\n")
            self.main_menu() 
    
    def send_message(self):
        if self.logged_in == False:
            print("Please Login First by pressing 2 in the main menu")
            print("\n")
        else:
            txt = input("Enter a Message : ")
            friend = input("Enter a name whom to send : ")
            print(f"Message has been succussfully sended to {friend}.")

            print("/n")
            self.main_menu()

            




# user1 = chatbook()