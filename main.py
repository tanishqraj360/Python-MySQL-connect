import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='sudo')
mycursor=con.cursor()
Unique_Id=''
mycursor.execute('CREATE DATABASE IF NOT EXISTS covid')
mycursor.execute('USE covid')

def plasma():
    mycursor.execute("CREATE TABLE IF NOT EXISTS plasma(Unique_Id int not null primary key,Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    ui=input('Enter a Unique Id -->')
    nb=input('Enter Your Name -->')
    ad=input('Enter Your Address -->')
    ph=input('Enter Your Phone no -->')
    id=input('Enter Your Email id -->')
    age=input('Enter Your Age-->')
    data=(ui,nb,ad,ph,id,age)
    p='insert into plasma value(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(p,data)
    con.commit()
    print('>===================================================================')
    print('Thank You For Your Donation!')
    input('Press ENTER to continue...')

def bed():
    mycursor.execute("CREATE TABLE IF NOT EXISTS bed(Unique_Id int not null primary key,Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    ui=input('Enter a Unique Id -->')
    nb=input('Enter Your Name -->')
    ad=input('Enter Your Address -->')
    ph=input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age=input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    b='insert into bed values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(b,data)
    con.commit()
    print('>===================================================================')
    print('Thank You For Your Donation!')
    input('Press ENTER to continue...')

def oxygen():
    mycursor.execute("CREATE TABLE IF NOT EXISTS oxygen(Unique_Id int not null primary key,Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    ui=input('Enter a Unique Id -->')
    nb = input('Enter Your Name -->')
    ad = input('Enter Your Address -->')
    ph = input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age = input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    o = 'insert into oxygen values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(o, data)
    con.commit()
    print('>===================================================================')
    print('Thank You For Your Donation!')
    input('Press ENTER to continue...')

def medicine():
    mycursor.execute("CREATE TABLE IF NOT EXISTS plasma(Unique_Id int not null primary key,Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    ui=input('Enter a Unique_Id -->')
    nb = input('Enter Your Name -->')
    ad = input('Enter Your Address -->')
    ph = input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age = input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    m = 'insert into medicine values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(m, data)
    con.commit()
    print('>===================================================================')
    print('Thank You For Your Donation!')
    input('Press ENTER to continue...')

def aplasma():
    mycursor.execute("CREATE TABLE IF NOT EXISTS aplasma(Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    nb = input('Enter Your Name -->')
    ad = input('Enter Your Address -->')
    ph = input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age = input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    ap = 'insert into aplasma value(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(ap, data)
    con.commit()
    print('These are the Plasma Donators')
    a='select Unique_Id,Address from plasma'
    c=con.cursor()
    c.execute(a)
    myresulta=c.fetchall()
    if myresulta:
        for i in myresulta:
            print("Unique Id -->", i[0])
            print("Address -->", i[1])
    else:
        print('Record Not Found.')
    Unique_Id=input('Enter the Unique Id from Your Nearest Address: ')
    g = 'select Name,Phone_No,Email_Id from plasma where Unique_Id=%s'
    c = con.cursor()
    c.execute(g,(Unique_Id,))
    myresult=c.fetchall()
    if myresult:
        for m in myresult:
            print("Name -->", m[0])
            print("Phone No -->", m[1])
            print("Email -->", m[2])
            print('Good Luck!')
            input('Press ENTER to continue...')
    else:
        print('Record Not Found')
        input('Press ENTER to continue...')

def abed():
    mycursor.execute("CREATE TABLE IF NOT EXISTS abed(Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    nb = input('Enter Your Name -->')
    ad = input('Enter Your Address -->')
    ph = input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age = input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    b = 'insert into abed values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(b, data)
    con.commit()
    print('These are the Bed Donators')
    a = 'select Unique_Id,Address from bed'
    c = con.cursor()
    c.execute(a)
    myresulta = c.fetchall()
    if myresulta:
        for i in myresulta:
            print("Unique Id -->", i[0])
            print("Address -->", i[1])
    else:
        print('Record Not Found.')
    Unique_Id = input('Enter the Unique Id from Your Nearest Address: ')
    g = 'select Name,Phone_No,Email_Id from bed where Unique_Id=%s'
    c = con.cursor()
    c.execute(g, (Unique_Id,))
    myresult = c.fetchall()
    if myresult:
        for k in myresult:
            print("Name -->", k[0])
            print("Phone No -->", k[1])
            print("Email -->", k[2])
            print('Good Luck!')
            input('Press ENTER to continue...')
    else:
        print('Record Not Found')
        input('Press ENTER to continue...')

def aoxygen():
    mycursor.execute("CREATE TABLE IF NOT EXISTS aoxygen(Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    nb = input('Enter Your Name -->')
    ad = input('Enter Your Address -->')
    ph = input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age = input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    b = 'insert into aoxygen values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(b, data)
    con.commit()
    print('These are the Plasma Donators')
    a = 'select Unique_Id,Address from oxygen'
    c = con.cursor()
    c.execute(a)
    myresulta = c.fetchall()
    if myresulta:
        for i in myresulta:
            print("Unique Id -->", i[0])
            print("Address -->", i[1])
    else:
        print('Record Not Found.')
        Unique_Id = input('Enter the Unique Id from Your Nearest Address: ')
        g = 'select Name,Phone_No,Email_Id from oxygen where Unique_Id=%s'
        c = con.cursor()
        c.execute(g, (Unique_Id,))
        myresult = c.fetchall()
        if myresult:
            for k in myresult:
                print("Name -->", k[0])
                print("Phone No -->", k[1])
                print("Email -->", k[2])
                print('Good Luck!')
                input('Press ENTER to continue...')
        else:
            print('Record Not Found')
            input('Press ENTER to continue...')

def amedicine():
    mycursor.execute("CREATE TABLE IF NOT EXISTS amedidicne(Name VARCHAR(30), Address VARCHAR(50),Phone_No VARCHAR(10), Email_Id VARCHAR(50),Age VARCHAR(2))")
    nb = input('Enter Your Name -->')
    ad = input('Enter Your Address -->')
    ph = input('Enter Your Phone no-->')
    id = input('Enter Your Email id: ')
    age = input('Enter Your Age -->')
    data = (nb, ad, ph, id, age)
    b = 'insert into amedicine values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(b, data)
    con.commit()
    print('These are the Plasma Donators')
    a = 'select Unique_Id,Address from medicine'
    c = con.cursor()
    c.execute(a)
    myresulta = c.fetchall()
    if myresulta:
        for i in myresulta:
            print("Unique Id -->", i[0])
            print("Address -->", i[1])
    else:
        print('Record Not Found.')
    Unique_Id = input('Enter the Unique Id from Your Nearest Address: ')
    g = 'select Name,Phone_No,Email_Id from medicine where Unique_Id=%s'
    c = con.cursor()
    c.execute(g, (Unique_Id,))
    myresult = c.fetchall()
    if myresult:
        for k in myresult:
            print("Name -->", k)
            print("Phone No -->", k)
            print("Email -->", k)
            print('Good Luck!')
            input('Press ENTER to continue...')
    else:
        print('Record Not Found')
        input('Press ENTER to continue...')

######################################################################
###################################################

while(True):
    print("""
    COVID CARE
    1. DONATE RESOURCE
    2. RECIEVE RESOURCE
    3. EXIT
    """)
    choice1=int(input('Enter Your Choice: '))
    if (choice1==1):
        print('''
        COVID CARE
        1. PLASMA
        2. BED
        3. OXYGEN
        4. MEDICINE
        5. EXIT
        ''')
        choice=int(input('Enter Your Choice: '))
        if (choice==1):
            plasma()
        elif (choice==2):
            bed()
        elif (choice==3):
            oxygen()
        elif (choice==4):
            medicine()
        elif (choice==5):
            break
        else:
            print('Invalid input. Please try again')
    elif (choice1==2):
        print('''
        COVID CARE
        1. PLASMA
        2. BED
        3. OXYGEN
        4. MEDICINE
        5. EXIT
        ''')
        choice=int(input('Enter Your Choice: '))
        if (choice==1):
            aplasma()
        elif (choice==2):
            abed()
        elif (choice==3):
            aoxygen()
        elif (choice==4):
            amedicine()
        elif (choice==5):
            break
        else:
            print('Invalid input. Please try again')
    elif choice1==3:
        break
    else:
        print('Invalid Input. Try Again')