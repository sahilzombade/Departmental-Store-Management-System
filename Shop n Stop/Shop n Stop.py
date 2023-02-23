import os
import platform
import mysql.connector
#Establishing a connection with MySQL and creating the required tables
myConnection=mysql.connector.connect(host="localhost",\
user="root",\
password="4814",\
database="stop_and_shop", \
use_pure=True)
print(myConnection)
mycursor=myConnection.cursor()
mycursor.execute('CREATE TABLE IF NOT EXISTS employees(emp_SNO int ,emp_name varchar(30),emp_dob date, emp_gender varchar(2), emp_zip int)')
mycursor.execute('CREATE TABLE IF NOT EXISTS customers(Cust_name varchar(30), Cust_email varchar(50), Cust_gender varchar(2))')
mycursor.execute('CREATE TABLE IF NOT EXISTS departmental_store(S_no int, Items varchar(100), Item_code varchar(100), price_per_item int, Quantity int , Discount int)')
mycursor.execute('CREATE TABLE IF NOT EXISTS orders(Sno int(2), item_name varchar(30), Quantity int(4), Price float(10,2),Inventory varchar(30))')

#Defining a function to Register Employee 

def RegisterEmployeeDetails():
 ED=[]
 
 empSNO=int(input("enter serial no"))
 ED.append(empSNO)
 empName=input("Enter Employee Name : ")
 ED.append(empName)
 empDOB=input("Enter Dob in YYYY-MM-DD Format : ")
 ED.append(empDOB)
 empGender=input("Enter employee's Gender : ")
 ED.append(empGender)
 empZipcode=input("Enter employee' zipcode : ")
 ED.append(empZipcode)
 employee=(ED)
 sql="insert into employees \
 (emp_SNO,emp_name,emp_dob,emp_gender,emp_zip) values \
 (%s,%s,%s,%s,%s)"
 mycursor.execute(sql,employee)
 myConnection.commit()
 print("You Have Been Succesfully Registered")
 print(empName)

#defining a function to View Employee Details
 
def ViewEmployeeDetails():
 
     sql="select * from employees"
     mycursor.execute(sql)
     res=mycursor.fetchall()
     print("The Employee Details are as Follows")
     print("(emp_SNO,emp_name,emp_dob,emp_gender,emp_zip)")
     for x in res:
         print(x)

#defining a function to Delete an Employee
def DeleteEmployee():
    n1=input("Enter the SNO of the Employee to be deleted : ")
    sql="DELETE FROM employees WHERE emp_SNO  = %s"
    mycursor.execute(sql %(n1))
    myConnection.commit()

    print("Editing Done : ")
    print("After correction the record is : ")
    sql="select * from employees"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    print("The Employee Details are as Follows")
    print("(emp_SNO,emp_name,emp_dob,emp_gender,emp_zip)")
    for x in res:
        print(x)

#defining a function to Register a new customer
    
def RegisterCustomerDetails():
    CD=[]
    Cust_name=input("Enter Customer Name to add : ")
    CD.append(Cust_name)
    Cust_email=input("Enter Customer email id : ")
    CD.append(Cust_email)
    Cust_gender=input("Enter Customer gender : ")
    CD.append(Cust_gender)
    customer=(CD)
    sql="insert into customers (Cust_name,Cust_email,Cust_gender) values (%s,%s,%s)"
    mycursor.execute(sql,customer)
    myConnection.commit()

#defining a function to view customer details
    
