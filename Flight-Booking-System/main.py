
"""
Flight Booking System

Author: Siddhant Wadher
Description:
    This script is a terminal-based flight booking system that supports:
    - Flight search
    - Booking with seat allocation
    - Payment simulation
    - User authentication

Database: MySQL
Modules Used: mysql.connector, tabulate, random, sys
"""

import mysql.connector as mys

mycon = mys.connect(host="localhost", user="root", passwd="siddhant@3101")
mycursor = mycon.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS airlines")
mycon.commit()


mycon=mys.connect(host="localhost",user="root",passwd="siddhant@3101",database="airlines")
mycursor=mycon.cursor(buffered=True)





import random

import sys

import tabulate                                              
headers1 =["FLIGHTNO","FROM","TO","JOURNEY TIME","FARE(IN INR)","AIRLINE"]
headers2=["FLIGHTNO","FROM","TO","JOURNEY TIME","AIRLINE"]
headers3 = ["PASSENGER NO.","PASSENGER NAME","GENDER","AGE","SEAT"]

print(">-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->-|->")
print("                                    WELCOME TO ONLINE FLIGHT BOOKING SYSTEM        ")
print("<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<-|-<")
print()

query = "create table if not exists flightbook(flightno int(100),bcity varchar(100),dcity varchar(20), jtime time,fare int(100),airline varchar(100))"
mycursor.execute(query)
   
mycursor.execute("INSERT INTO flightbook VALUES ('1','Raipur','Mumbai','10:00:00','11000','Indigo'),('2','Raipur','delhi','20:00:00','14000','Vistara'),('3','mumbai','delhi','01:00:00','5000','Indigo'),('4','delhi','kolkata','21:00:00','8500','SpiceJet'),('5','delhi','chennai','23:00:00','20000','AirIndia'),('6','delhi','paris','07:00:00','40000','Etihad Airways'),('7','delhi','Dubai','16:00:00','30000','Emirates'),('8','delhi','NewYork','19:00:00','46000','Qatar Airways'),('9','mumbai','Tokyo','00:00:00','68000','Akasa Air'),('10','mumbai','Mauritius','13:00:00','35000','Emirates')")
mycon.commit()

def add():#to add flights in database
    
    print("---------------------------------------------------------------------------------------------------------------------")
    query = "create table if not exists flightbook(flightno int(100),bcity varchar(100),dcity varchar(20), jtime time,fare int(100),airline varchar(100))"
    mycursor.execute(query)
   
    try:
      flightno = int(input("ENTER THE FLIGHT NUMBER:"))
      bcity = input("ENTER THE BOARDING CITY:")
      dcity = input("ENTER THE DESTINATION CITY:")
      jtime = input("ENTER THE JOURNEY TIME:")
      fare = int(input("ENTER THE FARE OF THE FLIGHT:"))
      airline = input("ENTER THE NAME OF THE AIRLINE:")
      q="insert into flightbook values({0},'{1}','{2}','{3}',{4},'{5}')".format(flightno,bcity,dcity,jtime,fare,airline)
      mycursor.execute(q)
      mycon.commit()
      print()
      print("FLIGHT ADDED TO DATABASE")
      print("---------------------------------------------------------------------------------------------------------------------")
    except:      
      print("---------------------------------------------------------------------------------------------------------------------")
      print("FLIGHT WITH FLIGHT NUMBER",flightno,"ALREADY EXISTS IN DATABASE!!!")
      print("---------------------------------------------------------------------------------------------------------------------")
      ans1=input("WANT TO ADD MORE FLIGHTS?(Y/N):")
      if ans1.lower()=="y":
          add()
      else:
          start()

def login():
    print("---------------------------------------------------------------------------------------------------------------------")     
    print("1-->SIGN UP")
    print("2-->SIGN IN")
    print()

    n=int(input("CHOOSE FROM THE FOLLOWING OPTIONS(1 OR 2):"))
    print("---------------------------------------------------------------------------------------------------------------------")
    query = "create table if not exists user_detail(USERNAME varchar(100),EMAIL_ADDRESS varchar(100) primary key,PASSWORD varchar(20))"
    mycursor.execute(query)
    if n==1:
     uname = input("ENTER YOUR USERNAME:")
     email = input("ENTER YOUR EMAIL:")
     pword = input("ENTER YOUR PASSWORD:")
     try:
        query="insert into user_detail values('{0}','{1}','{2}')".format(uname,email,pword)
        mycursor.execute(query)
        mycon.commit()
        print("YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED....")
        print("---------------------------------------------------------------------------------------------------------------------")
        login()
     except:
        print()
        print("THIS ACCOUNT ALREADY EXISTS!!!")
        start()
    elif n==2:
        email = input("ENTER YOUR EMAIL:")
        pword = input("ENTER YOUR PASSWORD:")
        query="select * from user_detail where EMAIL_ADDRESS= '{EMAIL_ADDRESS}' and PASSWORD='{PASSWORD}'".format(EMAIL_ADDRESS=email,PASSWORD=pword)
        mycursor.execute(query)
        data=mycursor.fetchall()
        nrec=mycursor.rowcount
        
        print("LOGIN SUCCESSFUL...")
        print("---------------------------------------------------------------------------------------------------------------------")
        start()   
    else:
        print()

        print("LOGIN FAILED --> PLEASE ENTER THE CORRECT EMAIL AND PASSWORD")
        login()
                
    
