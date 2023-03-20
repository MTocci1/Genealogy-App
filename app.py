# Mason (Alex) Tocci
# Prof. Johnson
# Intro to Programming
# Project 4: Genealogy
# 10 December 2021


from graphics import *
from Person import *

person_dict = {}

# create window for input
win = GraphWin("Genealogy Input", 480, 270)
win.setCoords(0.0, 0.0, 16.0, 9.0)

# create window for output
win2 = GraphWin("Genealogy Output", 960, 540)
win2.setCoords(0.0, 0.0, 32.0, 18.0)

output = Text(Point(16.0, 14.0), "")
output.draw(win2)

# tell user how to enter
label = Text(Point(8.0, 8.0), "Click to enter")
label.draw(win)

#hidden text for display
title = Text(Point(16.0, 17.0), "")
title.draw(win2)

g_text = Text(Point(3.0, 16.0), "")
g_text.draw(win2)

g_text_list = [
    Text(Point(5.0, 14.0), ""),
    Text(Point(12.0, 14.0), ""),
    Text(Point(19.0, 14.0), ""),
    Text(Point(26.0, 14.0), ""),
    ]
for i in g_text_list:
    i.draw(win2)

p_text = Text(Point(3.0, 11.0), "")
p_text.draw(win2)

p_text_list = [
    Text(Point(5.0, 9.0), ""),
    Text(Point(12.0, 9.0), ""),
    ]
for i in p_text_list:
    i.draw(win2)

s_text = Text(Point(3.0, 6.0), "")
s_text.draw(win2)

s_text_list = [
    Text(Point(5.0, 4.0), ""),
    Text(Point(12.0, 4.0), ""),
    Text(Point(19.0, 4.0), ""),
    Text(Point(26.0, 4.0), ""),
    ]
for i in s_text_list:
    i.draw(win2)
    

text = Text(Point(8.0, 7.0), "Do you want to [L]oad an existing genealogy \
or start a [N]ew one? ")
text.draw(win)

inputText = Entry(Point(8.0, 5.0), 18)
inputText.setText("")
inputText.draw(win)


# seperate functions to add/remove names and birthdays to the correct list
def store_person(owner, name, bday, relationship):
    new_object = Person(name, bday, relationship)
    person_dict[name] = new_object # add person to dictionary
    
def remove_person(owner, name):
    # make sure the person exists
    if name in person_dict:
        output.setText(person_dict[name].get_rel() + " " + name + " \
(" + person_dict[name].get_birthday() + ") has been removed \
from "+ owner + "'s genealogy.")
        del person_dict[name]
    else:
        output.setText(name +" could not be removed because they do not exist.")

def add_person(owner):
    # try and except for if the user does put format the input correctly
    try:
        inputText.setText("")
        text.setText("Do you want to add a [P]arent, [S]ibling, or \
[G]randparent? ")
        win.getMouse()
        a_who = str(inputText.getText())
        if a_who.upper() == "P":
            relationship = "parent"
            inputText.setText("")
            text.setText("Enter the new person's name and \
birth date (separated by comma)")
            win.getMouse()
            name, bday = str(inputText.getText()).split(", ")
            output.setText("Parent "+ name+ " (" + bday + ") has been added \
to "+ owner + "'s genealogy.")
            store_person(owner,name,bday,relationship)
            return edit_or_view(owner)
        elif a_who.upper() == "S":
            relationship = "sibling"
            inputText.setText("")
            text.setText("Enter the new person's name and \
birth date (separated by comma)")
            win.getMouse()
            name, bday = str(inputText.getText()).split(", ")
            output.setText("Sibling "+ name+ " (" + bday + ") has been added \
to "+ owner + "'s genealogy.")
            store_person(owner, name, bday, relationship)
            return edit_or_view(owner)
        elif a_who.upper() == "G":
            relationship = "grandparent"
            inputText.setText("")
            text.setText("Enter the new person's name and \
birth date (separated by comma)")
            win.getMouse()
            name, bday = str(inputText.getText()).split(", ")
            output.setText("Sibling "+ name+ " (" + bday + ") has been added \
to "+ owner + "'s genealogy.")
            store_person(owner, name, bday, relationship)
            return edit_or_view(owner)
        else:
            output.setText("Enter a valid input.")
            return add_person(owner)
    except ValueError:
        output.setText("Could not be added to genealogy. \nMake sure to put a \
space after the comma.")
        add_person(owner)