def ViewCustomersDetails():
    print("Enter The Customer Name")
    custName=input("Enter the Customer name for the Customer to be viewed : ")
    sql="select * from customers where Cust_name like %s"
    rl=(custName,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    if res==None:
        print("Record not Found . . . ")
        return
    print("The details of the customers are : " )
    print("(Cust_name,Cust_email,Cust_gender)")
    for x in res:
        print(x)
#defining a function to add order

def RegisterOrderDetails():
    OD=[]
    itemName=input("Enter Item Name to add : ")
    OD.append(itemName)
    itemQuantity=input("Enter Item Quantity : ")
    OD.append(itemQuantity)
    itemPrice=input("Enter Item Price : ")
    OD.append(itemPrice)
    inventoryDetail=input("Enter Inventory details : ")
    OD.append(inventoryDetail)
    order=(OD)
    sql="insert into orders (Item_name,Quantity,Price,Inventory) values (%s,%s,%s,%s)"
    mycursor.execute(sql,order)
    myConnection.commit()

#defining a function to view order details
# this includes viewing by different search options like search by item, qty etc
    
def ViewOrderDetails():
    print("Select the search criteria to View Order Details : ")
    print("1. Item")
    print("2. Quantity")
    print("3. Price")
    print("4. Inventory")
    print("5. To View All Records")
    ch=int(input("Enter the choice : "))
    if ch==1 :
        s=input("Enter Item Name to Be Searched For")
        rl=(s,)
        sql="select * from orders where Item_name like %s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Quantity to Be Searched For")
        rl=(s,)
        sql="select * from orders where Quantity = %s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=input("Enter Price to Be Searched For")
        rl=(s,)
        sql="select * from orders where Price=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter Inventory to Be Searched For")
        rl=(s,)
        sql="select * from orders where Inventory like %s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from orders"
        mycursor.execute(sql)
    res=mycursor.fetchall()
    print("The Order Details are as Follows")
    print("(SNo,Item_Name,Quantity,Price,Inventory)")
    for x in res:
        print(x)

# a code for billing system defined as a function to access the bill counter

