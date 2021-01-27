import mysql.connector
from datetime import date, timedelta,datetime
from tkinter import *
from tkcalendar import *
import tkinter.messagebox
import sys


class test2:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="password",
            database="sys"
        )
        self.mycursor = self.mydb.cursor()

    def menu(self):
        t = Tk()
        t.title("Passenger info")
        t.geometry("135x220")

        Label(t, text="Main Menu", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W,
                                                                      pady=12)

        signupButton = Button(t, text="Register", command=lambda :[t.destroy(),self.signup()], width=15)
        signupButton.grid(row=1, pady=7)
        signinButton = Button(t, text="Log In", command=lambda :[t.destroy(),self.login()], width=15)
        signinButton.grid(row=2, pady=7)
        tInfoButton = Button(t, text="Ticket Info", command=lambda :[t.destroy(),self.ticket_info()], width=15)
        tInfoButton.grid(row=3, pady=7)
        chatbotButton = Button(t, text="Chatbot", width=15)
        chatbotButton.grid(row=4, padx=10, pady=7)

        t.mainloop()


    def signup(self):
        root = Tk()
        root.title('Railway Reservation System')
        root.geometry('320x220')

        r = Frame(root)
        r.grid(row=0, column=0)

        gender = StringVar()
        gender.set("M")

        def register():
            pass1 = password1Entry.get()
            name = nameEntry.get()
            age_0 = ageEntry.get()
            sex_0 = gender.get()
            no = noEntry.get()
            user = userEntry.get()

            full_name = name
            username = user
            password = pass1
            contact = no
            age = int(age_0)
            sex = sex_0
            self.mycursor.execute("Select user_id from user")
            user_ids = self.mycursor.fetchall()
            l = len(user_ids)
            self.mycursor.execute(
                "INSERT INTO `sys`.`user` (`user_id`, `full_name`, `password`, `contact`, `age`, `sex`, `username`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
                    user_ids[l - 1][0] + 1, full_name, password, contact, age, sex, username))
            self.mydb.commit()
            tkinter.messagebox.showinfo("Registration Message", "Registration Successful")
            root.destroy()
            self.login()

        Label(r, text="New User Registration", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4,
                                                                                  sticky=E + W)
        Label(r, text="Full Name").grid(row=1, column=0, sticky=W)
        Label(r, text="Age").grid(row=2, column=0, sticky=W)
        Label(r, text="Sex").grid(row=3, column=0, sticky=W)
        Label(r, text="Contact No.").grid(row=4, column=0, sticky=W)
        Label(r, text="Username").grid(row=5, column=0, sticky=W)
        Label(r, text="Password").grid(row=6, column=0, sticky=W)
        nameEntry = Entry(r, width=30)
        nameEntry.grid(row=1, column=1, sticky=E)
        ageEntry = Entry(r, width=30)
        ageEntry.grid(row=2, column=1, sticky=E)
        genderEntry = OptionMenu(r, gender, "M", "F")
        genderEntry.grid(row=3, column=1)
        noEntry = Entry(r, width=30)
        noEntry.grid(row=4, column=1, sticky=E)
        userEntry = Entry(r, width=30)
        userEntry.grid(row=5, column=1, sticky=E)
        password1Entry = Entry(r, width=30 ,show="*")
        password1Entry.grid(row=6, column=1, sticky=E)
        AlreadyRegisteredButton = Button(r, text="Click here to login", command=self.login).grid(row=9, column=0, sticky=W, padx=12)
        RegisterButton = Button(r, text="Register", width=15, command=register).grid(row=9, column=1, sticky=E, padx=2)
        root.mainloop()


    def login(self):
        root = Tk()
        root.title('Railway Reservation System')
        root.geometry('320x220')
        l = Frame(root)
        l.grid(row=0, column=0)
        self.name_in=""
        self.pass_in=""
        self.flag_3=0
        def login():
            root.geometry('330x100')
            l.tkraise()
            username = usernameEntry.get()
            password = passwordEntry.get()
            if(username=="Admin" and password=="password"):
                self.insert()
                root.destroy()
                sys.exit()
            self.name_in=username
            self.pass_in=password
            self.mycursor.execute("SELECT username FROM user")
            names = self.mycursor.fetchall()
            self.mycursor.execute("Select password FROM user")
            passwords = self.mycursor.fetchall()
            flag_0 = 0
            flag_1 = 0
            for x in names:
                name_0 = ''.join(x)
                if (self.name_in == name_0):
                    flag_0 = 1
                    break
            for x in passwords:
                password_0 = ''.join(x)
                if (self.pass_in== password_0):
                    flag_1 = 1
                    break
            if (flag_0 == 1 and flag_1 == 1):
                self.mycursor.execute("SELECT full_name FROM user WHERE username='{}'".format(username))
                full_name = self.mycursor.fetchone()
                full_name = ''.join(full_name)
                tkinter.messagebox.showinfo("Welcome","Greetings! {}".format(full_name))
                self.flag_3 =1
                root.destroy()
            else:
                tkinter.messagebox.showinfo("Error", "User does not exist")
        Label(l, text="Login Page", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W)
        Label(l, text="Username").grid(row=1, column=1, padx=7)
        Label(l, text="Password").grid(row=2, column=1, padx=7)
        usernameEntry = Entry(l, width=40)
        usernameEntry.grid(row=1, column=2)
        passwordEntry = Entry(l, width=40, show='*')
        passwordEntry.grid(row=2, column=2)
        LoginButton = Button(l, text="Login", command=login)
        LoginButton.grid(row=3, column=1, columnspan=3)
        # CloseButton=Button(l,text="Close", command=lambda root=root:quit(root)).grid(row=3,column=2,columnspan=3)
        root.mainloop()
        if(self.flag_3==1):
            self.search()



    def search(self):
        self.flag_2 = 0
        self.source_in=""
        self.destination_in=""
        s = Tk()
        s.title("Railway Reservation System")
        s.geometry("460x280")
        self.dateEntry = StringVar()
        source = StringVar()
        source.set("Station")
        destination = StringVar()
        destination.set("Station")
        Label(s, text="Search Page", font=("Times New Roman", 18)).place(x=160,y=0)
        Label(s, text="Source").place(x=70,y=50)
        sourceEntry = OptionMenu(s, source, "Mumbai", "Delhi", "Chennai", "Kolkata")
        sourceEntry.place(x=125,y=45)
        sourceEntry.configure(width=8)
        def getSource():
            self.source_in = source.get()
            Label(s, text="Destination").place(x=50,y=85)
            def getDestination(value):
                self.destination_in=value
                destinationButton = Button(s, text="Confirm Destination", command=info).place(x=235,y=83)

            if (source.get() == "Mumbai"):
                destinationEntry = OptionMenu(s, destination, "Delhi", "Chennai", "Kolkata",command=getDestination)
                destinationEntry.place(x=125,y=80)
                destinationEntry.configure(width=8)
                # destinationButton = Button(s, text="Confirm Destination", command=info).grid(row=2, column=3)

            elif (source.get() == "Kolkata"):
                destinationEntry = OptionMenu(s, destination, "Delhi", "Chennai", "Mumbai",command=getDestination)
                destinationEntry.place(x=125,y=80)
                destinationEntry.configure(width=8)
                # destinationButton = Button(s, text="Confirm Destination", command=info).grid(row=2, column=3)

            elif (source.get() == "Chennai"):
                destinationEntry = OptionMenu(s, destination, "Delhi", "Mumbai", "Kolkata",command=getDestination)
                destinationEntry.place(x=125,y=80)
                destinationEntry.configure(width=8)
                # destinationButton = Button(s, text="Confirm Destination", command=info).grid(row=2, column=3)

            elif (source.get() == "Delhi"):
                destinationEntry = OptionMenu(s, destination, "Mumbai", "Chennai", "Kolkata",command=getDestination)
                destinationEntry.place(x=125,y=80)
                destinationEntry.configure(width=8)


        sourceButton = Button(s, text="Confirm Source", command=getSource).place(x=235,y=48)

        def info():
            self.mycursor.execute("Select source FROM train")
            sources = self.mycursor.fetchall()
            self.mycursor.execute("Select destination FROM train")
            destinations = self.mycursor.fetchall()
            flag_0 = 0
            flag_1 = 0
            source_0 = ""
            destination_0 =""
            str=""
            print(self.source_in)
            print(self.destination_in)
            for x in sources:
                source_0 = ''.join(x)
                if (self.source_in == source_0):
                    flag_0 = 1
                    break
            for x in destinations:
                destination_0 = ''.join(x)
                if (self.destination_in == destination_0):
                    flag_1 = 1
                    break
            if (flag_0 == 1 and flag_1 == 1):
                self.flag_2=1
                self.mycursor.execute(
                    "Select train_id,train_name from train WHERE source='{}' and destination='{}'".format(self.source_in,self.destination_in))
                trains = self.mycursor.fetchall()
                for i in trains:
                    self.train_id = i[0]
                    self.train_name = i[1]
                    str="Train {} travels according to given details,id {}".format(i[1], i[0])
            else:
                str="No trains available"
            print(str)
            Label(s, text=str).place(x=125,y=120)
            Label(s, text="Enter date to check availability of seats").place(x=10,y=150)
            self.dateEntry = DateEntry(s, width=15)
            self.dateEntry.place(x=235,y=150)
            dateButton = Button(s, text="Confirm Date", command=cal_func).place(x=365,y=148)

        def cal_func():
            str=""
            date_str = self.dateEntry.get()
            date_str = date_str.replace("/", "-")
            date_str = date_str.replace("20", "2020")
            date_str=datetime.strptime(date_str, '%m-%d-%Y').strftime('%Y-%m-%d')
            self.date_in = date_str
            self.mycursor.execute(
                "Select * from seats WHERE date=(SELECT CAST('{}' AS DATE)) and source='{}' and destination='{}'".format(
                    self.date_in, self.source_in, self.destination_in))
            available_trains = self.mycursor.fetchall()

            if (available_trains):
                for i in available_trains:
                    str="2 tier seats: {},3 tier seats: {},sleeper seats: {},general seats: {}".format(i[0],i[1],i[2],i[3])
            else:
                tkinter.messagebox.showinfo("Unavailable","No trains available for selected date")
            seats_info = Label(text=str).place(x=100,y=180)
            bookingButton = Button(s, text="Proceed To Book", command=lambda :[s.destroy(),self.availability_booking()]).place(x=170,y=240)
        s.mainloop()

    def availability_booking(self):
        b = Tk()
        b.title("Railway Reservation System")
        b.geometry('420x200')

        aukaat = StringVar()
        aukaat.set("Class")
        self.amt=0
        self.class_in=""
        self.no_passengers=0

        def class_func(value):
            if (value == "General"):
                self.class_in="general"
                amountText.configure(state='normal')
                amountText.delete(1.0, END)
                amountText.insert("end", "300")
                amountText.configure(state='disabled')
            elif (value == "SL"):
                self.class_in = "sleeper"
                amountText.configure(state='normal')
                amountText.delete(1.0, END)
                amountText.insert("end", "500")
                amountText.configure(state='disabled')
            elif (value == "3A"):
                self.class_in = "3_Tier"
                amountText.configure(state='normal')
                amountText.delete(1.0, END)
                amountText.insert("end", "700")
                amountText.configure(state='disabled')
            elif (value == "2A"):
                self.class_in = "2_Tier"
                amountText.configure(state='normal')
                amountText.delete(1.0, END)
                amountText.insert("end", "1000")
                amountText.configure(state='disabled')

        def amount():
            pNo = noEntry.get()
            self.no_passengers = int(pNo)
            amt = amountText.get(1.0, END)
            tAmt = int(pNo) * int(amt)
            self.amt=tAmt
            tAmountText.configure(state='normal')
            tAmountText.delete(1.0, END)
            tAmountText.insert("end", tAmt)
            tAmountText.configure(state='disabled')

        Label(b, text="Booking Page", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W,pady=15)
        Label(b, text="Select Class").grid(row=1, column=0)
        Label(b, text="Amount per seat").place(x=200, y=66)
        Label(b, text="Choose the no. of passengers:").grid(row=2, column=0, columnspan=2, pady=10)
        Label(b, text="Total amount").grid(row=4, column=0)

        classEntry = OptionMenu(b, aukaat, "General", "SL", "3A", "2A", command=class_func)
        classEntry.configure(width=8)
        classEntry.grid(row=1, column=1)
        amountText = Text(b, width=5, height=1)
        amountText.place(x=305, y=68)
        noEntry = Entry(b, width=7)
        noEntry.place(x=180, y=105)
        tAmountText = Text(b, width=9, height=1)
        tAmountText.grid(row=4, column=1)
        tAmountText.configure(state='disabled')

        passengerButton = Button(b, text="Confirm no. of passengers", command=amount)
        passengerButton.grid(row=2, column=2, columnspan=3, padx=80)
        def exec():
            self.mycursor.execute(
                "Select user_id FROM user where username='{}' and password='{}'".format(self.name_in, self.pass_in))
            user_id_tup = self.mycursor.fetchone()
            self.user_id = user_id_tup[0]
            self.mycursor.execute("Select book_id from books")
            if (self.mycursor.fetchall()):
                self.mycursor.execute("Select book_id from books")
                book_ids = self.mycursor.fetchall()
                l = len(book_ids)
                print(book_ids[l - 1][0])
                self.mycursor.execute(
                    "INSERT INTO `sys`.`books` (`book_id`, `book_time`, `no_ppl`, `user_id`, `train_id`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
                        book_ids[l - 1][0] + 1, str(datetime.now()), self.no_passengers, self.user_id, self.train_id))
                self.mycursor.execute(
                    "UPDATE `sys`.`seats` SET `{}` = {} -{} WHERE (`date` = '{}') and (`train_id` = '{}');".format(
                        self.class_in, self.class_in, self.no_passengers, self.date_in, self.train_id))
                # self.mydb.commit()
                self.payment()
            else:
                self.mycursor.execute(
                    "INSERT INTO `sys`.`books` (`book_id`, `book_time`, `no_ppl`, `user_id`, `train_id`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
                        1, str(datetime.now()), self.no_passengers, self.user_id, self.train_id))
                self.mycursor.execute(
                    "UPDATE `sys`.`seats` SET `{}` = {} -{} WHERE (`date` = '{}') and (`train_id` = '{}');".format(
                        self.class_in, self.class_in, self.no_passengers, self.date_in, self.train_id))
                # self.mydb.commit()
                self.payment()
        paymentButton = Button(b, text="Proceed to payment", command=lambda :[b.destroy(),exec()])
        paymentButton.grid(row=4, column=2, columnspan=3, padx=20)
        b.mainloop()





    def payment(self):
        root = Tk()
        root.title("Railway Reservation System")
        root.geometry('420x200')
        pay = IntVar()
        p = Frame(root)
        p.grid(row=0, column=0)
        p.tkraise()
        self.p_type=""
        flag = 0
        self.mycursor.execute("Select payment_id from payment")
        payment_ids = self.mycursor.fetchall()
        l = len(payment_ids)
        if (payment_ids):
            flag = 1
        else:
            flag = 0
        def mode():
            if (pay.get() == 1):
                self.p_type="card"
                Label(p, text="Enter Credit Card No.").grid(row=2, column=0, columnspan=2, pady=5)
                ccNo = Entry(p, width=20)
                ccNo.place(x=175, y=65)
                Label(p, text="Enter Expiry date and CVV").grid(row=3, column=0, columnspan=2)
                ccDate = Entry(p, width=5)
                ccDate.place(x=185, y=90)
                ccCVV = Entry(p, width=5, show="*")
                ccCVV.grid(row=3, column=2)
                confirmpaymentButton = Button(p, text="Confirm Payment", command=paid)
                confirmpaymentButton.grid(row=4, column=0, columnspan=4)
                if (flag == 1):
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`payment` (`payment_id`, `user_id`, `type`, `amount`) VALUES ('{}', '{}', 'card', '{}');".format(
                            payment_ids[l - 1][0] + 1, self.user_id, self.amt))
                else:
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`payment` (`payment_id`, `user_id`, `type`, `amount`) VALUES ('{}', '{}', 'card', '{}');".format(
                            1, self.user_id, self.amt))
            elif (pay.get() == 2):
                self.p_type="paytm"
                Label(p, text="Enter Mobile No. registered with Paytm :").grid(row=2, column=0, columnspan=2, pady=5)
                mobileNo = Entry(p, width=20)
                mobileNo.place(x=220, y=65)
                confirmpaymentButton = Button(p, text="Confirm Payment", command=paid)
                confirmpaymentButton.grid(row=4, column=0, columnspan=4)
                if (flag == 1):
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`payment` (`payment_id`, `user_id`, `type`, `amount`) VALUES ('{}', '{}', 'paytm', '{}');".format(
                            payment_ids[l - 1][0] + 1, self.user_id, self.amt))
                else:
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`payment` (`payment_id`, `user_id`, `type`, `amount`) VALUES ('{}', '{}', 'paytm', '{}');".format(
                            1, self.user_id, self.amt))
        def paid():
            Label(p,
                  text="Rs {} deducted from your account".format(self.amt)).grid(
                row=5, column=0, columnspan=4)
            passengerinfoButton = Button(p, text="Proceed to enter passenger info", command=lambda :[root.destroy(),self.ticket_generation()])
            passengerinfoButton.grid(row=6, column=0, columnspan=4, sticky=E)

        Label(p, text="Payment Page", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W)
        Label(p, text="Mode of Payment:").grid(row=1, column=0)
        cardButton = Radiobutton(p, text="Credit Card", variable=pay, value=1)
        cardButton.grid(row=1, column=1, padx=10)
        paytmButton = Radiobutton(p, text="Paytm", variable=pay, value=2)
        paytmButton.grid(row=1, column=2, padx=10)
        confirmmodeButton = Button(p, text="Confirm Mode", command=mode)
        confirmmodeButton.grid(row=1, column=3)
        root.mainloop()



    def ticket_generation(self):
        flag = 0
        self.mycursor.execute("Select ticket_id from ticket")
        ticket_ids = self.mycursor.fetchall()
        l = len(ticket_ids)
        if (ticket_ids):
            flag = 1
        else:
            flag = 0
        self.mycursor.execute("Select * from train WHERE source='{}' and destination='{}'".format(self.source_in,
                                                                                                  self.destination_in))
        train = self.mycursor.fetchone()
        if (flag == 0):
            self.mycursor.execute(
                "INSERT INTO `sys`.`ticket` (`ticket_id`, `date`, `source`, `destination`, `arrival_time`, `departure_time`, `no_passengers`, `train_name`, `user_id`, `train_id`) VALUES ('1', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
                    self.date_in, train[4], train[3], train[1], train[2], self.no_passengers, self.train_name,
                    self.user_id, self.train_id))
            self.ticket_id = 1
            tkinter.messagebox.showinfo("Ticket info","Your Ticket id is 1")
        elif (flag == 1):
            self.mycursor.execute(
                "INSERT INTO `sys`.`ticket` (`ticket_id`, `date`, `source`, `destination`, `arrival_time`, `departure_time`, `no_passengers`, `train_name`, `user_id`, `train_id`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
                    ticket_ids[l - 1][0] + 1,
                    self.date_in, train[4], train[3], train[1], train[2], self.no_passengers, self.train_name,
                    self.user_id, self.train_id))
            print("Your ticket id is {}".format(ticket_ids[l - 1][0] + 1))
            tkinter.messagebox.showinfo("Ticket info", "Your Ticket id is {}".format(ticket_ids[l - 1][0] + 1))
            self.ticket_id = ticket_ids[l - 1][0] + 1
        self.passenger_info()

    def passenger_info(self):
        i = Tk()
        i.title("Passenger info")
        i.geometry("420x270")

        Label(i, text="Passenger Info", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W)
        Label(i, text="Number of passengers").grid(row=1, column=0, pady=5)
        Label(i, text="Amount Paid").grid(row=1, column=2, padx=10)

        passengerText = Label(i,text=self.no_passengers)
        passengerText.grid(row=1, column=1)
        amountText = Label(i,text=self.amt)
        amountText.grid(row=1, column=3)

        def final():

            if (self.no_passengers==1):
                i.geometry("420x270")
                Label(i, text="1.Enter Passenger Name").grid(row=2, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=3, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=4, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=5, pady=10, sticky=W)

                def execute():
                    name = pName1Entry.get()
                    a_no_str=pAadhar1Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    # self.mydb.commit()
                    i.destroy()




                pName1Entry = Entry(i, width=40)
                pName1Entry.grid(row=2, column=1, columnspan=3)
                pAadhar1Entry = Entry(i, width=40)
                pAadhar1Entry.grid(row=3, column=1, columnspan=3)
                pAge1Entry = Entry(i, width=40)
                pAge1Entry.grid(row=4, column=1, columnspan=3)
                pGender1Entry = Entry(i, width=40)
                pGender1Entry.grid(row=5, column=1, columnspan=3)
                submit1Button = Button(i, text="Submit", command=execute)
                submit1Button.grid(row=6, column=0, columnspan=4)


            elif (self.no_passengers==2):
                i.geometry("420x430")
                Label(i, text="1.Enter Passenger Name").grid(row=2, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=3, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=4, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=5, pady=10, sticky=W)

                pName1Entry = Entry(i, width=40)
                pName1Entry.grid(row=2, column=1, columnspan=3)
                pAadhar1Entry = Entry(i, width=40)
                pAadhar1Entry.grid(row=3, column=1, columnspan=3)
                pAge1Entry = Entry(i, width=40)
                pAge1Entry.grid(row=4, column=1, columnspan=3)
                pGender1Entry = Entry(i, width=40)
                pGender1Entry.grid(row=5, column=1, columnspan=3)



                def execute():
                    name = pName1Entry.get()
                    a_no_str = pAadhar1Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    name = pName2Entry.get()
                    a_no_str = pAadhar2Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    # self.mydb.commit()
                    i.destroy()

                Label(i, text="2.Enter Passenger Name").grid(row=6, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=7, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=8, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=9, pady=10, sticky=W)

                pName2Entry = Entry(i, width=40)
                pName2Entry.grid(row=6, column=1, columnspan=3)
                pAadhar2Entry = Entry(i, width=40)
                pAadhar2Entry.grid(row=7, column=1, columnspan=3)
                pAge2Entry = Entry(i, width=40)
                pAge2Entry.grid(row=8, column=1, columnspan=3)
                pGender2Entry = Entry(i, width=40)
                pGender2Entry.grid(row=9, column=1, columnspan=3)


                submit1Button = Button(i, text="Submit", command=execute)
                submit1Button.grid(row=10, column=0, columnspan=4)

            elif (self.no_passengers==3):
                i.geometry("420x590")
                Label(i, text="1.Enter Passenger Name").grid(row=2, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=3, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=4, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=5, pady=10, sticky=W)

                pName1Entry = Entry(i, width=40)
                pName1Entry.grid(row=2, column=1, columnspan=3)
                pAadhar1Entry = Entry(i, width=40)
                pAadhar1Entry.grid(row=3, column=1, columnspan=3)
                pAge1Entry = Entry(i, width=40)
                pAge1Entry.grid(row=4, column=1, columnspan=3)
                pGender1Entry = Entry(i, width=40)
                pGender1Entry.grid(row=5, column=1, columnspan=3)


                def execute():
                    name = pName1Entry.get()
                    a_no_str = pAadhar1Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    name = pName2Entry.get()
                    a_no_str = pAadhar2Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    name = pName3Entry.get()
                    a_no_str = pAadhar3Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    # self.mydb.commit()
                    i.destroy()






                Label(i, text="2.Enter Passenger Name").grid(row=6, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=7, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=8, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=9, pady=10, sticky=W)

                pName2Entry = Entry(i, width=40)
                pName2Entry.grid(row=6, column=1, columnspan=3)
                pAadhar2Entry = Entry(i, width=40)
                pAadhar2Entry.grid(row=7, column=1, columnspan=3)
                pAge2Entry = Entry(i, width=40)
                pAge2Entry.grid(row=8, column=1, columnspan=3)
                pGender2Entry = Entry(i, width=40)
                pGender2Entry.grid(row=9, column=1, columnspan=3)


                Label(i, text="3.Enter Passenger Name").grid(row=10, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=11, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=12, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=13, pady=10, sticky=W)

                pName3Entry = Entry(i, width=40)
                pName3Entry.grid(row=10, column=1, columnspan=3)
                pAadhar3Entry = Entry(i, width=40)
                pAadhar3Entry.grid(row=11, column=1, columnspan=3)
                pAge3Entry = Entry(i, width=40)
                pAge3Entry.grid(row=12, column=1, columnspan=3)
                pGender3Entry = Entry(i, width=40)
                pGender3Entry.grid(row=13, column=1, columnspan=3)


                submit1Button = Button(i, text="Submit", command=execute)
                submit1Button.grid(row=14, column=0, columnspan=4)

            elif (self.no_passengers==4):
                i.geometry("420x755")
                Label(i, text="1.Enter Passenger Name").grid(row=2, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=3, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=4, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=5, pady=10, sticky=W)

                pName1Entry = Entry(i, width=40)
                pName1Entry.grid(row=2, column=1, columnspan=3)
                pAadhar1Entry = Entry(i, width=40)
                pAadhar1Entry.grid(row=3, column=1, columnspan=3)
                pAge1Entry = Entry(i, width=40)
                pAge1Entry.grid(row=4, column=1, columnspan=3)
                pGender1Entry = Entry(i, width=40)
                pGender1Entry.grid(row=5, column=1, columnspan=3)

                def execute():
                    name = pName1Entry.get()
                    a_no_str = pAadhar1Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    name = pName2Entry.get()
                    a_no_str = pAadhar2Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    name = pName3Entry.get()
                    a_no_str = pAadhar3Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    name = pName4Entry.get()
                    a_no_str = pAadhar4Entry.get()
                    a_no = int(a_no_str)
                    self.mycursor.execute(
                        "INSERT INTO `sys`.`passenger` (`pass_name`, `aadhar_no`, `ticket_id`) VALUES ('{}', '{}', '{}');".format(
                            name, a_no, self.ticket_id))
                    # self.mydb.commit()
                    i.destroy()






                Label(i, text="2.Enter Passenger Name").grid(row=6, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=7, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=8, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=9, pady=10, sticky=W)

                pName2Entry = Entry(i, width=40)
                pName2Entry.grid(row=6, column=1, columnspan=3)
                pAadhar2Entry = Entry(i, width=40)
                pAadhar2Entry.grid(row=7, column=1, columnspan=3)
                pAge2Entry = Entry(i, width=40)
                pAge2Entry.grid(row=8, column=1, columnspan=3)
                pGender2Entry = Entry(i, width=40)
                pGender2Entry.grid(row=9, column=1, columnspan=3)


                Label(i, text="3.Enter Passenger Name").grid(row=10, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=11, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=12, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=13, pady=10, sticky=W)

                pName3Entry = Entry(i, width=40)
                pName3Entry.grid(row=10, column=1, columnspan=3)
                pAadhar3Entry = Entry(i, width=40)
                pAadhar3Entry.grid(row=11, column=1, columnspan=3)
                pAge3Entry = Entry(i, width=40)
                pAge3Entry.grid(row=12, column=1, columnspan=3)
                pGender3Entry = Entry(i, width=40)
                pGender3Entry.grid(row=13, column=1, columnspan=3)


                Label(i, text="4.Enter Passenger Name").grid(row=14, pady=10, sticky=W)
                Label(i, text="Enter Passenger Aadhar No.").grid(row=15, pady=10, sticky=W)
                Label(i, text="Enter Passenger Age").grid(row=16, pady=10, sticky=W)
                Label(i, text="Enter Passenger Gender").grid(row=17, pady=10, sticky=W)

                pName4Entry = Entry(i, width=40)
                pName4Entry.grid(row=14, column=1, columnspan=3)
                pAadhar4Entry = Entry(i, width=40)
                pAadhar4Entry.grid(row=15, column=1, columnspan=3)
                pAge4Entry = Entry(i, width=40)
                pAge4Entry.grid(row=16, column=1, columnspan=3)
                pGender4Entry = Entry(i, width=40)
                pGender4Entry.grid(row=17, column=1, columnspan=3)


                submit1Button = Button(i, text="Submit", command=execute)
                submit1Button.grid(row=18, column=0, columnspan=4)

        submitButton = Button(i, text="Submit", command=final)
        submitButton.grid(row=1, column=5, columnspan=4)


        i.mainloop()


    def ticket_info(self):
        t = Tk()
        t.title("Ticket Details")
        t.geometry("360x430")
        def display():
            ticket_no_str = IDEntry.get()
            ticket_no=int(ticket_no_str)
            self.mycursor.execute("Select * from ticket WHERE ticket_id={}".format(ticket_no))
            ticket_info = self.mycursor.fetchone()
            print(
                "{} to {} {} train on {}. Departure Time:{},Arrival Time:{}. Train id: {}. No of passengers: {}".format(
                    ticket_info[2], ticket_info[3], ticket_info[7], ticket_info[1], ticket_info[5], ticket_info[4],
                    ticket_info[9], ticket_info[6]))
            source.delete(1.0, END)
            source.configure(state='normal')
            source.insert(INSERT,ticket_info[2])
            destination.delete(1.0, END)
            destination.configure(state='normal')
            destination.insert(INSERT, ticket_info[3])
            tID.delete(1.0, END)
            tID.configure(state='normal')
            tID.insert(INSERT, ticket_info[9])
            tName.delete(1.0, END)
            tName.configure(state='normal')
            tName.insert(INSERT, ticket_info[7])
            DOJ.delete(1.0, END)
            DOJ.configure(state='normal')
            DOJ.insert(INSERT, ticket_info[1])
            dTime.delete(1.0, END)
            dTime.configure(state='normal')
            dTime.insert(INSERT, ticket_info[5])
            aTime.delete(1.0, END)
            aTime.configure(state='normal')
            aTime.insert(INSERT, ticket_info[4])
            noPass.delete(1.0, END)
            noPass.configure(state='normal')
            noPass.insert(INSERT, ticket_info[6])
        Label(t, text="Ticket Info", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W)
        Label(t, text="Ticket ID").grid(row=1, column=0, pady=5)
        Label(t, text="Source").grid(row=2, column=0, pady=10, sticky=W + E)
        Label(t, text="Destination").grid(row=3, pady=10, sticky=W + E)
        Label(t, text="Train ID").grid(row=4, pady=10, sticky=W + E)
        Label(t, text="Train Name").grid(row=5, pady=10, sticky=W + E)
        Label(t, text="Date of Journey").grid(row=6, pady=10, sticky=W + E)
        Label(t, text="Departure Time").grid(row=7, pady=10, sticky=W + E)
        Label(t, text="Arrival Time").grid(row=8, pady=10, sticky=W + E)
        Label(t, text="No. of Passengers").grid(row=9, pady=10, sticky=W + E)
        submitButton = Button(t, text="Submit",command=display)
        submitButton.grid(row=1, column=1)
        IDEntry = Entry(t, width=10)
        IDEntry.place(x=105, y=38)
        source = Text(t, width=30, height=1,state='disabled')
        source.grid(row=2, column=1)
        destination = Text(t, width=30, height=1,state='disabled')
        destination.grid(row=3, column=1)
        tID = Text(t, width=30, height=1,state='disabled')
        tID.grid(row=4, column=1)
        tName = Text(t, width=30, height=1,state='disabled')
        tName.grid(row=5, column=1)
        DOJ = Text(t, width=30, height=1,state='disabled')
        DOJ.grid(row=6, column=1)
        dTime = Text(t, width=30, height=1,state='disabled')
        dTime.grid(row=7, column=1)
        aTime = Text(t, width=30, height=1,state='disabled')
        aTime.grid(row=8, column=1)
        noPass = Text(t, width=30, height=1,state='disabled')
        noPass.grid(row=9, column=1, padx=5)
        t.mainloop()
        # self.mycursor.execute("Select * from passenger WHERE ticket_id={}".format(ticket_no))
        # passenger_info = self.mycursor.fetchall()
        # for count, ele in enumerate(passenger_info):
        #     print("Details of passenger {}: ".format(count + 1))
        #     print("Name: {}, Aadhar number: {}".format(ele[0], ele[1]))
        #     print("")

    def insert(self):
        a = Tk()
        a.title("Administrator Privileges")
        a.geometry("300x430")

        def add_train():
            source = tSourceEntry.get()
            destination = tDestinationEntry.get()
            train_id = int(tIDEntry.get())
            train_name = tNameEntry.get()
            day = tDOJEntry.get()
            AT = tAtimeEntry.get()
            DT = tDtimeEntry.get()
            dict = {"Monday": None, "Tuesday": None, "Wednesday": 1, "Thursday": None, "Friday": None, "Saturday": None,
                    "Sunday": None}
            prev_key = ""
            while (any([v == None for v in dict.values()])):
                for key, value in dict.items():
                    if (value == 1):
                        prev_key = key
                        continue
                    if (prev_key):
                        dict[key] = dict[prev_key] + 1
                        prev_key = key
            self.mycursor.execute(
                "INSERT INTO `sys`.`train` (`train_id`, `arrival_time`, `departure_time`, `destination`, `source`, `train_name`, `total seats`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '40');".format(
                    train_id, AT, DT, destination, source, train_name))
            date_object = date(2020, 1, dict[day])
            while date_object.year == 2020:
                self.mycursor.execute(
                    "INSERT INTO `sys`.`seats` (`2_Tier`, `3_Tier`, `sleeper`, `general`, `destination`, `source`, `train_id`, `date`, `train_name`) VALUES ('10', '10', '10', '10', '{}', '{}', '{}', '{}', '{}');".format(
                        destination, source, train_id, str(date_object), train_name))
                date_object += timedelta(days=7)
            self.mydb.commit()
            tkinter.messagebox.showinfo("Administration Message", "Train added Successfully")
            a.destroy()

        Label(a, text="Admin Page", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4, sticky=E + W,
                                                                       pady=12)
        Label(a, text="Train ID").grid(row=1, pady=10, sticky=W)
        Label(a, text="Train Name").grid(row=2, pady=10, sticky=W)
        Label(a, text="Source").grid(row=3, column=0, pady=10, sticky=W)
        Label(a, text="Destination").grid(row=4, pady=10, sticky=W)
        Label(a, text="Day of travel").grid(row=5, pady=10, sticky=W)
        Label(a, text="Departure Time").grid(row=6, pady=10, sticky=W)
        Label(a, text="Arrival Time").grid(row=7, pady=10, sticky=W)
        Label(a, text="Total Seats").grid(row=8, pady=10, sticky=W)

        tIDEntry = Entry(a, width=30)
        tIDEntry.grid(row=1, column=1)
        tNameEntry = Entry(a, width=30)
        tNameEntry.grid(row=2, column=1)
        tSourceEntry = Entry(a, width=30)
        tSourceEntry.grid(row=3, column=1)
        tDestinationEntry = Entry(a, width=30)
        tDestinationEntry.grid(row=4, column=1)
        tDOJEntry = Entry(a, width=30)
        tDOJEntry.grid(row=5, column=1)
        tDtimeEntry = Entry(a, width=30)
        tDtimeEntry.grid(row=6, column=1)
        tAtimeEntry = Entry(a, width=30)
        tAtimeEntry.grid(row=7, column=1)
        tSeatsEntry = Entry(a, width=30)
        tSeatsEntry.grid(row=8, column=1)

        signupButton = Button(a, text="Add Train", command=add_train, width=15)
        signupButton.grid(row=9, columnspan=2, pady=7)

        a.mainloop()


obj=test2()
# obj.signup()
# obj.search()
# obj.login()
# obj.payment()
# obj.ticket_info()
# obj.insert()
obj.menu()
# obj.passenger_info()
