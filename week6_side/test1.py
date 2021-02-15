import sqlite3
import os
conn = sqlite3.connect(r'C:\Users\kritphol\Desktop\kraen\work\chadchalidh(Python)\student.db')
c = conn.cursor()

def menu():
    global choose
    print('---ระบบทะเบียนนักเรียน---\nadd info student[a]\nshow info[s]\nEdit info student[e]\ndelete info student[d]\nexti program[x]')
    choose = input('choose select : ')

def add():
    s_name = input('name and sername: ')
    s_email = input('Email: ')
    s_gender = input('gender: ')
    s_old = input('age: ')
    s_year = input('year: ')
    c.execute("""INSERT INTO students(name,email,gender,old,year)VALUES (?,?,?,?,?)""",
         (s_name,s_email,s_gender,s_old,s_year))
    conn.commit()
    print('add info succress!!')

def show():
    print('{0: <10}{1: <20}{2: <20}{3: <15}{4: <15}{5: <1}'.format('No.','name','Email','gender','age','year'))
    c.execute('''SELECT * FROM students''')
    result = c.fetchall()
    for x in result:
        print('{0: <7}{1: <17}{2: <18}{3: <15}{4: <15}{5: <1}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))

def edit():
    line = input('row Edit?: ')
    nname = input('name are edit?: ')
    nemail = input('Email are edit?: ')
    ngender = input('gender are edit?: ')
    nold = input('age are edit?: ')
    nyear = input('year are edit?: ')
    data = (nname,nemail,ngender,nold,nyear,line)
    c.execute('''UPDATE students SET name=?,email=?,gender=?,old=?,year=? WHERE id= ?''',data)
    print('edited!!')
    conn.commit()

def delete():
    delete = input('no.your need delete : ')
    c.execute('''DELETE FROM students WHERE id = ?''',delete)
    conn.commit()

while True:
    menu()
    if choose =='a':
        add()
    elif choose =='s':
        show()
    elif choose =='e':
        edit()
    elif choose =='d':
        delete()
    elif choose =='x':
        exitt = input('you are Exit (y/n) : ')
        if exitt == 'y':
            conn.close()
            print('thx for using')
            break
        elif exitt == 'n':
            continue