#!/usr/bin/env python
# coding: utf-8

# 
# # <center>G-Mail Registration Project</center>
# 
# <img src = "https://www.google.com/logos/doodles/2020/stay-and-play-at-home-with-popular-past-google-doodles-cricket-2017-6753651837108767-2xa.gif">

# ### Things to focus on :
# 
# 1. uniqueness of gmail id
# 2. security of passwords
# 3. OTP management
# 4. storing data
# <img src = "https://i1.wp.com/www.scorershub.com/wp-content/uploads/2019/06/create-Gmail-accountb-compressor.png?w=910&ssl=1">

username = ['Sowmya144'  ,'Surekha555','Suresh764','Koushika' ,'Krish24', 'Sumita82', 'Nikitha', 'Satyam']
password = ['Passcode1','Gmailpass2' ,'Pvsuresh1' ,'Codemail3' ,'Apassis4', 'passMail5', 'Nobitha6', 'Codepass7']
phone_no = ['1234567890' ,'9876543210' ,'3456789876' ,'2345678987' ,'9876543212' ,'6263332517' ,'1234567890' ,'9876543210']
gender   = ['Female' ,'Female' ,'Male' ,'Female' ,'Male' ,'Female' ,'Female' ,'Male']
fname    = ['Sowmya'  ,'Surekha' ,'Suresh' ,'Koushika' ,'Krishna' , 'Sumita' , 'Nikitha' , 'Satyam']
lname    = ['Sri' ,'Shukla' ,'Paleti' ,'Retu' ,'Sai' ,'Sri' ,'Sai' ,'Kumar']
dob      = ['27-Jul-2003', '12-Dec-1975','23-Dec-1970' ,'13-May-2001' ,'23-Jun-1997' ,'20-Apr-1997' ,'23-May-1987' ,'10-Mar-1996']


existed_data = {'username':username, 'password' : password, 'phone_no' : phone_no , 'gender' : gender , 'fname' : fname,
               'lname' : lname, 'dob' :dob}


import pandas as pd 
df = pd.DataFrame(existed_data)

df # presentation of data


import seaborn as sns 
sns.countplot(x = 'gender', data = df)  # Statistics of gender


# #### Function for first name and last name

def checkName(name): # check the name whether it contains only alphabets or not 
    if name.isalpha() and name != '':
        return True
    return False
  
firstname = [] ; lastname = []
def flname():
    first_name = input('Enter First Name : ')
    if checkName(first_name):
        last_name = input('Enter Last Name :')
        if checkName(last_name) != True:
            print("Invalid Last Name Input")
            return
        firstname.append(first_name)
        lastname.append(last_name)
    else:
        print("Invalid First Name Input")


# #### Function for usernames and passwords

def checkUserName(raw_user_name): # To check uniqueness
    if raw_user_name in username:
        return False
    return True
  
def checkpassword(password): # To check validity 
    if len(password) < 8:
        return False
    if password.isalnum() != True:
        return False
    return True

newusername = [] ; password = []
def username_password():
    raw_user_name = input("Enter Username: ").split('@gmail.com')
    if checkUserName(raw_user_name[0]):
        Password = input('Enter Password: ')
        if checkpassword(Password):
            newusername.append(raw_user_name[0])
            password.append(Password)
        else:
            print("Password must contain 8 characters, uppercases, lowercases and atleast 1 number")
    else:
        print('username already exists.')


# #### Function for dob, gender, phonenumber.

from datetime import date
def checkYear(year):  # To check validity of Year
    today = date.today()
    if year > today.year:
        return False
    return True
  
def checkMonth(month): # To check validity of Month
    m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if month in m:
        return True
    return False
  
import calendar
def checkDay(day, month, year): # To check validity of no of days in entered month
    num_days = calendar.monthrange(year, month)[1]
    if day > num_days:
        return False
    return True
  
