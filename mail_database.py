# -*- coding: utf-8 -*-
"""
This program allows the user to create a small database containing names
and e-mail directions. The user will be able to add, delete and edit new
entries via the menu, and store the database in a csv file
"""
import os
import csv


mails = []
name_pos = 0
mail_pos = 1
mail_header = ['Name', 'Mail']


def valid_menu_choice(which):
    if not which.isdigit():
        print(which + "needs to be the number of an entry")
        return False
    which = int(which)
    if which < 1 or which > len(mails):
        print(str(which) + "needs to be the number of an entry")
        return False
    return True

def delete_mail(which):
    if not valid_menu_choice(which):
        return
    which = int(which)
    del mails[which - 1]
    print("Deleted entry number",which)
    print()
    
def edit_mail(which):
    if not valid_menu_choice(which):
        return
    which = int(which)
    
    mail = mails[which - 1]
    print("Enter the data for a new entry. Press <enter> to leave un changed")
    
    print()
    print("Current name for this entry is '",mail[name_pos], "'")
    newname = input("Enter new name or press return: ")
    if newname == "":
        newname = mail[name_pos]
    
    print()
    print("Current mail address for this entry is '",mail[mail_pos],"'")
    new_mail = input("Enter new mail or press return: ")
    if new_mail == "":
        new_mail = mail[mail_pos]
    
    mail = [newname, new_mail]
    mails[which - 1] = mail
    
    print()
    print("The mail for the entry",which,"has been updated to:")
    print("Name: ",newname)
    print("Mail: ",new_mail)
    print()
    
def load_mail_list():
    if os.access("mail_list.csv",os.F_OK):
        f = open("mail_list.csv")
        for row in csv.reader(f):
            mails.append(row)
        f.close()
        
def save_mail_list():
    f = open("mail_list.csv", 'w', newline ='')
    for entry in mails:
        csv.writer(f).writerow(entry)
    f.close()
    
def show_mails():
    print()
    show_mail(mail_header, "")
    index = 1
    for mail in mails:
        show_mail(mail, index)
        index += 1
    print()
    
def show_mail(mail, index):
    outputstr = "{0:>3}  {1:<20}  {2:<32}"
    print(outputstr.format(index, mail[name_pos], mail[mail_pos]))
    
def create_mail():
    print("Creating a new mail entry. Please enter the data below:")
    newname = input("Please, enter the name: ")
    new_mail = input("Please, enter the mail address: ")
    mail = [newname, new_mail]
    mails.append(mail)
    print()
    print("The mail entry for",newname,"has been added successfully")
    print()
    
def menu_choice():
    """ Menu with program options """
    print("Please choose one of the following options:")
    print("    s) Show")
    print("    n) New")
    print("    e) Edit")
    print("    d) Delete")
    print("    q) Quit")
    choice = input("Your choice: ")
    if choice.lower() in ["s", "n", "d", "e", "q"]:
        return choice.lower()
    else:
        print(choice," is not a valid option. Please, try again")
        return None
    
def main_loop():
    
    load_mail_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        elif choice == "q":
            print("Exiting...")
            break
        elif choice == "s":
            show_mails()
        elif choice == "n":
            create_mail()
        elif choice == "e":
            input_ = ("Which item do you want to edit? (Press "
                      "q to go back to the menu) ")
            which = input(input_)
            if which.lower() == "q":
                print()
                continue
            edit_mail(which)
        elif choice == "d":
            input_ = ("Which item do you want to delete? (Press "
                      "q to go back to the menu) ")
            which = input(input_)
            if which.lower() == "q":
                print()
                continue
            delete_mail(which)
            
    save_mail_list()            
  
if __name__ == '__main__':
    main_loop()