def remove_who(owner):
    inputText.setText("")
    text.setText("Who do you want to remove? ")
    win.getMouse()
    name = str(inputText.getText())
    remove_person(owner, name)
    return edit_or_view(owner)

def lookup_name(owner, name):
    #make sure person exists
    if name in person_dict:
        output.setText(owner +"'s "+ person_dict[name].get_rel() +" "+ name+ " \
was born "+ person_dict[name].get_birthday() +".")
    else:
        output.setText(name+ " does not exist in "+ owner +"'s genealogy")
    return edit_or_view(owner)

def test_bday(owner, birthday):
    # search for birthday
    bday = False
    for k, v in person_dict.items():
        if v.get_birthday() == birthday:
            output.setText(owner +"'s "+ v.get_rel() +", "+ k +", was \
born "+ birthday +".")
            bday = True
    return bday

def lookup_bday(owner, birthday):
    # print message when a birthday is not found
    bday = test_bday(owner, birthday)
    if bday == False:
        output.setText("The birthday ("+ birthday +") does not exist \
in "+ owner +"'s genealogy")
    return edit_or_view(owner)
        
def name_or_bday(owner):
    inputText.setText("")
    text.setText("Do you want to look up by [N]ame or [B]irthday? ")
    win.getMouse()
    lookup2 = str(inputText.getText())
    if lookup2.upper() == "N":
        inputText.setText("")
        text.setText("Who do you want to look up? ")
        win.getMouse()
        name = str(inputText.getText())
        lookup_name(owner, name)
    elif lookup2.upper() == "B":
        inputText.setText("")
        text.setText("What is the birthday of this person? ")
        win.getMouse()
        birthday = str(inputText.getText())
        lookup_bday(owner, birthday)
    else:
        output.setText("Enter a valid input.")
        return name_or_bday(owner)

def display_grandparent(text_obj, person):
    text_obj.setText(person.get_name() + "\n" + person.get_birthday())

def display_parent(text_obj, person):
    text_obj.setText(person.get_name() + "\n" + person.get_birthday())
    
def display_sibling(text_obj, person):
    text_obj.setText(person.get_name() + "\n" + person.get_birthday())

def display(owner):
    inputText.setText("")
    label.setText("")
    text.setText("Click to continue")
    output.setText("")
    title.setText("Genealogy for "+ owner +":")
    g_text.setText("Grandparents:")
    p_text.setText("Parents:")
    s_text.setText("Siblings:")
    
    # display names in the correct box
    i = 0
    try: # try and except in case the user enters too many people
        for k, v in person_dict.items():
                if v.get_rel() == "grandparent":
                    display_grandparent(g_text_list[i], v)
                    i += 1
    except IndexError:
        pass
    
    i = 0
    try:
        for k, v in person_dict.items():
                if v.get_rel() == "parent":
                    display_parent(p_text_list[i], v)
                    i += 1
    except IndexError:
        pass
    
    i = 0
    try:
        for k, v in person_dict.items():
                if v.get_rel() == "sibling":
                    display_parent(s_text_list[i], v)
                    i += 1
    except IndexError:
        pass
    
    
    # create all the rectangles
    g1 = Rectangle(Point(2,12), Point(8,15)).draw(win2)
    g2 = Rectangle(Point(9,12), Point(15,15)).draw(win2)
    g3 = Rectangle(Point(16,12), Point(22,15)).draw(win2)
    g4 = Rectangle(Point(23,12), Point(29,15)).draw(win2)
    p1 = Rectangle(Point(2,10), Point(8,7)).draw(win2)
    p2 = Rectangle(Point(9,10), Point(15,7)).draw(win2)
    s1 = Rectangle(Point(2,5), Point(8,2)).draw(win2)
    s2 = Rectangle(Point(9,5), Point(15,2)).draw(win2)
    s3 = Rectangle(Point(16,5), Point(22,2)).draw(win2)
    s4 = Rectangle(Point(23,5), Point(29,2)).draw(win2)

    win.getMouse()

    # clear the screen
    g1.undraw()
    g2.undraw()
    g3.undraw()
    g4.undraw()
    p1.undraw()
    p2.undraw()
    s1.undraw()
    s2.undraw()
    s3.undraw()
    s4.undraw()

    for i in g_text_list:
        i.setText("")
    for i in p_text_list:
        i.setText("")
    for i in s_text_list:
        i.setText("")
        
    title.setText("")
    g_text.setText("")
    p_text.setText("")
    s_text.setText("")

    edit_or_view(owner)
    
