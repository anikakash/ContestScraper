import requests
import datetime
from dateutil import tz
import pytz
from dateutil import parser
import pytz



#---------------------- Functions-------------------------------------

# convert second to hours
def convert(n):
    return str(datetime.timedelta(seconds = n))

#UTC To BDT TIME :
def ChangeTime(time):
    sunset_today = Details_Of_CF[i]
    nz_zone = pytz.timezone('Asia/Dhaka')
    parsed_date = parser.parse(sunset_today).astimezone(nz_zone)
    return parsed_date

# Is Today or Not Checker:

def is_today_status(val):
    if val == "No":
        print("This contest is not happening today")
    elif val =="Yes":
        print("Today is the contest")
    elif val == "CODING":
        print("Contest is Running....")
    else :
        print("Later")
#------------------Functions End Here-------------------------------


#==================Main Programm=====================================


# ------------------- CODE FORCES START FROM HERE ----------------------

response = requests.get('https://kontests.net/api/v1/codeforces')
print("\n\n------------------- CODE FORCES START FROM HERE ----------------------\n")
# print(response.status_code)
# print(response.json())
CF_List_Size = len(response.json())
index = 0
while index<2:
    Details_Of_CF = response.json()[index]
    for i in Details_Of_CF:
        if i == "start_time" or i == "end_time":
            print(f'{i} : {ChangeTime(Details_Of_CF[i])} ')
        elif i == "duration":
            min = int(Details_Of_CF[i])
            print(f'{i} : {convert(min)} Hours ')
        elif i == "in_24_hours" or i == "status":
           is_today_status(Details_Of_CF[i])
        else: print(f'{i} : {Details_Of_CF[i]} ')
    index+=1
    print("\n---------------------------------END HERE ----------------------\n")
print('------------------- CODE FORCES END HERE ----------------------\n\n')


response = requests.get('https://kontests.net/api/v1/code_chef')
print("\n\n------------------- CODE CHEF START FROM HERE ----------------------\n")
# print(response.status_code)
# print(response.json())
CF_List_Size = len(response.json())
index = 0
while index<CF_List_Size:
    Details_Of_CF = response.json()[index]
    for i in Details_Of_CF:
        if i == "start_time" or i == "end_time":
            print(f'{i} : {ChangeTime(Details_Of_CF[i])} ')
        elif i == "duration":
            min = int(Details_Of_CF[i])
            print(f'{i} : {convert(min)} Hours ')
        elif i == "in_24_hours" or i == "status":
           is_today_status(Details_Of_CF[i])
        else: print(f'{i} : {Details_Of_CF[i]} ')
    index+=1
    print("\n---------------------------------END HERE ----------------------\n")
print('------------------- CODE CHEF END HERE ----------------------\n\n')


response = requests.get('https://kontests.net/api/v1/at_coder')
print("\n\n------------------- AT CODER START FROM HERE ----------------------\n")
# print(response.status_code)
# print(response.json())
CF_List_Size = len(response.json())
index = 0
while index<2:
    Details_Of_CF = response.json()[index]
    for i in Details_Of_CF:
        if i == "start_time" or i == "end_time":
            print(f'{i} : {ChangeTime(Details_Of_CF[i])} ')
        elif i == "duration":
            min = int(Details_Of_CF[i])
            print(f'{i} : {convert(min)} Hours ')
        elif i == "in_24_hours" or i == "status":
           is_today_status(Details_Of_CF[i])
        else: print(f'{i} : {Details_Of_CF[i]} ')
    index+=1
    print("\n---------------------------------END HERE ----------------------\n")
print('-------------------AT CODER END HERE ----------------------\n\n')