def start():
    print("1-->SEARCH FLIGHTS")
    print("2-->BOOK FLIGHTS")
    print("3-->ADD FLIGHTS TO THE DATABASE")
    print("4-->EXIT")
    print()
    n=int(input("CHOOSE FROM THE FOLLOWING OPTIONS(1,2,3 OR 4):"))      
    if n==1:
       print("---------------------------------------------------------------------------------------------------------------------") 
       a=input("ENTER YOUR BOARDING CITY:")           
       b=input("ENTER YOUR DESTINATION CITY:")             
       print()
       query="select * from flightbook where bcity= '{}' and dcity='{}'".format(a,b)
       mycursor.execute(query)
       data=mycursor.fetchall()
       nrec=mycursor.rowcount                         
       list1=[]
       if nrec!=0:
            print(nrec,"FLIGHTS FOUND")
            for i in data:
                  list1.append(i)
            print(tabulate.tabulate(list1,headers=headers1,tablefmt="grid"))
            print("---------------------------------------------------------------------------------------------------------------------")      
       else:
                 print()
                 print("FLIGHTS NOT FOUND!!!")
                 print()
                 print("--------------------------------------------------------------------------------------------------------------")
    elif n==2:
      print("---------------------------------------------------------------------------------------------------------------------")
      a=input("ENTER YOUR BOARDING CITY:")           
      b=input("ENTER YOUR DESTINATION CITY:")            
      print()
      query="select * from flightbook where bcity= '{}' and dcity='{}'".format(a,b)
      mycursor.execute(query)
      data=mycursor.fetchall()
      nrec=mycursor.rowcount                             
      list1=[]
      if nrec!=0:
           print(nrec,"FLIGHTS FOUND")
           for i in data:
               list1.append(i)
           print(tabulate.tabulate(list1,headers=headers1,tablefmt="grid"))
      else:
           print("FLIGHTS NOT FOUND...")
           print("---------------------------------------------------------------------------------------------------------------------")
           start()
      print()
      print("PLEASE PROVIDE US THE FOLLOWING DETAILS OF THE FLIGHT YOU WANT TO BOOK")
      fno= int(input("ENTER THE FLIGHT NO:"))
      query="select * from flightbook where flightno=%s"%(fno,)
      mycursor.execute(query)
      data=mycursor.fetchall()
      list3=[]
      if data!=None:
           list3.append(data)
           print(tabulate.tabulate(list3,headers=headers1,tablefmt="grid"))
           print()
           ans2=input("ARE YOU SURE YOU WANT TO BOOK THIS FLIGHT?(Y/N):")
           print()
           if ans2.lower()=="y":
               query="drop table if exists passengers"
               mycursor.execute(query) 
               query = "create table passengers(PASSENGERNO int, PASSENGER_NAME varchar(100),GENDER varchar(20),AGE int,SEAT varchar(20))"
               mycursor.execute(query) 
               print("PLEASE PROVIDE US THE FOLLOWING PERSONAL DETAILS")
               np = int(input("NUMBER OF PASSENGERS:"))
               print()
               for i in range(1,np+1):
                     print("GIVE THE DETAILS OF PASSENGER",i)
                     passengerno =i
                     name = input("ENTER THE NAME OF THE PASSENGER:")
                     gender =input("ENTER THE GENDER OF THE PASSENGER:")
                     age = int(input("ENTER THE AGE OF THE PASSENGER:"))
                     s1= random.randint(1,30)
                     s2=random.randint(0,5)
                     list=["A","B","C","D","E","F"]
                     seat = str(s1)+str(list[s2])        
                     query="insert into passengers values({0},'{1}','{2}',{3},'{4}')".format(passengerno,name,gender,age,seat)
                     mycursor.execute(query)
                     mycon.commit()
                     print()
               ddate = input("ENTER YOUR DEPARTURE DATE(DD-MM-YYYY):")
               dday = input("ENTER THE DAY OF DEPARTURE:")
               query="select fare from flightbook where flightno=%s"%(fno,)
               mycursor.execute(query)
               data=mycursor.fetchone()
               if data!=None:
                    tfare = np*data[0]
                    print("---------------------------------------------------------------------------------------------------------------------")
                    print("YOUR NET FARE OF ",np,"PASSENGERS IS:","Rs",tfare)
                    print("---------------------------------------------------------------------------------------------------------------------")
                    print()
                    ans3 = input("PROCEED FOR PAYMENT?(Y/N):")
                    print()
                    if ans3.lower()=="y":
                        print("SELECT YOUR MODE OF PAYMENT")
                        print("1-->CREDIT AND DEBIT CARDS")
                        print("2-->eWALLETS")
                        print("3-->BANK TRANSFER")
                        print()
                        n=int(input("CHOOSE FROM THE FOLLOWING OPTIONS(1,2 OR 3):"))
                        print()
                        if n==1:
                              cardno = int(input("ENTER YOUR CARD NUMBER:"))
                              print("WAIT FOR A MOMENT...")
                              print()
                              print("PAYMENT OF RS",np*data[0],"DONE SUCCESFULLY")
                              print("YOUR FLIGHT HAS BEEN BOOKED..")
                        elif n==2:
                              mno = int(input("ENTER YOUR MOBILE NUMBER:"))
                              print("WAIT FOR A MOMENT...")
                              print()
                              print("PAYMENT OF RS",np*data[0],"DONE SUCCESFULLY")
                              print("YOUR FLIGHT HAS BEEN BOOKED..")
                        elif n==3:
                              ano = int(input("ENTER YOUR ACCOUNT NUMBER:"))
                              print("WAIT FOR A MOMENT...")
                              print()
                              print("PAYMENT OF RS",np*data[0],"DONE SUCCESFULLY")
                              print("YOUR FLIGHT HAS BEEN BOOKED..")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("1-->PRINT TICKET")
                        print("2-->CANCEL BOOKING")
                        print("3-->RETURN TO HOMESCREEN")
                        print()
                        n=int(input("CHOOSE FROM THE FOLLOWING OPTIONS(1,2 OR 3):"))
                        print()
                        if n==1:
                                    print("*********************************************************************************************************************")
                                    print("                                              HAVE A NICE TRIP!                                                     ")     
                                    print("FLIGHT DETAILS")
                                    q2=" select flightno,bcity,dcity, jtime, airline from flightbook where flightno=%d"%(fno)
                                    mycursor.execute(q2)
                                    data=mycursor.fetchone()
                                    list4=[]
                                    if data!=None:
                                         list4.append(data)
                                    print(tabulate.tabulate(list4,headers=headers2,tablefmt="grid"))
                                    print("PASSENGERS DETAILS")
                                    query = "select * from passengers".format(passengerno,name,gender,age)
                                    mycursor.execute(query)
                                    data=mycursor.fetchall()
                                    nrec=mycursor.rowcount
                                    list5=[]
                                    if nrec!=0:
                                       for i in data:
                                             list5.append(i)
                                    print(tabulate.tabulate(list5,headers=headers3,tablefmt="grid"))
                                    print("DATE AND DAY OF DEPARTURE:",ddate,"/",dday)
                                    hr= random.randint(1,23)
                                    min = random.randint(10,59)
                                    if hr<12:
                                        print("BOARDING TIME:",hr,":",min,"AM IST")
                                    else:
                                        print("TIME OF FLIGHT:",hr,":",min,"PM IST")
                                    print("TOTAL AMOUNT PAID : Rs",tfare)
                                    print("*********************************************************************************************************************")
                                    print("---------------------------------------------------------------------------------------------------------------------")
                        elif n==2:
                                    print("---------------------------------------------------------------------------------------------------------------------")
                                    for i in range(1,np+1):
                                       query="drop table if exists passengers"
                                       mycursor.execute(query) 
                                    print("YOUR BOOKING HAS BEEN CANCELED...")
                                    print("!!!YOU WILL GET THE REFUND OF YOUR MONEY IN DUE COURSE OF TIME!!!")
                                    print("---------------------------------------------------------------------------------------------------------------------")
                                    start()
                        elif n==3:
                                    print("---------------------------------------------------------------------------------------------------------------------")
                                    print("                               THANK YOU FOR CHOOSING US TO BOOK YOUR FLIGHTS                                        ")
                                    print("---------------------------------------------------------------------------------------------------------------------")
                                    start()
 
                    else:
                         print("---------------------------------------------------------------------------------------------------------------------")
                         start()                      
           else:
                  print("---------------------------------------------------------------------------------------------------------------------")
                  start()
    elif n==3: 
     add()


    elif n==5:
        admin()
    else:
        print("---------------------------------------------------------------------------------------------------------------------")
        sys.exit()              

login()
start()
start()