# created new functions to keep the code neat
# didn't want if statements under if statements
def one_all(owner):
    inputText.setText("")
    text.setText("Do you want to [L]ookup one person or [D]isplay \
everyone? ")
    win.getMouse()
    lookup = str(inputText.getText())
    if lookup.upper() == "L":
        name_or_bday(owner)
    elif lookup.upper() == "D":
        display(owner)
    else:
        output.setText("Enter a valid input.")
        return one_all(owner)
        
def add_remove(owner):
    inputText.setText("")
    text.setText("Do you want to [A]dd or [R]emove a person? ")
    win.getMouse()
    add = str(inputText.getText())
    if add.upper() == "A":
        add_person(owner)  
    elif add.upper() == "R":
        remove_who(owner)
    else:
        output.setText("Enter a valid input.")
        return add_remove(owner)
        
def edit_or_view(owner):
    inputText.setText("")
    text.setText("Would you like to [E]dit, [Q]uery, or [S]ave your genealog\
y? ")
    win.getMouse()
    edit = str(inputText.getText())
    if edit.upper() == "E":
        add_remove(owner)
    elif edit.upper() == "Q":
        one_all(owner)
    elif edit.upper() == "S":
        save_file(owner)
    else:
        output.setText("Enter a valid input.")
        return edit_or_view(owner)
        

def save_file(owner):
    output.setText("Genealogy saved to file 'genealogy.txt'")
    file = open("genealogy.txt", "w")

    # write owners name on it's own line so it's easier to load
    file.write(str(person_dict[owner].get_name()))

    # save all data on one line
    file.write("\n")
    for k, v in person_dict.items():
        file.write(str(k) + ","+ str(v.get_birthday()) + "," + str(v.get_rel()) + ":")
    file.close()
    edit_or_view(owner)

def load_file():
    try: # make sure user has a file to load
        file = open("genealogy.txt","r")
        line = file.readline().strip()
        owner = str(line)
        line = file.readline()
        while line:
            try:
                data = line.split(":")
                for i in range(len(data)):
                    Sdata = data[i].split(",")
                    name, bday, relationship = Sdata[0], Sdata[1], Sdata[2]
                    store_person(owner, name, bday, relationship)
            except IndexError:
                break
        file.close()
        edit_or_view(owner)
    except FileNotFoundError:
        output.setText("File not found. Create a new file.")
        main()
    
def main():
    inputText.setText("")
    win.getMouse()
    l_or_n = str(inputText.getText())
    if l_or_n.upper() == "L":
        load_file()
    elif l_or_n.upper() == "N":
        file = open("genealogy.txt","w")
        file.close()
        inputText.setText("")
        relationship = "owner"
        text.setText("Who is the owner of this genealogy? ")
        win.getMouse()
        name = str(inputText.getText())
        owner = name
        text.setText("What is the owner's birthday? ")
        inputText.setText("")
        win.getMouse()
        bday = str(inputText.getText())
        store_person(owner, name, bday, relationship)
        edit_or_view(owner)
    else:
        output.setText("Enter a valid input.")
        return main()
main()