from datetime import date
def checkAge(birthDate): # To check whether candidate is above 13 years or not
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    if age >= 13:
        return True
    else:
        return False
      
import datetime
Date = [] 
def dob(): # DOB function
    year = int(input('Enter Birth year [1987, 1956, 2013,...] :'))
    if checkYear(year):
        month = input('Enter Birth Month [Jan, Feb, Mar, ...] :').capitalize()
        if checkMonth(month):
            day = int(input('Enter Birth Date [12, 23, 44...] :'))
            datetime_object = datetime.datetime.strptime(month, "%b") # converts month into month number
            month_num = datetime_object.month
            if checkDay(day, month_num, year):
                birthDate = date(year, month_num, day)
                if checkAge(birthDate):
                    DOB = str(day) + '-' + str(month) + '-' + str(year)
                    Date.append(DOB)
                else:
                    print("You must be atleast 13 years")
            else:
                print("Invalid Day Input")
        else:
            print("Invalid Month Input")
    else:
        print("Invalid Year Input")
        
Gender = []
def gender(): # Gender function
    print('Enter Gender : ["Male, Female"] : ')
    gen_int = input('Enter Gender : ').capitalize()
    if gen_int == 'Male' or 'Female':
        Gender.append(gen_int)
    else:
        print('Invalid Input')
        
def checkLength(MOB): # To check length of mobile number
    if len(MOB) != 10:
        return False
    return True
 
import random
def generateOTP(): # To generate OTP
    return random.randint(627463,736453)
 
def checkOTP(OTP_Generated): # To check OTP
    otp_enter = int(input('Enter OTP : G-'))
    if otp_enter == OTP_Generated:
        return True
    return False

def TandC(): # To accept Terms and Conditions
    print('Please accept the Terms & Conditions to create your account.')
    answer = input('Accept the T&Cs Enter 1 : ')
    if answer != '1':
        return False
    return True
 
phone_num = []
def mobile():
    MOB = input('Enter 10 Digit Mobile Number : ')
    if MOB not in phone_no:
        if MOB not in phone_num:
            if checkLength(MOB):
                OTP_Generated = generateOTP()
                code = 'G-'+ str(OTP_Generated) + ' is your One Time Google Verification Code.'
                print('Enter the OTP sent to your mobile number ending with ', MOB[-3:])
                print(code)
                if checkOTP(OTP_Generated):
                    if TandC():
                        phone_num.append(MOB)
                        print('Account Created Succesfully.')
                    else:
                        print('Invalid Response')
                else:
                    print('Invalid OTP.')
            else:
                print("Invalid Input")
        else:
            print('Number already exists.')
    else:
        print("Another Account with this number exists")

flname()

dob()

username_password()

gender()

mobile()

data2 = {'username':newusername, 'password' : password, 'phone_no' : phone_num , 'gender' : Gender , 'fname' : firstname,
               'lname' : lastname, 'dob' :Date}

df2 = pd.DataFrame(data2)

df2

final_data = pd.concat([df,df2])

final_data

day_data = final_data.to_csv('bank-data.csv')


import time
login_success = [] ; login_failed = []
def login():
    bank = pd.read_csv('bank-data.csv', index_col = 'username')
    EMAIL = input('Enter email: ').split("@")
    em = EMAIL[0]
    if em in bank.index.to_list():
        PASS = input('Enter Password : ')
        if bank['password'][em] == PASS:
            t = time.localtime()
            currenttime = time.strftime('%H : %M: %S', t)
            print('Login Successfull.')
            login_success.append(str(em) + ' at ' + str(currenttime))
        else:
            t = time.localtime()
            currenttime = time.strftime('%H : %M: %S', t)
            print('Incorrect Password')
            login_failed.append(str(em) + ' at ' + str(currenttime))
    else:
        print('EMAIL doesnot exist!.')


login()

login()

login_success

login_failed

data = 'https://github.com/paletinaveena/Gmail-Registration/blob/main/Gmail_members_details.csv'