def BillingSystem():
    k=0
    print("welcome to STOP AND SHOP")
    while k<1:
        print()
        print("WELCOME TO THE Billing system")
        print()
        print("1.To enter only one record in the database")
        print("2.To enter mutiple records in the database")
        print("3.To update the database")
        print("4.To delete an item from the database")
        print("5.To print the bill")
        print("6.To delete the bill")
        print("7.To exit the program")

        numo=int(input("Enter your choice 1/2/3/4/5/6/7 according to the task you want to perform: "))

        if numo==1: #To enter only one record in the database
            print("Enter the value in order of S.No, Items, Item Code, Price Per Item, Quantity and Discount")
            i=0
            row=[]
            elemento=["S.No","ITEM","ITEM CODE","PRICE PER ITEM","QUANTITY","DISCOUNT"]
            while i<6:
                if i!=1 and i!=2: 
                    element=input("Enter the "+elemento[i])
                else:
                    element=input("Enter the "+elemento[i])
                i+=1
                row.append(element)
            sql="INSERT INTO departmental_store VALUES(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,row)
            myConnection.commit()

        elif numo==2: #To enter multiple records in the database
            n=int(input("Enter the number of records you want to put "))
            j=1
            print("Enter the value in order of S.No, Items, Item Code, Price Per Item, Quantity and Discount")
            while j<n+1:
                i=0
                row=[]
                elemento=["S.No","ITEM","ITEM CODE","PRICE PER ITEM","QUANTITY","DISCOUNT"]
                while i<6:
                    if i!=1 and i!=2:
                        element=input("Enter the "+elemento[i])
                    else:
                        element=input("Enter the "+elemento[i])
                    i+=1
                    row.append(element)
                print()
                sql="INSERT INTO departmental_store VALUES(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,row)
                myConnection.commit()
                j=j+1

        elif numo==3: #To update the database
            print()
            print("1.To update the S.No")
            print("2.To update the Item name")
            print("3.To update the item code")
            print("4.To update the Price Per Item")
            print("5.To update the Quantity of the item")
            print("6.To update the Discount on the items")
            print()
            
            ent=int(input("Enter your choice 1/2/3/4/5/6 for what you want to update: "))

            if ent==1: #To update the S.no
                n1=int(input("Enter the SNO you want to set"))
                n2=int(input("Enter the reference SNO you want to update"))
                sql="UPDATE departmental_store SET S_NO= %s WHERE S_NO= %s"
                mycursor.execute(sql,(n1,n2))
                myConnection.commit()
                print("S.No updated successfully!")

            elif ent==2: #To update the Item name
                n1=input("Enter the ITEM you want to set")
                n2=input("Enter the reference ITEM you want to update")
                sql="UPDATE departmental_store SET ITEMS= %s WHERE ITEMS= %s"
                mycursor.execute(sql,(n1,n2))
                myConnection.commit()
                print("ITEM updated successfully!")

            elif ent==3: #To update the Item code
                n1=input("Enter the ITEM CODE you want to set")
                n2=input("Enter the reference ITEM CODE you want to update")
                sql="UPDATE departmental_store SET ITEM_CODE= %s WHERE ITEM_CODE= %s"
                mycursor.execute(sql,(n1,n2))
                myConnection.commit()
                print("ITEM_CODE updated successfully!")

            elif ent==4: #To update the price per item
                n1=input("Enter the Price per item you want to set: ")
                n2=input("Enter the reference Price Per Item you want to update: ")
                sql="UPDATE departmental_store SET PRICE_PER_ITEM= %s WHERE PRICE_PER_ITEM= %S"
                mycursor.execute(sql,(n1,n2))
                myConnection.commit()
                print("PRICE_PER_ITEM updated successfully")

            elif ent==5: #To update the quantity of an item
                n1=input("Enter the QUANTITY you want to set")
                n2=input("Enter the reference QUANTITY you want to update")
                sql="UPDATE departmental_store SET QUANTITY= %s WHERE QUANTITY= %s"
                mycursor.execute(sql,(n1,n2))
                myConnection.commit()
                print("QUANTITY updated successfully!")

            elif ent==6: #To update the discount on an item
                n1=input("Enter the DISCOUNT you want to set")
                n2=input("Enter the reference DISCOUNT you want to update")
                sql="UPDATE departmental_store SET DISCOUNT= %s WHERE DISCOUNT= %s"
                mycursor.execute(sql,(n1,n2))
                myConnection.commit()
                print("DISCOUNT updated successfully!")

            else:
                print("Incorrect input")
        
        elif numo==4: #To delete an item from the database
            print()
            print("1.To delete an entry using S.NO as reference")
            print("2.To delete an entry using ITEMS as reference")
            print("3.To delete an entry using ITEMCODE as reference")
            print("4.To delete an entry using PRICE as reference")
            print("5.To delete an entry using QUANTITY as reference")
            print("6.To delete an entry using DISCOUNT as reference")
            print()
            entt=int(input("Enter your choice 1/2/3/4/5/6 to delete an entry: "))

            if entt==1: #To delete an entry by taking S.no as reference
                n1=int(input("Enter the S.NO as reference"))
                sql="DELETE FROM departmental_store WHERE S_NO = %s"
                mycursor.execute(sql %(n1))
                myConnection.commit()

            elif entt==2: #To delete an entry by taking Item as reference
                n1=input("Enter the ITEM as reference")
                sql="DELETE FROM departmental_store WHERE ITEMS= %s"
                mycursor.execute(sql %(n1))
                myConnection.commit()

            elif entt==3: #To delete an entry by taking Itemcode as reference
                n1=input("Enter the ITEMCODE as reference")
                sql="DELETE FROM departmental_store WHERE ITEM_CODE= %s"
                mycursor.execute(sql%(n1))
                myConnection.commit()

            elif entt==4: #To delete an entry by taking Price as reference
                n1=int(input("Enter the PRICE as reference"))
                sql="DELETE FROM departmental_store WHERE PRICE_PER_ITEM= %s"
                mycursor.execute(sql %(n1))
                myConnection.commit()

            elif entt==5: #To delete an entry by taking Quantity as reference
                n1=int(input("Enter the QUANTITY as reference"))
                sql="DELETE FROM departmental_store WHERE QUANTITY= %s"
                mycursor.execute(sql %(n1))
                myConnection.commit()

            elif entt==6: #To delete an entry by taking Discount as reference
                n1=int(input("Enter the DISCOUNT as reference"))
                sql="DELETE FROM departmental_store WHERE DISCOUNT= %s"
                mycursor.execute(sql %(n1))
                myConnection.commit()

            else:
                print("Incorrect input")

        elif numo==5: #To print the bill


            import itertools

            mycursor.execute("SELECT PRICE_PER_ITEM FROM departmental_store")
            hello=[]
            for m in mycursor:
                hello.append(m)
            hellos=[]
            for mn in hello:
                for hf in mn:
                    hellos.append(hf)
            mycursor.execute("SELECT QUANTITY FROM departmental_store")
            hello1=[]
            for m in mycursor:
                hello1.append(m)
            hellos2=[]
            for mnh in hello1:
                for hfg in mnh:
                    hellos2.append(hfg)

            mycursor.execute("SELECT DISCOUNT FROM departmental_store")
            hello2=[]
            for fg in mycursor:
                hello2.append(fg)
            hellos3=[]
            for mng in hello2:
                for hfh in mng:
                    hellos3.append(hfh)
            #print(hellos)
            #print(hellos2)
            #print(hellos3)    

            sums=0
            for (v,y,hj) in zip (hellos,hellos2,hellos3):
                sums=sums+(v*y-(v*y*hj/100))
            print(sums)



            mycursor.execute("SELECT * FROM departmental_store")
            fields=[('S.NO',"ITEMS","ITEM CODE","PRICE PER ITEM","QUANTITY","DISCOUNT")]
            lis=[]
            for i in mycursor:
                lis.append(i)
            for j in lis:
                fields.append(j)
            def BILL(fields):
                 output= " __________________________________________________________________________________________\n"
                 for item in fields[0]:
                  
                     output+="|   " + str(item) + "   "

                 output+="\n|------------------------------------------------------------------------------------------"

                 return output
            print(BILL(fields))
                

            
            for item in lis:
                print("|",item[0]," "*(7-len(str(item[0]))),"|",
                item[1]," "*(8-len(item[1])),"|",
                item[2]," "*(12-len(item[2])),"|",
                item[3]," "*(17-len(str(item[3]))),"|",
                item[4]," "*(11-len(str(item[4]))),"|",
                item[5]," "*(11-len(str(item[5]))),"|")

            print("|------------------------------------------------------------------------------------------")
            print("| TOTAL AMOUNT :",sums)
            print("| (Inc. of all taxes)")
            print("|")
            print("|")
            print("| Thank you for shopping from our store ")

            print("|__________________________________________________________________________________________")


        elif numo==6: #To delete the whole bill
            mycursor.execute("TRUNCATE TABLE departmental_store")
            myConnection.commit()
            print("Bill successfully deleted")

        elif numo==7: #To end the program
            k+=1
            print("Program is ended successfully")

        else:
            print("Invalid choice")
            
