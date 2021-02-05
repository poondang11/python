import os
choice = 0
filename = ''

def menu():
    global choice
    print('menu\n 1.open calculator\n 2.open notepad\n 3.cmd\n 4.Exit')
    choice = input('select menu:')

def opennotepad():
    filename = 'c:\\windows\\SysWOW64\\notepad.exe'
    print('Memorandum writing %s'%filename)
    os.system(filename)

def opencalculator():
    filename = 'c:\\windows\\SysWOW64\\calc.exe'
    print('calculate Number %s'%filename)
    os.system(filename) 


while True:
    menu()
    if choice == '1':
        opencalculator()
    elif choice =='2':
        opennotepad()
    else:
        break  
