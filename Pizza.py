#importing tkinter
from tkinter import *
import time
from sqlite3 import *
from tkinter import messagebox


# Pizza class
class Pizza:
    cartlist=[]
    amount=0
#--  page 1------
    def main(sf):
        try:
            # Destroy previous window if any
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass
        # Size and placement of window
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        # Caption
        sf.scr.title("Python Tkinter GUI application")
        # icon
        sf.scr.iconbitmap('p.ico')

        # Image size
        sf.mainf1=Frame(sf.scr,height=100,width=1000)
        sf.logo=PhotoImage(file="logo1.png")
        sf.l=Label(sf.mainf1,image=sf.logo)

        # logo placement
        sf.l.place(x=70,y=0)

        # Frame size
        sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=618,width=1000)
        sf.c=Canvas(sf.mainf2,height=618,width=1000)
        sf.c.pack()

        # Pizza background
        sf.back=PhotoImage(file="pizzamain.png")

        # pizza background
        sf.c.create_image(500,304,image=sf.back)

        # Button to enter login page
        sf.lab=Button(sf.mainf2,text= "Click Here to Enter store",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("algerian",30, 'bold'),fg="black",bg="#a80202")
        
        # Placemet of button
        sf.lab.place(x=190,y=250)
        sf.mainf2.pack(fill=BOTH,expand=1)

        # loop
        sf.scr.mainloop()

#------ page 2------
    def Login(sf):
        # list for cart
        sf.cartlist=[]

        # Checking the amount
        sf.amount=0

        # destroy previous window
        sf.scr.destroy()
        sf.scr=Tk()

        # Caption
        sf.scr.title("Python Tkinter GUI application")

        # Placement and size of window
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))

        # Frame size 
        sf.loginf1=Frame(sf.scr,height=150,width=1000)

        # logo(pizza)
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.ba=Label(sf.loginf1,image=sf.logo,height=150).place(x=70,y=0)

        # Home button 
        sf.home=Button(sf.loginf1,text="Home",command=lambda:sf.main(),bg="black",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        
        # Home button placement
        sf.home.place(x=10,y=110)

        # Administrator login button
        sf.adlog=Button(sf.loginf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="black",fg="white",font=("algerian",16))
        
        # Placement of button
        sf.adlog.place(x=370,y=110)

        # Getting the local time
        sf.localtime=time.asctime(time.localtime(time.time()))

        # Time rectangle
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="white",font=("default",16),bg="black")

        # Time placement
        sf.tim.place(x=730,y=110)

        sf.loginf1.pack(fill=BOTH,expand=1)
        sf.loginf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.loginf2,height=618,width=1366)
        sf.c.pack()

        # Pizza background
        sf.logo1=PhotoImage(file="pizzamain.png")

        # Placement of background
        sf.c.create_image(500,309,image=sf.logo1)

        # Create rectangle
        sf.c.create_rectangle(250,100,780,450,fill="#a80202",outline="white",width=6)

        # Login button
        sf.log=Label(sf.loginf2,text="LOGIN",fg="white",bg="black",width=20,font=("algerian",27))

        # Placement of the button
        sf.log.place(x=289,y=105)

        # Username logo
        sf.lab1=Label(sf.loginf2,text="UserName",bg="#a80202",font=("algerian",22))

        # Placement of logo
        sf.lab1.place(x=260,y=180)

        # Entry to type text
        sf.user=Entry(sf.loginf2,bg="white",font=("algerian",22),bd=6 ,justify='left')

        # Entry placement
        sf.user.place(x=420,y=180)

        # Password logo
        sf.lab2=Label(sf.loginf2,text="Password",bg="#a80202",font=("algerian",22))

        # Placement of logo
        sf.lab2.place(x=260,y=250)

        # Entry for password
        sf.pasd=Entry(sf.loginf2,bg="white",font=("algerian",22),bd=6 ,justify='left')

        # Placement for password
        sf.pasd.place(x=420,y=250)

        # Button for login
        sf.lg=Button(sf.loginf2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="black",font=("algerian",20),bd=4)
        #  Button for placement
        sf.lg.place(x=360,y=320)

        # funtion to clear text
        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)

        # Button for clear text
        sf.cl=Button(sf.loginf2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="black",font=("algerian",20),bd=4)
        
        # Placement to clear text
        sf.cl.place(x=560,y=320)

        # Button for registration
        sf.rg=Button(sf.loginf2,text="New into MyPizzaStore",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("algerian",20),bd=6)
        
        # Placement of the button
        sf.rg.place(x=340,y=380)
        sf.loginf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    #Getting username and password
    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass

