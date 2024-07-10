import mysql.connector as mys
from datetime import datetime, date

mycon = mys.connect(host='localhost', user='root', passwd='root', database='library')
if mycon.is_connected():
    print("\n\nSUCCESFULLY CONNECTED TO DATABASE")
mycur = mycon.cursor()


def check(idn):
    q = "select ID from membership"
    mycur.execute(q)
    rs = mycur.fetchall()
    for i in rs:
        if (idn == i[0]):
            return 1


def exct(query):
    mycur.execute(query)
    mycon.commit()


def tryInt():
    while True:
        try:
            n = int(input(' '))
        except ValueError:
            print("Invalid Data Type\nPlease Enter again:", end='')
            continue
        else:
            return n


def admin():
    while True:
        cha = input("\n\nEnter choice:\na.Create Membership\nb.Delete membership\nc.Update membership\nd.Go back to menu\n")
        if (cha == 'a'):
            print("\nEnter the details:")
            print("ID No.:", end='')
            idno = tryInt()
            ch = check(idno)
            if (ch == 1):
                print("ID No. already exists")
            else:
                name = input("Name: ")
                print("Phone Number:", end='')
                ph = tryInt()
                email = input("Email ID: ")
                add = input("Address: ")
                q = "insert into MEMBERSHIP values({0},'{1}',{2},'{3}','{4}')".format(idno, name, ph, email, add)
                exct(q)
                print("\nMEMBERSHIP SUCCESFULLY CREATED")
                q = "select * from membership where id={}".format(idno)
                mycur.execute(q)
                rs = mycur.fetchall()
                print("Membership ID:", rs[0][0], "\nName:", rs[0][1], "\nPh. No.:", rs[0][2], "\nEmail ID:", rs[0][3],
                      "\nAddress:", rs[0][4], "\n")
                print('-' * 50)
        if (cha == 'b'):
            print("\nEnter ID no. of the member to be deleted:", end='')
            idno = tryInt()
            ch = check(idno)
            if (ch == 1):
                yn = input("Are you sure you want to delete? (yes/no): ")
                if (yn == 'no'):
                    print("DELETION CANCELLED")
                elif (yn == 'yes'):
                    q = "delete from MEMBERSHIP where ID={}".format(idno)
                    exct(q)
                    print("\nMEMBERSHIP SUCCESSFULLY DELETED")
                    print('-' * 50)
            else:
                print("Membership not found")
        if (cha == 'c'):
            print("\nEnter ID no. of the member to be updated:", end='')
            idno = tryInt()
            ch = check(idno)
            if (ch == 1):
                detail = input("Enter the details to be changed (Name,PhNo,Email,Address): ")
                dt = detail.split(',')
                for d in dt:
                    if (d == 'Name'):
                        new = input("Enter new Name: ")
                        q = "update membership set Name='{1}' where ID={2}".format(d, new, idno)
                    elif (d == 'PhNo'):
                        print("Enter new PhNo:", end='')
                        new = tryInt()
                        q = "update membership set PhNo={1} where ID={2}".format(d, new, idno)
                    elif (d == 'Email'):
                        new = input("Enter new Email: ")
                        q = "update membership set Email='{1}' where ID={2}".format(d, new, idno)
                    elif (d == 'Address'):
                        new = input("Enter new Address: ")
                        q = "update membership set Address='{1}' where ID={2}".format(d, new, idno)
                    exct(q)
                print("\nSUCCESSFULLY UPDATED")
                print('-' * 50)
                q = "select * from membership where id={}".format(idno)
                mycur.execute(q)
                rs = mycur.fetchall()
                print("Membership ID:", rs[0][0], "\nName:", rs[0][1], "\nPh. No.:", rs[0][2], "\nEmail ID:", rs[0][3],
                      "\nAddress:", rs[0][4], "\n")
            else:
                print("Membership Not Found")
            print("_" * 50, "\n")
        if (cha == 'd'):
            print("_" * 50)
            break


