import csv
import json

birthdays = {}

def get_info():
    cap = 1
    while len(birthdays) < cap:
        name = input("enter name").lower()
        birth= input("enter bday").lower()
        birthdays[name] = birth
    return birthdays



def write_to_json():
    get_info()
    print("Currently adding input")
    births_json = json.dumps(birthdays)
    f = open("birthdict.json", "a")
    f.write(births_json +"\n")
    f.close()

write_to_json()

def add_another():
    add_person = input("Another? y/n").lower()
    if add_person == "y":
        write_to_json()
    if add_another == "n":
        print("bye")

add_another()