# ------Every other page follows pretty much the same code-------
#--  page 3------
    def Adminlogin(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Python Tkinter GUI application")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.adminf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.adminf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.adminf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.adminf1.pack(fill=BOTH,expand=1)
        sf.adminf2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.adminf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(350,100,1016,450,fill="#a80202",outline="white",width=6)
        sf.log=Label(sf.adminf2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=27,font=("algerian",27))
        sf.log.place(x=357,y=110)
        sf.lab1=Label(sf.adminf2,text="UserName",bg="#a80202",font=("algerian",22))
        sf.lab1.place(x=400,y=200)
        sf.usera=Entry(sf.adminf2,bg="white",font=("algerian",22),bd=5)
        sf.usera.place(x=650,y=200)
        sf.lab2=Label(sf.adminf2,text="Password",bg="#a80202",font=("algerian",22))
        sf.lab2.place(x=405,y=270)
        sf.pasda=Entry(sf.adminf2,bg="white",font=("algerian",22),bd=5)
        sf.pasda.place(x=650,y=270)
        sf.lg=Button(sf.adminf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.admindatabase(),font=("algerian",20,'bold'),bd=5)
        sf.lg.place(x=650,y=350)
        sf.cl=Button(sf.adminf2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Login(),font=("algerian",20,'bold'),bd=5)
        sf.cl.place(x=400,y=350)
        def clear(sf):
            sf.usera.delete(0,END)
            sf.pasda.delete(0,END)
        sf.rg=Button(sf.adminf2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(sf),bd=5,font=("algerian",20,'bold'))
        sf.rg.place(x=880,y=350)
        
        sf.adminf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultadmin(sf):
        sf.loguser=sf.usera.get()
        sf.logpass=sf.pasda.get()
        return sf.loguser,sf.logpass

#--  page 4------
    def Register(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Python Tkinter GUI application")
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        #sf.scr.resizable(False, False)
        sf.regf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.ba=Label(sf.regf1,image=sf.logo,height=150).place(x=70,y=0)
        sf.home=Button(sf.regf1,text="Home",command=lambda:sf.main(),bg="black",cursor="hand2",fg="white",font=("default",16))
        sf.home.place(x=10,y=110)
        sf.adlog=Button(sf.regf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bg="black",fg="white",font=("default",16))
        sf.adlog.place(x=370,y=110)
      
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.regf1,text=sf.localtime,fg="white",font=("default",16),bg="black")
        sf.tim.place(x=730,y=110)
        sf.regf1.pack(fill=BOTH,expand=1)
        
        sf.regf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.regf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(500,304,image=sf.logo1)
        sf.c.create_rectangle(150,100,900,450,fill="#a80202",outline="white",width=6)
        sf.log=Label(sf.regf2,text="REGISTRATION",fg="white",bg="black",width=20,font=("algerian",27))
        sf.log.place(x=280,y=120)
        sf.lab1=Label(sf.regf2,text="FirstName",bg="#a80202",font=("algerian",18))
        sf.lab1.place(x=160,y=200)
        sf.first=Entry(sf.regf2,bg="white",width=15,font=("algerian",18),bd=5)
        sf.first.place(x=300,y=200)
        sf.lab2=Label(sf.regf2,text="LastName",bg="#a80202",font=("algerian",18))
        sf.lab2.place(x=530,y=200)
        sf.last=Entry(sf.regf2,bg="white",width=15,font=("algerian",18),bd=5)
        sf.last.place(x=660,y=200)
        sf.lab3=Label(sf.regf2,text="Username",bg="#a80202",font=("algerian",18))
        sf.lab3.place(x=160,y=250)
        sf.usern=Entry(sf.regf2,bg="white",width=15,font=("algerian",18),bd=5)
        sf.usern.place(x=300,y=250)
        sf.lab4=Label(sf.regf2,text="Password",bg="#a80202",font=("algerian",18))
        sf.lab4.place(x=530,y=250)
        sf.passd=Entry(sf.regf2,bg="white",width=15,font=("algerian",18),bd=5)
        sf.passd.place(x=660,y=250)
        sf.lab5=Label(sf.regf2,text="Email",bg="#a80202",font=("algerian",18))
        sf.lab5.place(x=210,y=300)
        sf.email=Entry(sf.regf2,bg="white",width=15,font=("algerian",18),bd=5)
        sf.email.place(x=300,y=300)
        sf.lab6=Label(sf.regf2,text="Mobile No.",bg="#a80202",font=("algerian",18))
        sf.lab6.place(x=530,y=300)
        sf.mob=Entry(sf.regf2,bg="white",width=15,font=("algerian",18),bd=5)
        sf.mob.place(x=660,y=300)
        sf.bc=Button(sf.regf2,text="Back",cursor="hand2",command=lambda:sf.Login(),fg="white",bg="black",font=("algerian",18),bd=5)
        sf.bc.place(x=170,y=370)
        sf.rg=Button(sf.regf2,text="Register",cursor="hand2",fg="white",bg="black",command=lambda:sf.Regdatabase(),font=("algerian",18),bd=5)
        sf.rg.place(x=430,y=370)
        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)
        sf.cl=Button(sf.regf2,text="Clear",cursor="hand2",fg="white",bg="black",command=lambda:clear(sf),font=("algerian",18),bd=5)
        sf.cl.place(x=780,y=370)
        sf.regf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob=sf.mob.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob

