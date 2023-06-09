# OOP
class Person:
    pass

person1 = Person()
person1.firstName = 'Eben'
person1.lastName = 'Badu'
person1.fullName = f'{person1.firstName} {person1.lastName}'
print(person1.fullName)

# Init Method

class Person:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def full_name(self):
        return f'{self.first_name} {self.last_name}'  
    def initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'  
    def email(self):
        return f'{self.first_name[0]}{self.last_name}{self.phone_number[1:3]}@gmail.com'.lower()
    
Person1 = Person('Ebenezer', 'Egyam', '0249910382') 
print(Person1.full_name())
print(Person1.initials())
print(Person1.email())

# Baking

class BakingPan:
    unit_price = 5
    expirie = 2
    def __init__(self, flour, sugar, special_ingredient):
        self.flour = flour
        self.sugar = sugar
        self.special_ingredient = special_ingredient

    def bread_name(self):
        return f'{self.flour} {self.special_ingredient} bread'
    def cost(self, quantity):
        return f'Total Cost: {self.unit_price*quantity}'
    def expiry_date(self, year):
        return f'Expiry Date: {self.expirie + year}'
    
bread1 = BakingPan('Soft', '20', 'wheat')    
print(bread1.bread_name())
print(bread1.cost(7))
print(bread1.expiry_date(2023))


# Student MIS web

class Person:
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def email(self):
        return f'{self.first_name[0]}{self.last_name}{self.phone_number[7:10]}@st.ug.edu.gh'.lower()
    def initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'
    
# Inheritance. Add and drop courses
class Student(Person):
    def __init__(self, first_name, last_name, age, phone_number, hall, courses = None):
        super().__init__(first_name, last_name, age, phone_number)
        self.hall = hall
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_courses(self, course_title):
        if course_title not in self.courses:
            self.courses.append(course_title)
    def drop_courses(self, course_title):
        if course_title in self.courses:
            self.courses.remove(course_title)

student1 = Student('Ebenezer','Egyam', 20, '0249910382', 'Legon main')
student1.add_courses('Rheology')
student1.add_courses('Thermod')
student1.add_courses('Chemical Engineering Calculation')
print(student1.courses)        

student1.drop_courses('Rheology')
print(student1.courses)

# Conditional statement

voting_age = 18
Age = int(input('Enter your age: '))
if Age >= voting_age:
    print('You qualify to vote')
else:
    print('You do not qualify to vote. 18+')


# MIS LOGIN
from getpass import getpass
Student_ID = int(input('Enter your ID: '))
Pin = getpass('Enter your Pin')
print('Your ID is',Student_ID, 'and your Pin is', Pin)

# string
School = 'University of Ghana'
list = School.split(' ')
print(list)
print(len(list))


# Assignment operator

Total = 0
item_price = 10
Total += item_price
quantity = int(input('Quantity: '))
Total *= quantity
print(Total)

# Loop
Fruits = ['Apple', 'Mango', 'Orange', 'Pawpaw', 'Pineapple']

for fruit in Fruits:
    print(fruit)
    if fruit == 'Pawpaw':
        break


names = ['ken' , 'ama', 'kwame']
scores = [67, 99, 100]
for name, score in zip(names, scores):
    print(f'{name} scored {score}')

for x in range(2, 13, 2):
    print(x)

# Sum of numbers in a list
numbers = [1,2,3,4,5,6]
Total = 0
for x in numbers:
    Total += x
    print(Total)


# Functions
def Addition(x, y):
    z = x + y
    return z
Addition(3, 4)

# Args and Kwargs
def addition(*args):
    total = 0
    for x in args:
        total += x
    print(f'Sum: {total}')
addition(1,2,3,4,5,6)    


def myself(name, age):
    return f'My name is {name} and I am {age} years old'
print(myself(age = 20, name='Eben'))

# QR Code Generator
# Simple

import PySimpleGUI as pg
import qrcode 

layout = [
    [pg.Input(key = 'input_key')],
    [pg.Button('Create', key = 'Button_key')],
    [pg.Image('', key = 'image_key')]
]

window = pg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    input = values['input_key']
    if event == 'Button_key':
        image = qrcode.make(input)
        image.save('qrco.png')
        window['image_key'].update('qrco.png')    

window.close()        

