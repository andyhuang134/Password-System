import json
import random
import string

class json_class:
    def __init__(self):
        self.json_file = r"accounts.json"
    # saves the username and password to the json file
    def json_save(self, username, password):
        self.json_format = {"username": username, "password": password}

        with open(self.json_file, "r") as f:
            read_file = f.read()
            json_dict = json.loads(read_file)
            json_dict.append(self.json_format)

        with open(self.json_file, "w") as f:
            json.dump(json_dict, f, indent=4)
    # returns the json file 
    def json_open(self):
        with open(self.json_file, "r") as f:
            read_file = f.read()
            json_dict = json.loads(read_file)
        return json_dict

# password checker
class password_checker:
    def __init__(self, password):
        self.password = password

    def check_number(self):
        for letter in self.password:
            if letter.isnumeric():
                return True
        print("you need at least 1 number")

    def check_capital(self):
        for letter in self.password:
            if letter.isupper():
                return True
        print("you need at least 1 capital letter")

    def check_punctuation(self):
        for letter in self.password:
            if letter in string.punctuation:
                return True
        print("you need at least 1 punctuation")

    def check_length(self):
        length = len(self.password)
        if length >= 8:
            return True
        print("password needs to be at least 8 characters long")

    def main(self):
        check_number = self.check_number()
        check_capital = self.check_capital()
        check_punctuation = self.check_punctuation()
        check_length = self.check_length()

        if check_number and check_capital and check_punctuation and check_length == True:
            return True
        else:
            check_number
            check_capital
            check_punctuation
            return False


class password_generator:

    def __init__(self, username, numbers, characters, punctuations, capitals):
        self.numbers = numbers
        self.characters = characters
        self.punctuations = punctuations
        self.capitals = capitals
        self.username = username

    def add_numbers(self):
        numbers = "1234567890"
        choose_number = random.choice(numbers)
        return str(choose_number)

    def add_characters(self):
        characters = 'abcdefghijklmnopqrstuvwxyz'
        choose_character = random.choice(characters)
        return str(choose_character)

    def add_punctuations(self):
        punctuation_list = ["'", '"', '!', '@', '#', '$', '%', '^', '&', '*',
                            '(', ')', '_', '+', '-', '=', '[', ']', ';', ':', '', ',', '.', '<', '>', '/', '?', '~', '`']
        choose_punctuation = random.choice(punctuation_list)
        return str(choose_punctuation)
    def add_capitals(self):
        capitals = 'abcdefghijklmnopqrstuvwxyz'
        choose_capital = random.choice(capitals.upper())
        return str(choose_capital)
    
    # adds letters/symbols/numbers all together
    def main(self):
        generated_password = []
        actual_password = ""
        
        for numbers in range(self.numbers):
            generated_password.append(self.add_numbers())
        for characters in range(self.characters - self.capitals):
            generated_password.append(self.add_characters())
        for puncutations in range(self.punctuations):
            generated_password.append(self.add_punctuations())
        for capitals in range(self.capitals):
            generated_password.append(self.add_capitals())
        # shuffles the chosen letters/symbols/numbers
        random.shuffle(generated_password)
        for i in generated_password:
            actual_password += i
            
        # saves the username and password to the json file
        account = json_class()
        account.json_save(self.username, actual_password)
    
# requirements for making a password
class password_requirements:
    def __init__(self, numbers, characters, punctuations, capitals):
        self.numbers = numbers
        self.characters = characters
        self.punctuations = punctuations
        self.capitals = capitals

    def check_punctuations(self):
        if self.punctuations < 1:
            print("You need atleast 1 punctuation")
            return False
        return True

    def check_numbers(self):
        if self.numbers < 1:
            print("You need atleast 1 number")
            return False
        return True
    def check_capitals(self):
        if self.capitals < 1:
            print("You need atleast 1 capital")
            return False
        return True
            
    def check_characters(self):
        if self.characters < self.capitals:
            print("You need more characters than capitals")
            return False
        return True
    def main(self):
        check_punctuations = self.check_punctuations()
        check_numbers = self.check_numbers()
        check_capitals = self.check_capitals()
        check_characters = self.check_characters()
        
        if check_punctuations and check_numbers and check_capitals and check_characters == True:
            return True
        else:
            check_punctuations
            check_numbers
            check_capitals
            check_characters
            return False
        
# user create password
def create_password(username):
    while True:
        password = input("Input your password ")

        password_check = password_checker(password)
        checked_password = password_check.main()
        if checked_password == True:
            account = json_class()
            account.json_save(username, password)
            break

# checks if username is in the json file
def check_username(username):
    account = json_class()
    accounts = account.json_open()

    for acc in range(len(accounts)):
        if username == accounts[acc]["username"]:
            return True
    return False

# checks the username and password
def check_account(username, password):
    account = json_class()
    accounts = account.json_open()
    account_dict = {"username": username, "password": password}

    def check():
        for acc in range(len(accounts)):  # check account
            if account_dict["username"] == accounts[acc]["username"]:
                if password != accounts[acc]["password"]:
                    print('wrong password')
                    return False

                elif password == accounts[acc]["password"]:
                    print("You have logged into your crypto account")
                    return True

    check_password = check()
    if check_password == False:
        while True:
            password = input("enter your password ")
            check_password = check()
            if check_password == True:
                break
        return True

# bot generated password
def system_password(username):
    while True:
        try:
            numbers = int(input("how many numbers "))
            characters = int(input("how many characters "))
            punctuations = int(input("how many punctuations "))
            capitals = int(input("how many capitals "))
            password_req = password_requirements(numbers, characters, punctuations, capitals)
            password_requirement = password_req.main()
            # creates password if requirements are met
            if password_requirement == True:
                generate_password = password_generator(username, numbers, characters, punctuations, capitals)
                generated_password = generate_password.main()
                print("Your crypto account has been created")
                break
        except ValueError:
            print("Input is not a number")


def main():
    option = input("Login ").lower()
    while True:
        if option == "login":
            username = input("Enter your username ")
            username_in_json = check_username(username)
            if username_in_json == True:

                password = input(f"Enter your password ")
                checked_account = check_account(username, password)
                if checked_account == True:
                    break
            
            elif username_in_json == False:
                print(f"The account {username} was not found.")
                password_option = input(
                    "How would you like to create the new password? (own/system) ").lower()
                if password_option == "own":
                    while True:
                        create_password(username)
                        print("Your crypto account has been created")
                        break
                    break
                elif password_option == "system":
                    system_password(username)
                    break
        else:
            option = input("No other option other than login ").lower()


if __name__ == "__main__":
    main()