#--  page 5------
    def adminmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Pizza GUI")
        sf.scr.geometry("1366x768")

        sf.admainf1=Frame(sf.scr,bg="#f2e8b8",height=150,width=1366)
        sf.admainf1.pack(side=TOP,fill=BOTH)
        sf.c=Canvas(sf.admainf1,height=150,bg="#f2e8b8",width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo2.png")
        sf.c.create_image(683,50,image=sf.logo)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(900,50,text=sf.localtime,fill="white",font=("default",16))
        sf.c.create_text(683,125,font=( 'algerian' ,25, 'bold','underline' ),text="Management System")
        sf.out=Button(sf.admainf1,text="Log Out",bg="#0b1335",cursor="hand2",command=lambda:sf.Adminlogin(),fg="white",bd=5,font=("default",16,'bold'))
        sf.out.place(x=1100,y=25)

        def Ref(sf):
            sf.con=connect("pizza.db")
            sf.cur=sf.con.cursor()
            try:
                 sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                 sf.con.commit()
            except:
                pass
            x=sf.cur.execute("select count(*) from orderdetail")
            ordno=list(x)[0][0]+1
            sf.order.set(ordno)

            sf.v1=sf.vp1.get()
            if sf.v1=="Medium":
                sf.p1=float(sf.Deluxe_Veggie.get())*450
            elif sf.v1=="Large":
                sf.p1=float(sf.Deluxe_Veggie.get())*650
            else:
                sf.p1=float(sf.Deluxe_Veggie.get())*250
            sf.v2=sf.vp2.get()
            if sf.v2=="Medium":
                sf.p2= float(sf.Veg_Vaganza.get())*400
            elif sf.v2=="Large":
                sf.p2= float(sf.Veg_Vaganza.get())*600
            else:
                sf.p2= float(sf.Veg_Vaganza.get())*250
            sf.v3=sf.vp3.get()
            if sf.v3=="Medium":
                sf.p3= float(sf.Pepper.get())*385
            elif sf.v3=="Large":
                sf.p3= float(sf.Pepper.get())*550
            else:
                sf.p3= float(sf.Pepper.get())*225
            sf.v4=sf.vp4.get()
            if sf.v4=="Medium":
                sf.p4= float(sf.Margherita.get())*195
            elif sf.v4=="Large":
                sf.p4= float(sf.Margherita.get())*385
            else:
                sf.p4= float(sf.Margherita.get())*99
            sf.v5=sf.vp5.get()
            if sf.v5=="Medium":
                sf.p5= float(sf.Non_Veg_Supreme.get())*450
            elif sf.v5=="Large":
                sf.p5= float(sf.Non_Veg_Supreme.get())*650
            else:
                sf.p5= float(sf.Non_Veg_Supreme.get())*250
            sf.v6=sf.vp6.get()
            if sf.v6=="Medium":
                sf.p6= float(sf.Chicken_Tikka.get())*400
            elif sf.v6=="Large":
                sf.p6= float(sf.Chicken_Tikka.get())*600
            else:
                sf.p6= float(sf.Chicken_Tikka.get())*225
            sf.v7=sf.vp7.get()
            if sf.v7=="Medium":
                sf.p7= float(sf.Chicken_Sausage.get())*385
            elif sf.v7=="Large":
                sf.p7= float(sf.Chicken_Sausage.get())*550
            else:
                sf.p7= float(sf.Chicken_Sausage.get())*225
            sf.v8=sf.vp8.get()
            if sf.v8=="Medium":
                sf.p8= float(sf.Chicken_Peri.get())*195
            elif sf.v8=="Large":
                sf.p8= float(sf.Chicken_Peri.get())*385
            else:
                sf.p8= float(sf.Chicken_Peri.get())*99

            
            sf.costofmeal = "Rs.",str('%.2f'% (sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14))
            sf.PayTax=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)*.05)
            sf.Totalcost=(sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)
            sf.Ser_Charge=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)/99)
            sf.Service="Rs."+str('%.2f'% sf.Ser_Charge)
            sf.OverAllCost="Rs."+str(int(sf.PayTax + sf.Totalcost + sf.Ser_Charge))
            sf.PaidTax="Rs."+str('%.2f'% sf.PayTax)
            sf.money=int(sf.PayTax + sf.Totalcost + sf.Ser_Charge)
            sf.Service_Charge.set(sf.Service)
            sf.cost.set(sf.costofmeal)
            sf.Tax.set(sf.PaidTax)
            sf.Total.set(sf.OverAllCost) 

        def reset(sf):
            sf.Deluxe_Veggie.set("0")
            sf.Veg_Vaganza.set("0")
            sf.Pepper.set("0")
            sf.Margherita.set("0")
            sf.Non_Veg_Supreme.set("0")
            sf.Chicken_Tikka.set("0")
            sf.Chicken_Sausage.set("0")
            sf.Chicken_Peri.set("0")
            sf.Total.set("0")
            sf.Service_Charge.set("0")
            sf.Tax.set("0")
            sf.cost.set("0")
            sf.order.set("0")
            sf.Cutomer_name.set("")
            sf.cusmob.set("")
            sf.vp1.set("Medium")
            sf.vp2.set("Medium")
            sf.vp3.set("Medium")
            sf.vp4.set("Medium")
            sf.vp5.set("Medium")
            sf.vp6.set("Medium")
            sf.vp7.set("Medium")
            sf.vp8.set("Medium")

            
        def price(sf):
            sf.roo = Tk()
            sf.roo.geometry("600x768+0+0")
            sf.roo.title("Price List")
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
            sf.lblinfo.grid(row=0, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15,'bold'), text="Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
            sf.lblinfo.grid(row=0, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Deluxe Veggie", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Veg Vaganza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="5 sf.Pepper", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="sf.Margherita", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Supreme", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Tikka", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Suasage", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Peri", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=2)
   

            sf.roo.mainloop()


        sf.admainf2 = Frame(sf.scr,width =1366,bg="#f2e8b8",height=618,relief=SUNKEN)
        sf.admainf2.pack(side=BOTTOM,fill=BOTH,expand=1)
        sf.Deluxe_Veggie= StringVar()
        sf.Veg_Vaganza = StringVar()
        sf.Pepper = StringVar()
        sf.Margherita= StringVar()
        sf.Non_Veg_Supreme = StringVar()
        sf.Chicken_Tikka = StringVar()
        sf.Chicken_Sausage= StringVar()
        sf.Chicken_Peri= StringVar()

        sf.Total = StringVar()
        sf.Service_Charge= StringVar()
        sf.Tax = StringVar()
        sf.cost = StringVar()
        sf.order=StringVar()
        sf.Cutomer_name =StringVar()
        sf.cusmob = StringVar()
        sf.vp1=StringVar()
        sf.vp2=StringVar()
        sf.vp3=StringVar()
        sf.vp4=StringVar()
        sf.vp5=StringVar()
        sf.vp6=StringVar()
        sf.vp7=StringVar()
        sf.vp8=StringVar()
        reset(sf)
        sf.l=["Medium","Large","Regular"]

        #veg pizza
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'algerian' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=1)
        sf.lbl1 = Label(sf.admainf2,pady=2, font=( 'algerian' ,20, 'bold','underline' ),bg="#f2e8b8",text="Veg Pizza",bd=10,anchor='w')
        sf.lbl1.place(x=180,y=0)
        sf.lbl11 = Label(sf.admainf2,pady=2, font=( 'algerian' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl11.grid(row=1,column=0)
        sf.lbl12 = Label(sf.admainf2,pady=2, font=( 'algerian' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl12.grid(row=1,column=1)
        sf.lbl13 = Label(sf.admainf2,pady=2, font=( 'algerian' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl13.grid(row=1,column=2,padx=4)

        sf.lbldel= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Deluxe Veggie:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbldel.grid(row=2,column=0)
        sf.opdel=OptionMenu(sf.admainf2,sf.vp1,*sf.l)
        sf.opdel.config(width=6)
        sf.opdel.grid(row=2,column=1)
        sf.txtdel= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Deluxe_Veggie , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtdel.grid(row=2,column=2)

        sf.lblvaga = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Veg Vaganza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblvaga.grid(row=3,column=0)
        sf.opvaga=OptionMenu(sf.admainf2,sf.vp2,*sf.l)
        sf.opvaga.config(width=6)
        sf.opvaga.grid(row=3,column=1)
        sf.txtvaga = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Veg_Vaganza , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtvaga.grid(row=3,column=2)

        sf.lblpep= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text=" 5 Pepper:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpep.grid(row=4,column=0)
        sf.oppep=OptionMenu(sf.admainf2,sf.vp3,*sf.l)
        sf.oppep.config(width=6)
        sf.oppep.grid(row=4,column=1)
        sf.txtpep= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Pepper ,bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtpep.grid(row=4,column=2)

        sf.lblmag = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Margherita:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmag.grid(row=5,column=0)
        sf.opmag=OptionMenu(sf.admainf2,sf.vp4,*sf.l)
        sf.opmag.config(width=6)
        sf.opmag.grid(row=5,column=1)
        sf.txtmag = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Margherita,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtmag.grid(row=5,column=2)


        #sf.non veg
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'algerian' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=6,column=1)
        sf.lbl2 = Label(sf.admainf2,pady=2, font=( 'algerian' ,20, 'bold','underline' ),bg="#f2e8b8",text="Non-Veg Pizza",bd=10,anchor='w')
        sf.lbl2.place(x=150,y=290)
        sf.lbl21 = Label(sf.admainf2,pady=2, font=( 'algerian' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl21.grid(row=7,column=0)
        sf.lbl22 = Label(sf.admainf2,pady=2, font=( 'algerian' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl22.grid(row=7,column=1)
        sf.lbl23 = Label(sf.admainf2,pady=2, font=( 'algerian' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl23.grid(row=7,column=2)

        sf.lblsup= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Non-Veg Supreme:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsup.grid(row=8,column=0)
        sf.opsup=OptionMenu(sf.admainf2,sf.vp5,*sf.l)
        sf.opsup.config(width=6)
        sf.opsup.grid(row=8,column=1)
        sf.txtsup= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Non_Veg_Supreme , bd=6,bg="powder blue" ,justify='right')
        sf.txtsup.grid(row=8,column=2)

        sf.lbltika = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Tikka:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltika.grid(row=9,column=0)
        sf.optika=OptionMenu(sf.admainf2,sf.vp6,*sf.l)
        sf.optika.config(width=6)
        sf.optika.grid(row=9,column=1)
        sf.txttika = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Tikka , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txttika.grid(row=9,column=2)

        sf.lblsaus= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Sausage:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsaus.grid(row=10,column=0)
        sf.opsaus=OptionMenu(sf.admainf2,sf.vp7,*sf.l)
        sf.opsaus.config(width=6)
        sf.opsaus.grid(row=10,column=1)
        sf.txtsaus= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Sausage , bd=6,bg="powder blue" ,justify='right')
        sf.txtsaus.grid(row=10,column=2)

        sf.lblperi = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Peri:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblperi.grid(row=11,column=0)
        sf.opperi=OptionMenu(sf.admainf2,sf.vp8,*sf.l)
        sf.opperi.config(width=6)
        sf.opperi.grid(row=11,column=1)
        sf.txtperi= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.Chicken_Peri , bd=6,bg="powder blue" ,justify='right')
        sf.txtperi.grid(row=11,column=2)

        #Special
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'algerian' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=5)

        # customer
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'algerian' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=8)
        sf.lbl6 = Label(sf.admainf2,pady=2, font=( 'algerian' ,22, 'bold','underline' ),bg="#f2e8b8",text="Customer Detail",bd=10,anchor='w')
        sf.lbl6.place(x=970,y=0)
        
        sf.lblnam= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Name:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblnam.grid(row=1,column=7)
        sf.txtnam= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Cutomer_name , bd=6,width=14,bg="powder blue" ,justify='left')
        sf.txtnam.grid(row=1,column=8)


        sf.lblmob = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Mobile No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmob.grid(row=2,column=7)
        sf.txtmob = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.cusmob,width=14,bd=6,bg="powder blue" ,justify='left')
        sf.txtmob.grid(row=2,column=8)

        #bill
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'algerian' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=3,column=8)
        sf.lbl5 = Label(sf.admainf2,pady=2, font=( 'algerian' ,22, 'bold','underline' ),bg="#f2e8b8",text="Bill Payment",bd=10,anchor='w')
        sf.lbl5.place(x=1000,y=140)

        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'algerian' ,20),width=5,bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=4,column=6)
        sf.lblord= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Order No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblord.grid(row=4,column=7)
        sf.txtord= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.order , bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txtord.grid(row=4,column=8)

        sf.lblco = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Subtotal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblco.grid(row=5,column=7)
        sf.txtco = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.cost,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtco.grid(row=5,column=8)

        sf.lblser= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Service Charge:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblser.grid(row=6,column=7)
        sf.txtser= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Service_Charge ,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtser.grid(row=6,column=8)

        sf.lbltax = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Tax:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltax.grid(row=7,column=7)
        sf.txttax = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Tax, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttax.grid(row=7,column=8)

        sf.lbltot = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Total:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltot.grid(row=8,column=7)
        sf.txttot = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Total, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttot.grid(row=8,column=8)

        sf.btnprice=Button(sf.admainf2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PRICE", bg="powder blue",command=lambda:price(sf))
        sf.btnprice.place(x=970,y=440)

        sf.btnTotal=Button(sf.admainf2,pady=2,bd=6,fg="black",font=('ariel' ,16,'bold'),width=6, text="TOTAL", bg="powder blue",command=lambda:Ref(sf))
        sf.btnTotal.place(x=1160,y=440)

        sf.btnreset=Button(sf.admainf2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=lambda:reset(sf))
        sf.btnreset.place(x=970,y=500)

        sf.btnpay=Button(sf.admainf2,pady=2, bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PAY", bg="powder blue",command=lambda:sf.adminorderdetail())
        sf.btnpay.place(x=1160,y=500)

        sf.scr.mainloop()

    def resultadminorder(sf):
        r1=sf.Deluxe_Veggie.get()
        r2=sf.Veg_Vaganza.get()
        r3=sf.Pepper.get()
        r4=sf.Margherita.get()
        r5=sf.Non_Veg_Supreme.get()
        r6=sf.Chicken_Tikka.get()
        r7=sf.Chicken_Sausage.get()
        r8=sf.Chicken_Peri.get()

        r20=sf.Cutomer_name.get()
        r21=sf.cusmob.get()
        r22=sf.vp1.get()
        r23=sf.vp2.get()
        r24=sf.vp3.get()
        r25=sf.vp4.get()
        r26=sf.vp5.get()
        r27=sf.vp6.get()
        r28=sf.vp7.get()
        r29=sf.vp8.get()

        l1=[r1,r22,30]
        l2=[r2,r23,31]
        l3=[r3,r24,32]
        l4=[r4,r25,33]
        l5=[r5,r26,34]
        l6=[r6,r27,35]
        l7=[r7,r28,36]
        l8=[r8,r29,37]
        
        return r20,r21,l1,l2,l3,l4,l5,l6,l7,l8


#--  page 6------        
    def menulist(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Python Tkinter GUI application")
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        #sf.scr.resizable(False, False)
        sf.menuf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.menuf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.c.create_image(503,75,image=sf.logo)
        
        sf.home=Button(sf.menuf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.menuf1.pack(fill=BOTH,expand=1)

        sf.menuf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.menuf2,height=618,width=1366)
        sf.c.pack()
        sf.back=PhotoImage(file="pizzamain.png")
        sf.c.create_image(500,304,image=sf.back)
        sf.c.create_rectangle(150, 140, 816, 420,fill="#a80202",outline="white",width=6)
        sf.veg=PhotoImage(file="veg.png")
        sf.c.create_image(300,250,image=sf.veg)
        sf.vegbut=Button(sf.menuf2,text="Veg Pizza",cursor="hand2",fg="white",command=lambda:sf.vegpizza(sf.x),bg="black",bd=5,font=("default",18,'bold'))
        sf.vegbut.place(x=230,y=350)
        sf.nonveg=PhotoImage(file="Non.png")
        sf.c.create_image(630,250,image=sf.nonveg)
        sf.nonvegbut=Button(sf.menuf2,text="Non-Veg Pizza",cursor="hand2",fg="white",command=lambda:sf.nonvegpiz(sf.x),bg="black",bd=5,font=("default",18,'bold'))
        sf.nonvegbut.place(x=540,y=350)

        sf.menuf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()


#--  page 8------
    def vegpizza(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        sf.scr.title("Python Tkinter GUI application")
        #sf.scr.resizable(False, False)
        sf.vegf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.vegf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.c.create_image(513,75,image=sf.logo)
        sf.home=Button(sf.vegf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.vegf1.pack(fill=BOTH,expand=1)

        sf.vegf2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.vegf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(500,280,image=sf.logo1)
        sf.log=Label(sf.vegf2,text="VEG PIZZA",bg="#9db1f2",font=("algerian",22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(200, 40, 826, 475,fill="#a80202",outline="white",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # pizza 1
        sf.c.create_rectangle(205, 45, 823, 150,width=2)
        sf.delu=PhotoImage(file="deluxe.png")
        sf.c.create_image(270,95,image=sf.delu)
        sf.c.create_text(550,60,text="Deluxe Veggie",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,90,text="$10/$12/$8",fill="#ff3838",font=("default",17,'bold'))
        #ch1=sf.check(sf.vegf2,100)
        sf.v1=IntVar()
        sf.C11=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v1)
        sf.C11.place(x=400,y=80)
        sf.C12 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v1)
        sf.C12.place(x=500,y=80)
        sf.C13 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v1)
        sf.C13.place(x=600,y=80)
        sf.C11.select()
        sf.C11.deselect()    
        sf.C11.invoke()
        sf.c.create_text(450,130,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.vegf2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=510,y=120)
        sf.add1=Button(sf.vegf2,text="ADD",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=700,y=110)
        def addch1():
            if sf.v1.get()==10:
                ch1="Medium"
                pric1=10
            elif sf.v1.get()==20:
                ch1="Large"
                pric1=12
            else:
                ch1="Regular"
                pric1=8
            sf.addlist(["Deluxe Veggie",ch1,sf.q1.get(),pric1*int(sf.q1.get())])
            
        #pizza 2
        sf.c.create_rectangle(205, 150, 823, 257,width=2)
        sf.vag=PhotoImage(file="extravaganza.png")
        sf.c.create_image(270,200,image=sf.vag)
        sf.c.create_text(550,170,text="Veg Vaganza",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,200,text="$9/$11/$8",fill="#ff3838",font=("default",17,'bold'))
##        ch2=sf.check(sf.vegf2,220)
        sf.v2=IntVar()
        sf.C21=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v2)
        sf.C21.place(x=400,y=200)
        sf.C22 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v2)
        sf.C22.place(x=500,y=200)
        sf.C23 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v2)
        sf.C23.place(x=600,y=200)
        sf.C21.select()
        sf.C21.deselect()    
        sf.C21.invoke()
        sf.c.create_text(450,240,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.vegf2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=510,y=230)
        sf.add2=Button(sf.vegf2,text="ADD",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=700,y=220)
        def addch2():
            if sf.v2.get()==10:
                ch2="Medium"
                pric2=9
            elif sf.v2.get()==20:
                ch2="Large"
                pric2=11
            else:
                ch2="Regular"
                pric2=8

            sf.addlist(["Veg Vaganza",ch2,sf.q2.get(),pric2*int(sf.q2.get())])
        #pizza 3
        sf.c.create_rectangle(205, 257, 823, 364,width=2)
        sf.pep=PhotoImage(file="5-pepper-veg-pizza.png")
        sf.c.create_image(270,310,image=sf.pep)
        sf.c.create_text(550,270,text="5 Pepper",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,300,text="$8/$9/$6",fill="#ff3838",font=("default",17,'bold'))
        #ch3=sf.check(sf.vegf2,340)
        sf.v3=IntVar()
        sf.C31=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v3)
        sf.C31.place(x=400,y=300)
        sf.C32 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v3)
        sf.C32.place(x=500,y=300)
        sf.C33 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v3)
        sf.C33.place(x=600,y=300)
        sf.C31.select()
        sf.C31.deselect()    
        sf.C31.invoke()

        sf.c.create_text(450,345,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.vegf2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=510,y=335)

        sf.add3=Button(sf.vegf2,text="ADD",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=700,y=320)
        def addch3():
            if sf.v3.get()==10:
                ch3="Medium"
                pric3=8
            elif sf.v3.get()==20:
                ch3="Large"
                pric3=9
            else:
                ch3="Regular"
                pric3=6
            sf.addlist(["5 Pepper     ",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #pizza 4
        sf.c.create_rectangle(205, 364, 823, 471,width=2)
        sf.mag=PhotoImage(file="Margherit.png")
        sf.c.create_image(270,420,image=sf.mag)
        sf.c.create_text(550,390,text="Margherita",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,410,text="$7/$9/$5",fill="#ff3838",font=("default",17,'bold'))
        #ch4=sf.check(sf.vegf2,460)
        sf.v4=IntVar()
        sf.C41=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v4)
        sf.C41.place(x=400,y=410)
        sf.C42 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v4)
        sf.C42.place(x=500,y=410)
        sf.C43 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v4)
        sf.C43.place(x=600,y=410)
        sf.C41.select()
        sf.C41.deselect()    
        sf.C41.invoke()
        
        sf.c.create_text(450,450,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.vegf2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=510,y=440)
        
        sf.add4=Button(sf.vegf2,text="ADD",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=700,y=430)
        def addch4():
            if sf.v4.get()==10:
                ch4="Medium"
                pric4=7
            elif sf.v4.get()==20:
                ch4="Large"
                pric4=9
            else:
                ch4="Regular"
                pric4=5
            sf.addlist(["Margherita  ",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con=Button(sf.vegf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="black",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=0)
       
        sf.vegf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
        
##----page 9 ------
    
    def addlist(sf,q):
        if q[-2]!="0" and q[-2].isdigit():
            sf.cartlist.append(q)
            sf.amount=sf.amount+q[-1]
            messagebox.showinfo("Cart","Item Successfully added")
        else:
            messagebox.showinfo("Cart","Enter Valid Quantity to add")
        print(sf.cartlist,sf.amount)

#--  page 10------
    def nonvegpiz(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        sf.scr.title("Python Tkinter GUI application")
        #sf.scr.resizable(False, False)
        sf.vegf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.vegf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.c.create_image(513,75,image=sf.logo)
        sf.home=Button(sf.vegf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.vegf1.pack(fill=BOTH,expand=1)

        sf.vegf2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.vegf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(500,280,image=sf.logo1)
        sf.log=Label(sf.vegf2,text="VEG PIZZA",bg="#9db1f2",font=("algerian",22))
        sf.log.place(x=500,y=4)
        sf.c.create_rectangle(200, 40, 826, 475,fill="#a80202",outline="white",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # pizza 1
        sf.c.create_rectangle(205, 45, 823, 150,width=2)
        sf.delu=PhotoImage(file="Non-Veg_Supreme.png")
        sf.c.create_image(270,95,image=sf.delu)
        sf.c.create_text(550,60,text="Non-Veg Supreme",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,90,text="$10/$12/$8",fill="#ff3838",font=("default",17,'bold'))
        #ch1=sf.check(sf.vegf2,100)
        sf.v1=IntVar()
        sf.C11=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v1)
        sf.C11.place(x=400,y=80)
        sf.C12 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v1)
        sf.C12.place(x=500,y=80)
        sf.C13 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v1)
        sf.C13.place(x=600,y=80)
        sf.C11.select()
        sf.C11.deselect()    
        sf.C11.invoke()
        sf.c.create_text(450,130,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty1=Entry(sf.vegf2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty1.place(x=510,y=120)
        sf.add1=Button(sf.vegf2,text="ADD",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=700,y=110)
        def addch1():
            if sf.v1.get()==10:
                ch1="Medium"
                pric1=10
            elif sf.v1.get()==20:
                ch1="Large"
                pric1=12
            else:
                ch1="Regular"
                pric1=8
            sf.addlist(["Non-Veg Supreme",ch1,sf.q1.get(),pric1*int(sf.q1.get())])
            
        #pizza 2
        sf.c.create_rectangle(205, 150, 823, 257,width=2)
        sf.vag=PhotoImage(file="nonChicken_Tikka.png")
        sf.c.create_image(270,200,image=sf.vag)
        sf.c.create_text(550,170,text="Chicken Tikkaa",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,200,text="$9/$11/$8",fill="#ff3838",font=("default",17,'bold'))
##        ch2=sf.check(sf.vegf2,220)
        sf.v2=IntVar()
        sf.C21=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v2)
        sf.C21.place(x=400,y=200)
        sf.C22 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v2)
        sf.C22.place(x=500,y=200)
        sf.C23 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v2)
        sf.C23.place(x=600,y=200)
        sf.C21.select()
        sf.C21.deselect()    
        sf.C21.invoke()
        sf.c.create_text(450,240,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty2=Entry(sf.vegf2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=510,y=230)
        sf.add2=Button(sf.vegf2,text="ADD",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=700,y=220)
        def addch2():
            if sf.v2.get()==10:
                ch2="Medium"
                pric2=9
            elif sf.v2.get()==20:
                ch2="Large"
                pric2=11
            else:
                ch2="Regular"
                pric2=8

            sf.addlist(["Chicken Tikkaa",ch2,sf.q2.get(),pric2*int(sf.q2.get())])
        #pizza 3
        sf.c.create_rectangle(205, 257, 823, 364,width=2)
        sf.pep=PhotoImage(file="non-Chicken_Sausage.png")
        sf.c.create_image(270,310,image=sf.pep)
        sf.c.create_text(550,270,text="Chicken Sausage",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,300,text="$8/$9/$6",fill="#ff3838",font=("default",17,'bold'))
        #ch3=sf.check(sf.vegf2,340)
        sf.v3=IntVar()
        sf.C31=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v3)
        sf.C31.place(x=400,y=300)
        sf.C32 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v3)
        sf.C32.place(x=500,y=300)
        sf.C33 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v3)
        sf.C33.place(x=600,y=300)
        sf.C31.select()
        sf.C31.deselect()    
        sf.C31.invoke()

        sf.c.create_text(450,345,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty3=Entry(sf.vegf2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=510,y=335)

        sf.add3=Button(sf.vegf2,text="ADD",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=700,y=320)
        def addch3():
            if sf.v3.get()==10:
                ch3="Medium"
                pric3=8
            elif sf.v3.get()==20:
                ch3="Large"
                pric3=9
            else:
                ch3="Regular"
                pric3=6
            sf.addlist(["Chicken Sausage",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #pizza 4
        sf.c.create_rectangle(205, 364, 823, 471,width=2)
        sf.mag=PhotoImage(file="no-LoadedL.png")
        sf.c.create_image(270,420,image=sf.mag)
        sf.c.create_text(550,390,text="Chicken Peri",fill="#000000",font=("algerian",20))
        sf.c.create_text(730,410,text="$7/$9/$5",fill="#ff3838",font=("default",17,'bold'))
        #ch4=sf.check(sf.vegf2,460)
        sf.v4=IntVar()
        sf.C41=Radiobutton(sf.vegf2,text = "Medium",value=10,variable=sf.v4)
        sf.C41.place(x=400,y=410)
        sf.C42 = Radiobutton(sf.vegf2, text = "Large",value = 20, variable =sf.v4)
        sf.C42.place(x=500,y=410)
        sf.C43 = Radiobutton(sf.vegf2, text = "Regular",value = 30, variable =sf.v4)
        sf.C43.place(x=600,y=410)
        sf.C41.select()
        sf.C41.deselect()    
        sf.C41.invoke()
        
        sf.c.create_text(450,450,text="Quantity : ",fill="#000000",font=("default",12))
        sf.qty4=Entry(sf.vegf2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=510,y=440)
        
        sf.add4=Button(sf.vegf2,text="ADD",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=700,y=430)
        def addch4():
            if sf.v4.get()==10:
                ch4="Medium"
                pric4=7
            elif sf.v4.get()==20:
                ch4="Large"
                pric4=9
            else:
                ch4="Regular"
                pric4=5
            sf.addlist(["Chicken Peri",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        sf.con=Button(sf.vegf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="black",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=0)
       
        sf.vegf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
        

#--  page 13------
    def Address(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Pizza")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.addf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.addf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.out=Button(sf.addf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.out.place(x=1200,y=100)
        sf.addf1.pack(fill=BOTH,expand=1)

        sf.addf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.addf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.addf2,text="Address",fg="white",bg="#a80202",width=20,font=("default",27))
        sf.log.place(x=480,y=110)
        sf.c.create_rectangle(180,100,1186,450,fill="#a80202",outline="white",width=6)
        sf.lab1=Label(sf.addf2,text="City",bg="#a80202",font=("algerian",18))
        sf.lab1.place(x=190,y=200)
        sf.city=Entry(sf.addf2,bg="white",width=15,font=("default",18),bd=5)
        sf.city.place(x=430,y=200)
        sf.lab2=Label(sf.addf2,text="Locality",bg="#a80202",font=("algerian",18))
        sf.lab2.place(x=730,y=200)
        sf.loc=Entry(sf.addf2,bg="white",width=15,font=("default",18),bd=5)
        sf.loc.place(x=918,y=200)
        sf.lab3=Label(sf.addf2,text="Building Name",bg="#a80202",font=("algerian",18))
        sf.lab3.place(x=190,y=250)
        sf.buil=Entry(sf.addf2,bg="white",width=15,font=("default",18),bd=5)
        sf.buil.place(x=430,y=250)
        sf.lab4=Label(sf.addf2,text="House No.",bg="#a80202",font=("algerian",18))
        sf.lab4.place(x=730,y=250)
        sf.hou=Entry(sf.addf2,bg="white",width=15,font=("default",18),bd=5)
        sf.hou.place(x=918,y=250)
        sf.lab5=Label(sf.addf2,text="Landmark",bg="#a80202",font=("algerian",18))
        sf.lab5.place(x=190,y=300)
        sf.lan=Entry(sf.addf2,bg="white",width=15,font=("default",18),bd=5)
        sf.lan.place(x=430,y=300)
        sf.bc=Button(sf.addf2,text="Back",command=lambda:sf.Orderde(sf.x),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.addf2,text="Order Now",command=lambda:sf.orderpay(sf.x),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.city.delete(0,END)
            sf.loc.delete(0,END)
            sf.buil.delete(0,END)
            sf.hou.delete(0,END)
            sf.lan.delete(0,END)
        sf.cl=Button(sf.addf2,text="Clear",command=lambda:clear(sf),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.addf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

        
#--  page 14------
    def Orderde(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Python Tkinter GUI application")
        sf.scr.geometry("1366x768")
        sf.ordf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.ordf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.ordf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.ordf1.pack(fill=BOTH,expand=1)
        
        sf.ordf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.ordf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.ordf2,text="YOUR ORDER",bg="#9db1f2",font=("algerian",22))
        sf.log.place(x=450,y=4)
        sf.c.create_rectangle(250, 60, 800, 500,fill="#a80202",outline="white",width=6)
        sf.amt=sf.amount
        sf.text="Total : "+str(sf.amt)
        sf.tot=Label(sf.ordf2,text=sf.text,bg="#f2da9d",width=12,font=("algerian",22))
        sf.tot.place(x=900,y=250)
        if sf.x=="deli":
            sf.y=sf.Address
        if sf.x=="pick":
            sf.y=sf.orderpay
        sf.pay=Button(sf.ordf2,text="Pay",command=lambda:sf.y(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.pay.place(x=900,y=300)
        sf.exi=Button(sf.ordf2,text="Add more",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.exi.place(x=1000,y=300)
        sf.c.create_text(525,80,text="Items\tSize\tQty\tPrice",font=("algerian",18))
        sf.c.create_text(525,90,text="_______________________________________",font=("algerian",18))
        y=100
        for i in sf.cartlist:
            y+=30
            s=i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+str(i[3])
            sf.c.create_text(525,y,text=s,font=("default",16))
            
        sf.ordf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

 #-----  database-------               
    def logindatabase(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("pizza.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
        if list(x)[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In\nWelcome to MyPizzaStore")            
            sf.menulist("deli")

    def Regdatabase(sf):
        sf.credreg=sf.resultreg()
        sf.con=connect("pizza.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and mob=%r "%(sf.credreg[0],sf.credreg[5]))
        if list(x)[0][0]==0:
            if sf.credreg[0]=="" or sf.credreg[1]=="" or sf.credreg[2]=="" or sf.credreg[3]=="" or sf.credreg[5]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r)"%(sf.credreg[0],sf.credreg[1],sf.credreg[2],sf.credreg[3],sf.credreg[4],sf.credreg[5]))
                sf.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")

    def admindatabase(sf):
        sf.credadm=sf.resultadmin()
        sf.con=connect("pizza.db")
        sf.cur=sf.con.cursor()
        x=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credadm[0],sf.credadm[1]))
        # print(x)
        if list(x)[0][0]==0:
            if sf.credadm[0]=="" or sf.credadm[1]=="":
                messagebox.showinfo("Admin","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Admin","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Admin","You have Successfully Log In")            
            sf.adminmain()

    def adminorderdetail(sf):
        sf.credadmord=sf.resultadminorder()
        if sf.money!=0 and sf.credadmord[0]!="" and sf.credadmord[1]!="":
            if messagebox.askyesno("Pay","Want to make payment"):
                sf.con=connect("pizza.db")
                sf.cur=sf.con.cursor()
                od=[]
                try:
                    sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                except:
                    pass
                for i in sf.credadmord[3:]:
                    if i[-1]!="0":
                        od.append(i)
                a=sf.credadmord[0]
                b=sf.credadmord[1]
                print(a,b,str(sf.money),od)
                s="insert into orderdetail(name,mobile,money,orderdet) values(%r,%r,%r,%r)"%(a,b,str(sf.money),str(od))
                sf.cur.execute(s)
                sf.con.commit()
                messagebox.showinfo("Pay","Successfully Paid the amount")
        else:
            messagebox.showinfo("Pay","Enter Customer's Name and Mobile No  and  Order Something")
  
    def orderpay(sf,x):
        
        messagebox.showinfo("Pay","The order has been placed.")
        
x=Pizza()
x.main()
