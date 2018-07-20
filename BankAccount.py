import hashlib
import os.path
accounts = {}

salts = []

def get_salt():
        file = open("salts.txt", "r")
        for line in file:
                salts.append(line)
        print(salts)

def salt_password(password):
        print(salts)
        indexA = ord('a')
        password = password.lower()
        last_letter = password[-1]
        if not last_letter.isalnum():
                index = 0
        elif last_letter.isnumeric():
                last_later = int(last_letter)
        else:
                indexL = ord(last_letter)
                index = indexL - indexA
                print(salts[index])
        
def read_file():
        if not os.path.isfile("accounts.txt"):
                return
        f = open("accounts.txt", "r")
        for line in f:
                print(line)
                words = line.split(" ")
                words.pop()
                #code to. update() your dictionary using
                # words[0], words[1]
                username = words[0]
                password = words[1]
                PIN = words[2]
                balance = words[3]
                accounts.update({words[0] : [password, PIN, balance]})
        f.close()

def write_file():
        f = open("accounts.txt", "w")
        for username in accounts:
                f.write(username + " ")
                info = accounts[username]
                for item in info:
                        f.write(str(item) + " ")
                f.write("\n")
        f.close()
def hasher(password):
        b = bytes(password, 'utf-8')
        m = hashlib.sha256(b)
        m = m.hexdigest()
        return m


def login():

        print("Logging in... ")
        username = input ("Please enter your username ")
        if not accounts.get (username):
            print("Please enter a valid username. ")
            return
        actualPassword = accounts[username][0]
        for i in range(0,6):
            password = input ("Please enter your password ")
            password = hasher(password)
            if i == 5:
                print("Locked out... sorry... NOT sorry :*( ")
                break
        
            if password == actualPassword:
                print("Welcome, " + username + "!")
                view = input ("Would you like to view your balance? ")
                if view.lower() == 'yes':
                        print("Ok here is your balance:" + str(accounts[username][2]))
                else:
                        print("Ok, goodbye!")
                transfer = input ("Would you like to transfer money into an other person's account? ")
                if transfer.lower() == 'yes':
                        moneyTransfer = int(input ("How much? "))
                        accounts[username][2] -= moneyTransfer
                        if moneyTransfer < (accounts[username][2]):
                                print("Invalid transfer")
                        else:
                                print("You have transfered:" + str(moneyTransfer))
                else:
                        withdraw = input ("Would you like to withdraw money from your account? ")
                        if withdraw.lower() == 'yes':
                                input ("How much? ")
                        else:
                                print("Ok, have a good day!")
                withdraw = input ("Would you like to withdraw money from your account? ")
                if withdraw.lower() == 'yes':
                        input ("How much? ")
                        accounts[username][2] -= moneyTransfer
                else:
                        print("Ok, have a good day!")            
            else:
                print("Wrong password, try again. ")

get_salt()
salt_password("tac")
read_file()
message = input ("Enter 'C' if you would you like to create a new bank account, or enter 'L' to login to your current account. (or press 'Q' to quit)")
while message != 'Q':
    if message == 'C':
        username = input ("Create a username. ")
        while accounts.get(username):
                username = input("Username taken-- Try a new one: ")
        password = input ("Create a password. ")
        password = password + salt_password(password)
        password = hasher(password)
   
        PIN = input ("Pleasae enter a PIN number to secure your information. ")
        PIN = hasher(PIN)
        accounts.update({username : [password, PIN, 0]})
    elif message == 'L':
         login()
    else:
        print("Please enter a valid input. ")
        
    message = input ("Enter 'C' if you would you like to create a new bank account, or enter 'L' to login to your current account.")
write_file()
