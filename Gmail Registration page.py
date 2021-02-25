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
# 3. otp management
# 4. storing data
# <img src = "https://i1.wp.com/www.scorershub.com/wp-content/uploads/2019/06/create-Gmail-accountb-compressor.png?w=910&ssl=1">

# In[1]:


username = ['Sowmya144'  ,'Surekha555','Suresh764','Koushika' ,'Krish24', 'Sumita82', 'Nikitha', 'Satyam']
password = ['passcode','gmailpass' ,'pvsuresh1' ,'codemail' ,'Apassis', 'passmail', 'Nobitha', 'codepass']
phone_no = ['1234567890' ,'9876543210' ,'3456789876' ,'2345678987' ,'9876543212' ,'6263332517' ,'1234567890' ,'9876543210']
gender   = ['Female' ,'Female' ,'Male' ,'Female' ,'Male' ,'Female' ,'Female' ,'Male']
fname    = ['Sowmya'  ,'Surekha' ,'Suresh' ,'Koushika' ,'Krishna' , 'Sumita' , 'Nikitha' , 'Satyam']
lname    = ['Sri' ,'Shukla' ,'Paleti' ,'Retu' ,'Sai' ,'Sri' ,'Sai' ,'Kumar']
dob      = ['27-Jul-2003', '12-Dec-1975','23-Dec-1970' ,'13-May-2001' ,'23-Jun-1997' ,'20-Apr-1997' ,'23-May-1987' ,'10-Mar-1996']


# In[2]:


sample_data = {'username':username, 'password' : password, 'phone_no' : phone_no , 'gender' : gender , 'fname' : fname,
               'lname' : lname, 'dob' :dob}


# In[3]:


sample_data.keys()


# In[4]:


sample_data['username']


# In[5]:


import pandas as pd 
df = pd.DataFrame(sample_data)


# In[6]:


df


# In[7]:


import seaborn as sns 
sns.countplot(x = 'gender', data = df)


# #### Function for taking fname and lname

# In[8]:


firstname = [] ; lastname = []
def flname():
    first_name = input('Enter First Name : ')
    while True:
        if first_name == '':
            break
        else:
            last_name = input('Enter Last Name :')
            firstname.append(first_name)
            lastname.append(last_name)
            if last_name != '':
                break


# #### Fucntion for taking usernames and passwords

# In[9]:


user = [] ; pas = []
def user_pass():
    raw_user_name = input("Enter Username ['xyz@gmail.com'] : ").split('@gmail.com')
    if raw_user_name[0] in username:
        print('username already exists.')   
    else:
        Password = input('Enter Password: ')
        if len(Password)> 8:
            if Password.isalnum() != True:
                print('Enter uppercases, lowercases and use atleast 1 number')
            else:
                user.append(raw_user_name[0])
                pas.append(Password)
        else:
            print('use atleast 8 characters.')


# In[12]:


user_pass()


# #### Function to take dob, gender, phonenumber.

# In[13]:


Date = [] 
def dgp():
    import datetime, random 
    m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    day = int(input('Enter Birth Date : [12, 23, 44...] '))
    if day > 31:
        print('Invalid Input.')
    else:
        month = input('Enter Birth Month : [Jan, Feb, Mar, ...] ').capitalize()
        if month in m:
            #x = datetime.datetime.now()
            #Y = x.strftime('%y')
            year = int(input('Enter Birth year : [1987, 1956, 2013,...] '))
            if year >= 2020:
                print('Invalid Year')
            else:
                DOB = str(day) + '-' + str(month) + '-' + str(year) 
                Date.append(DOB)
        else:
            print('Enter valid Month Name')


# In[14]:


phonenum = []
def mobile():
    import random 
    MOB = input('Enter 10 Digit Mobile Number : ')
    if MOB not in phonenum:
        if len(MOB) != 10:
            print('Invalid Input')
        else:
            code_generation = random.randint(627463,736453)
            code = 'G-'+ str(code_generation) + 'is your One Time Google Verification Code.'
            print('Enter the otp sent to your mobile number ending with ',MOB[-3:])
            print(code)
            otp_enter = input('Enter OTP : ')
            if otp_enter == str('G-'+ str(code_generation)):
                print('Please accept the Terms & Conditions to create your account.')
                answer = input('Accept the T&Cs Enter 1 : ')
                if answer != '1':
                    print('Invalid Response')
                else:
                    phonenum.append(MOB)
                    print('Account Created Succesfully.')
            else:
                print('Invalid OTP.')
    else:
        print('Number already exists.')


# In[15]:


Gender = []
def gender():
    print('Enter Gender : ["Male, Female"] : ')
    gen_int = input('Enter Gender : ').capitalize()
    if gen_int == 'Male' or 'Female':
        Gender.append(gen_int)
    else:
        print('Invalid Input')


# In[16]:


flname()


# In[17]:


dgp()


# In[18]:


gender()


# In[19]:


mobile()


# In[20]:


phonenum.append('9849966528')
firstname, lastname, Date, phonenum, Gender , user, pas


# In[ ]:


data2 = {'username':user, 'password' : pas, 'phone_no' : phonenum , 'gender' : Gender , 'fname' : firstname,
               'lname' : lastname, 'dob' :Date}


# In[ ]:


df2 = pd.DataFrame(data2)


# In[ ]:


df2


# In[ ]:


df


# In[ ]:


final_data = pd.concat([df,df2])


# In[ ]:


final_data


# In[24]:


day_data = final_data.to_csv('bank-data.csv')


# In[25]:


login_success = [] ; login_failed = []
def login():
    bank = pd.read_csv('bank-data.csv', index_col = 'username')
    EMAIL = input('Enter email: ').split("@")
    em = EMAIL[0]
    if em in bank.index.to_list():
        PASS = input('Enter Password : ')
        if bank['password'][em] == PASS:
            import time
            t = time.localtime()
            currenttime = time.strftime('%H : %M: %S', t)
            print('Login Successfull.')
            login_success.append(str(em) + ' at ' + str(currenttime))
        else:
            import time
            t = time.localtime()
            currenttime = time.strftime('%H : %M: %S', t)
            print('Incorrect Password')
            login_failed.append(str(em) + ' at ' + str(currenttime))
    else:
        print('EMAIL doesnot exist!.')


# In[26]:


login()


# In[27]:


login_success, login_failed


# In[28]:


bank = pd.read_csv('bank-data.csv', index_col = 'username')


# In[29]:


bank


# In[30]:


bank.columns


# In[31]:


bank.index


# In[32]:


list(bank.index)


# In[33]:


bank['password']['Sowmya144'] == 'passcode'


# In[34]:


bank['dob']['Sowmya144']


# In[35]:


login()


# In[36]:


login_success


# In[37]:


login_failed


# In[38]:


login()


# In[39]:


data = 'https://github.com/paletinaveena/Gmail-Registration/blob/main/Gmail_members_details.csv'


# In[40]:


import webbrowser as wb 
wb.open('https://github.com/paletinaveena/Gmail-Registration/blob/main/Gmail_members_details.csv')


# In[41]:


help('url')


# In[42]:


import urllib.request
response = urllib.request.urlopen('https://github.com/paletinaveena/Gmail-Registration/blob/main/Gmail_members_details.csv')
html = response.read()


# In[43]:


url = 'https://github.com/paletinaveena/Gmail-Registration/blob/main/Gmail_members_details.csv'


# In[44]:


html


# In[45]:


read = pd.read_html(url)


# In[46]:


read


# In[ ]:





# In[ ]:




