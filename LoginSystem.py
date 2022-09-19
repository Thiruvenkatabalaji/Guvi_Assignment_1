import pandas as pd
import re

file =open("C:\\Users\\thiru\\OneDrive\\Documents\\email_db.txt","r")
data={}
d=[];
f=[];
for i in file:
    (a,b)=i.strip().split(",");
    d.append(a)
    f.append(b)
    data =dict(zip(d,f));
       
        
def register():
    username = input("Register \n Enter a username: ")
    if username_validation(username) == True:
        if username in d:
            print("Username exist");
            print("Please proceed to login");
            login();
        else:
            password = input("Enter a password: ")
            if Password_validation(password)== True:
                db=open("C:\\Users\\thiru\\OneDrive\\Documents\\email_db.txt","a");
                db.write(username+","+password+"\n");
                print("Registered Sucessfully!!");
            else:
                print("Password incorrect,Please register again")
                register();
    else:
        print("Username incorrect,Please register again");
        register();


def username_validation(username):
    x = re.search("^[A-za-z]+.*\@+.?.+\.[A-Za-z]{2,3}$",username)
    if x:
        return True;
    else:
        return False;

def Password_validation(password):
    y = re.search("^(?=.*\d)(?=.*[A-Z])(?=.[a-z])(?=.*[@$!%#?&])[A-Za-z\d@$!%#%*?&]{6,15}$",password)
    if y:
        return True;
    else:
        return False;
    
def login():
    username = input("LOGIN \n Enter a username: ");
    if username in d:
        password = input("Enter a Password: ")
        if data[username]== password:
            print("Login Sucessfull!!")
        else:
            print("Not sucessfull")
            Forget_Password(username);
    else:
        print("Please register");
        register();

def Forget_Password(username):
    new_password = input("enter a new password: ")
    if Password_validation(new_password)== True:
        data[username]= new_password;
        file_rewrite();
    else:
        print("Re-enter the new password");
        Forget_Password(username);
    
def file_rewrite():
    open("C:\\Users\\thiru\\OneDrive\\Documents\\email_db.txt","w").close();
    db=open("C:\\Users\\thiru\\OneDrive\\Documents\\email_db.txt","a");
    for key, value in data.items():
        db.write(key+","+value+"\n");
        

print("1. Login\n2. Register");
n = int(input("Enter a number 1 or 2: "));
if n ==1:
    login();
else:
    register();