# defining a main menu which'll pop up as soon as the code runs
# all the functions defined above are being called by a loop here.
#this will work as a menu driven program

def MainMenu():
    print("*********************************************")
    print("*         WELCOME TO STOP AND SHOP          *")
    print("*********************************************")
    print("1 : To Register Employee")
    print("2 : To View Employee Details ")
    print("3 : To Delete Employee Record ")
    print("4 : To Add Customers ")
    print("5 : To View Customers")
    print("6 : To Add Orders")
    print("7 : To View Orders")
    print("8 : To Go To Billing System")
    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("You Had Entered Wrong Choice")
    else:
        print("\n")
        if(userInput == 1):
            RegisterEmployeeDetails()
        elif (userInput==2):
            ViewEmployeeDetails()
        elif (userInput==3):
            DeleteEmployee()
        elif (userInput==4):
            RegisterCustomerDetails()
        elif (userInput==5):
            ViewCustomersDetails()
        elif (userInput==6):
            RegisterOrderDetails()
        elif (userInput==7):
            ViewOrderDetails()
        elif (userInput==8):
            BillingSystem()
        else:
            print("Enter correct choice. . . ")

#after the entire code runs this'll ask that to run it again or exit
MainMenu()
def AskChoiceAgain():
    AksChcRun = input("\nWant To Run Again Y/n: ")
    while(AksChcRun.lower() == 'y'):
        if(platform.system() == 'darwin'):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MainMenu()
        AksChcRun = input("\nWant To Run Again Y/n: ")
AskChoiceAgain()