# Complex
pg.theme_background_color('#576CBC')
layout = [
    [pg.Input(key = 'input', font = ('Arial', 12))],
    [pg.Text('Fill Color', font = ('Arial', 12), background_color = '#576CBC'),
     pg.Input(key = 'fill_color', default_text='Black', size = 5, font = ('Arial', 12)),
     pg.Text('Back Color', font = ('Arial', 12), background_color = '#576CBC'),
     pg.Input(key = 'back_color', default_text='white', size = 5, font = ('Arial', 12))],
    [pg.Button('Create', key = 'button', font = ('Arial', 12), button_color = '#001D6E')],
    [pg.Image('', key = 'image')]
]

window = pg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    input = values['input']
    Fill_color = values['fill_color']
    Back_color = values['back_color']
    if event == 'button':
        qr = qrcode.QRCode(box_size=13, border=2)
        qr.add_data(input)
        image = qr.make_image(fill_color = Fill_color, back_color = Back_color )
        image.save('qrcd.png')
        window['image'].update('qrcd.png')
window.close()

# Speech to text
import PySimpleGUI as pg
import pyttsx3
pg.theme_background_color ('#867070')
layout  = [
    [pg.Input(key='input_key', font=('Arial', 12)), 
     pg.Button('Speak', key = 'Speak_button', font=('Arial', 12), button_color='#00235B')],
    [pg.Text('Select Voice Type', font=('Arial', 12), background_color='#867070'), 
     pg.Radio('Male','Gender', key = 'Male_voice', default=True, font=('Arial', 12), background_color='#867070'),
     pg.Radio('Female', 'Gender', key = 'Female_voice', font=('Arial', 12), background_color='#867070')],
    [pg.Text('Speech rate', font=('Arial', 12),background_color = '#867070'),
     pg.Input(key='Rate', default_text=150, size=4, font=('Arial', 12))],
    [pg.Text('Volume', font=('Arial', 12),background_color='#867070'),
     pg.Slider(key = 'Volume', default_value=5, orientation='horizontal', size=(15,15), font=('Arial', 12), range = (0, 10), background_color='#867070')]  
]


window = pg.Window('Text To Speech App', layout)
while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break

    speaker = pyttsx3.init()
    input = values['input_key']
    Rate = values['Rate']
    Volume = values['Volume']/10

    if event == 'Speak_button':
        if values['Male_voice']== True:
           voices = speaker.getProperty('voices')
           speaker.setProperty('voice', voices[0].id)
           speaker.setProperty('rate', Rate)
           speaker.setProperty('volume', Volume)
           speaker.say(input)
           speaker.runAndWait()
        if values['Female_voice']== True:
           voices = speaker.getProperty('voices')
           speaker.setProperty('voice', voices[1].id)
           speaker.setProperty('rate', Rate)
           speaker.setProperty('volume', Volume)
           speaker.say(input)
           speaker.runAndWait()


# using class    
import pyttsx3
class Speech_eng:
    def Voice_type(input_type, voice_type, speed_rate, volume):
        speaker = pyttsx3.init()
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[voice_type].id)
        speaker.setProperty('rate', speed_rate)
        speaker.setProperty('volume', volume)
        speaker.say(input_type)
        speaker.runAndWait()

import PySimpleGUI as sg


sg.theme_background_color('#635985')
layout = [
   [sg.Multiline(key = 'Text_input', font=('Open Sans', 12), size=(40, 2)),
     sg.Button('Speak', key = 'Speak_button', font=('Open Sans', 12), button_color='#00235B')],
   [sg.Text('Select Voice Type',font=('Open Sans', 11), background_color= '#635985'), 
    sg.Radio('Male','Gender', key = 'Male_voice', default=True, font=('Open Sans', 11), background_color= '#635985'), 
    sg.Radio('Female', 'Gender', key = 'Female_voice', font=('Open Sans', 11), background_color= '#635985')],
   [sg.Text('Speech rate', font=('Open Sans', 11), background_color= '#635985'), sg.Input(key='speed_rate', size=3, default_text='150', font=('Open Sans', 11))],
   [sg.Text('Volume level', font=('Open Sans', 11),background_color= '#635985'), 
    sg.Slider(key = 'volume', range=(0, 10), orientation='horizontal', size=(10, 15), default_value= 5, font=('Open Sans', 11), background_color= '#635985')]
]   

window = sg.Window('Text to Speach App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    input = values['Text_input']
    speed_r = int(values['speed_rate']) 
    speech_vol = int(values['volume']) * 0.1

    if event =='Speak_button':
        if values['Male_voice'] == True:
            Speech_eng.Voice_type(input_type=input,voice_type=0,speed_rate=speed_r,volume=speech_vol)
        
        if values['Female_voice'] == True:
            Speech_eng.Voice_type(input_type=input,voice_type=1,speed_rate=speed_r,volume=speech_vol )
        
window.close()  
   