def user(idn):
    while True:
        cha = input("\n\nEnter choice:\na.Borrow a book\nb.Return book\nc.Go back to menu\n")
        if (cha == 'a'):
            q = "select name from membership where id={}".format(idn)
            mycur.execute(q)
            dt = mycur.fetchone()
            q = "select * from book where not Quantity=0"
            mycur.execute(q)
            r = mycur.fetchall()
            print("LIST OF BOOKS AVAILABLE:")
            for i in r:
                print(i[0], ". ", i[1], " - ", i[2], sep='')
                print()#TILL HERE -DISPLAYING OF BOOKS
            n = int(input("\nEnter number of books to be borrowed: "))
            b = list()
            slnos=list()
            for x in range(0, n):
                g = int(input("Enter the serial number of the book to be borrowed: "))
                q = "select Bookname,Quantity,SlNo from book where SlNo={}".format(g)
                mycur.execute(q)
                r = mycur.fetchone()
                slnos.append(r[2])
                if (r != None):
                    q = "select Book_borrowed from borrow where ID={} and Book_borrowed='{}'".format(idn,r[0])
                    mycur.execute(q)
                    e = mycur.fetchall()

                    count = len(e)

                    if (count >= 1):
                        print("Max limit per customer reached")
                    else:
                        b.insert(x, r[0])
                        q = "Update book set Quantity={} where SlNo={}".format((r[1] - 1), g)
                        exct(q)
                else:
                    print("Book not available\n")

            now = datetime.now()
            d = now.strftime('%Y-%m-%d')

            print("\n\nMembership ID:", idno, "\t\tDate:", d, "\nName:", dt[0], "\nBooks Borrowed:")
            for x in range(0, len(b)):
                q = "insert into borrow values ({},'{}','{}',{})".format(idno, b[x], d, slnos[x])
                exct(q)
                print("\t", b[x])
            if n>0:
                print("Please return the book(s) within 30 days, after which a fine of Rupees 10, per day, will be imposed\n\n")
               
            print('_' * 75)
        if (cha == 'b'):#Returning
            q = "select Book_Borrowed, date_of_borrowing,SlNo from borrow where id={}".format(idno)
            mycur.execute(q)
            b = mycur.fetchall()
            for i in b:
                n=36-len(i[0])#Used for allignment
                m=str(i[2])
                k=6-len(m)
                print("\nBook number:",i[2]," "*k,"Book Name:", i[0]," "*n, "Date Borrowed:", str(i[1]))
            s=int(input("\nEnter Book Number to be returned: "))
            q="select Book_borrowed,date_of_borrowing from borrow  where id={}  and SlNo={} ".format(idno,s)
                                                                                                                
            mycur.execute(q)
            r = mycur.fetchone()
            if (r != None):
                extra = 0
                bor_date = r[1]
                yb = int(bor_date[0:4])
                mb = int(bor_date[5:7])
                dtb = int(bor_date[8:])
                now = datetime.now()
                d = now.strftime('%Y-%m-%d')
                yr = int(d[0:4])
                mr = int(d[5:7])
                dtr = int(d[8:])
                date1 = date(yb, mb, dtb)
                date2 = date(yr, mr, dtr)
                n = (date2 - date1).days
                if (n > 30):
                    print("\nBook overdue, fine will be imposed")
                    extra = 10 * (n - 30)
                    print("Book name:" + r[0] + "\nNo. of days overdue:", n - 30, "\nFine:", extra)
                    print("Book successfully returned")
                else:
                    print("Book successfully returned")
                q = "delete from borrow where id={} and SlNo={}".format(idno, s)
                exct(q)
                q = "update book set Quantity=Quantity+{} where SlNo={}".format(1, s)
                exct(q)
            print("_" * 75)

        if (cha == 'c'):
            print("_" * 50)
            break


print("\n\nWELCOME TO THE LIBRARY\n\n")
while True:
    chl = int(input("\n1.ADMIN\n2.USER\n3.EXIT\n"))
    if (chl == 1):
        un = input("\nEnter Username: ")
        pswd = input("Enter Password: ")
        q = "select * from admin where username='{0}' and password='{1}'".format(un, pswd)
        mycur.execute(q)
        rs = mycur.fetchall()
        if (len(rs) != 0):
            admin()
        else:
            print("\nINVALID USERNAME OR PASSWORD\n", '-' * 50)
    if (chl == 2):
        print("\nEnter ID no.:", end='')
        idno = tryInt()
        ch = check(idno)
        if (ch == 1):
            user(idno)
        else:
            print("\nINVALID MEMBERSHIP ID", '-' * 50)
    if (chl == 3):
        yn = input("\nAre you sure you want to exit?(yes/no): ")
        if (yn == 'yes'):
            print("\nTHANK YOU FOR VISITING")
            print("*" * 100)
            break
