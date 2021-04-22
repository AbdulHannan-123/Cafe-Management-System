
from os import system,name
import numpy
def clear():
    if name =='nt':
        _=system('cls')
    else:
        _=system('clear')

class user:
    def __init__(self, userName, password, email, contact):
        self.userName=userName
        self.pasw=password
        self.email=email
        self.contact=contact
        self.id=0
        self.next=None

#   this is link list for menu
'''                          
class Node:                 #linklist creater
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.start = None

    def view(self):             #list ko show karany k leay
        if (self.start == None):
            print("no menu")
        else:
            temp = self.start
            while (temp != None):
                    print(temp.data,end="\n")
                    temp = temp.next

    def insert(self,value):       # list me data store karanay k leay
        node = Node(value)
        if self.start == None:
            self.start = node
        else:
            temp = self.start
            while(temp.next!=None):
                temp = temp.next
            temp.next = node

def MENU():                               # Menu dekhanay k leay
    mylist = linkedlist()
    print("THERE ARE SOME REFRESHMENTS FOR YOU")
    mylist.insert("1 := BURGER")
    mylist.insert("2 := PIZZA")
    mylist.insert("3 := PASTA")
    mylist.view()
    num=str(input("Enter the Number :"))
    return num


def Burger():   #burger show karany k leay
    bur=linkedlist()
    print("-_-_-_-_-_-_-_-_THERE ARE BURGURS-_-_-_-_-_-_-_-_")
    bur.insert("1 := CHESE BURGER................100")
    bur.insert("2 := BEEF BURGER.................150")
    bur.insert("3 := CHICKEN BURGER..............200")
    bur.view()
    num=str(input("Enter The Order Number : "))
    return num

def Pizza():    # pizzay show karanay k leay
    piz=linkedlist()
    print("-_-_-_-_-_-_-_-_PIZZA'S-_-_-_-_-_-_-_-_")
    piz.insert("1 := CHICKEN PERIPERI")
    piz.insert("2 := CHICKEN CHEEZE")
    piz.insert("3 := CHICKEN PEPAROONI")
    piz.view()

def Pasta():                     #Pasta k menu
    pas=linkedlist()
    print("-_-_-_-_-_-_-_-_PASTA-_-_-_-_-_-_-_-_")
    pas.insert("1 := CHEESE PASTA")
    pas.insert("2 := LASANIA")
    pas.view()

#def Calculation():          # for calculation in progress

'''

def MENU():
    my_array = numpy.array(["Enter 1 := burger","Enter 2 := Pasta","Enter 3 := Pizza"])
    Pprint(my_array)
    menu_no = input("\n\t Enter Choice := ")
    return menu_no


def Burger():
    brgr = numpy.array(["Enter 1 :=Chicken Burger","Enter 2 :=Beef Burger","Enter 3 := Cheese Burger"])
    Pprint(brgr)
    brgr_no = input("\n\t Enter Choice := ")
    return brgr_no

def Pasta():
    pas = numpy.array(["Enter 1 :=Chicken Pasta","Enter 2 := Cheese Pasta"])
    Pprint(pas)
    pas_no = input("\n\t Enter Choice := ")
    return pas_no

def Pizza():
    piz = numpy.array(["Enter 1 := Perri Peri Pizza", "Enter 2 := Cheese Pizza", "Enter 3 := BBQ Pizza"])
    Pprint(piz)
    piz_no = input("\n\t Enter Choice := ")
    return piz_no

def Pprint(x):
    for i in range(len(x)):
        print(x[i])

def cal():
    inp = input("Enter 1 for order again\nEnter 2 for Main Menu\npress any to exit :=  ")
    if inp == "1":
        clear()
        return True
    elif inp == "2":
        clear()
        FUN()
    else:
        clear()
        return False




class Stack:
    def __init__(self):
        self.stk=[]

    def Push(self,data):
        self.data=data
        self.stk.append(self.data)

    def Pop(self):
        if self.stk==[]:
            return -1
        else:
            return self.stk.pop()

    def Peek(self):
        if len(self.stk)==0:
            return "none"
        else:
            return self.stk[-1]



def FUN():             #Recursion function
    a=MENU()           # call menu
    s = Stack()        # stack price
    z = Stack()        #   stack name
    s.Push(0)
    z.Push("")
    x=0

    clear()

    if (a!="2" and a!="1" and a!="3"):
        print("_____________Number is OUT-OF-ORDER_______________")
        FUN()

    elif a=="1":
            price=0
            name=""
            loop=True
            while loop:
                print("\n" * 80)
                b=Burger()
                if (b != "2" and b != "1" and b != "3"):
                    print("_____________Number is OUT-OF-ORDER_______________")
                    FUN()
                elif b == "1":
                    price=100
                    name="Chicken"
                    print("your price is ", price)


                elif b == "2":
                    price = 200
                    name = "Beef"
                    print("your price is ", price)

                elif b == "3":
                    price = 300
                    name="Cheese"
                    print("your price is ", price)
                s.Push(price)
                z.Push(name)
                clear()
                loop= cal()

    elif a=="2":
        price = 0
        name = ""
        loop= True
        while loop:
            print("\n" * 80)
            b=Pizza()
            if (b != "2" and b != "1" and b != "3"):
                print("_____________Number is OUT-OF-ORDER_______________\n\n_-_-_-_-BACK TO MAIN MENU-_-_-_-_")
                FUN()
            elif b == "1":
                price = 100
                name = "Perri Peri Pizza"
                print("your price is ", price)


            elif b == "2":
                price = 200
                name = "Cheese Pizza"
                print("your price is ", price)

            elif b == "3":
                price = 300
                name = "BBQ Pizza"
                print("your price is ", price)
            s.Push(price)
            z.Push(name)
            loop = cal()


    elif a=="3":
        price = 0
        name = ""
        loop = True
        while loop:
            print("\n" * 80)
            b = Pasta()
            if (b != "2" and b != "1" and b != "3"):
                print("_____________Number is OUT-OF-ORDER_______________\n\n_-_-_-_-BACK TO MAIN MENU-_-_-_-_")
                FUN()
            elif b == "1":
                price = 100
                name = "Chicken Pasta"
                print("your price is ", price)


            elif b == "2":
                price = 200
                name = "Chese Pasta"
                print("your price is ", price)

            s.Push(price)
            z.Push(name)
            loop = cal()

    print("ITEM      |       PRICE      |       TOTEL\n")
    while z.Peek() !="":
        print(z.Pop(),"           ",s.Peek())
        print()
        y = s.Pop()
        x += y
    print("                                 ",x)






class loginSignupPage:
    def __init__(self):
        self.head=None
        self.size=50
        self.lenght=0
        self.lastId=1000
        self.limitReached=False
        self.details={}

    def set_Total_No_Of_Waiters(self, num):
        self.size=num

    def addWaiter(self, userName, password, email, contact):
        node = user(userName, password, email, contact)
        if self.head==None:      # if there is'nt any node initialized in the linked list, initialize one and make it the head
            self.head=node
            self.lenght+=1
            node.id=self.lastId
            self.details[node.id]=[str(userName), str(email), str(contact)]
            self.lastId+=10 # when the second user signs up, he gets the different id
            print("Congrats!  your signup is copmpleted. You can login now. Your ID is {}\n".format(node.id))
        else:
            if self.lenght<=self.size:
                x=self.head
                while x.next!=None:
                    x=x.next
                x.next=node
                self.lenght+=1
                node.id = self.lastId
                self.details[node.id]=[str(userName), str(email), str(contact)]
                self.lastId += 10
                print("Congrats!  your signup is copmpleted. You can login now. Your ID is {}\n".format(node.id))

            else:
                self.limitReached=True

    def signUp(self):
        print("************************ Create a new account ************************\n")
        name=input("Enter your Name: ")
        password=input("Enter your Password: ")
        email=input("Enter your email: ")
        contact=input("Enter your Contact no: ")


        if self.limitReached==True:
            print("Sorry sir, there's no vacancy left!\n")
        else:
            self.addWaiter(name, password, email, contact)
            x=int(input("\n1. Do you want to Log in to your account now?\n2. Go back to main menu?\n\nenter the number of your choice: "))
            while x>2:
                x=int(input("Enter a valid number"))
            if x==1:
                print("\n" * 80)
                self.login()
            elif x==2:
                self.mainMenu()

    def bindarySearch(self, x):
        arr=list(self.details.keys())
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return False

    def mainMenu(self):
        print("*****************  Welcome to Bilal's Cafe ***************\n")
        choice=int(input("1. SignUp, if you're new here.\n2. LogIn, if you already have an account.\n3. list of Waiters working here.\n4. Search waiter by id\n\nChoose the number of your choice: "))
        while choice>4:
            print("Please enter the number 1-3: ", end="")
            choice = int(input(""))
        if choice==1:
            print("\n" * 100)
            self.signUp()
        elif choice==2:
            print("\n" * 100)
            self.login()
        elif choice==3:
            for i in range(len(self.details)):
                print(str(i+1)+". "+ str(list(self.details.values())[i]))
            x = int(input("Go back to main menu? ('1' for yes/'2' for no)?\n\nenter the number of your choice: "))
            while x>2:
                x = int(input("Enter a valid number: "))
            if x == 1:
                print("\n" * 80)
                self.mainMenu()
            elif x == 2:
                return
        elif choice==4:
            self.idSearch()
            x = int(input("\nGo back to main menu? ('1' for yes/'2' for no)?\n\nenter the number of your choice: "))
            while x > 2:
                x = int(input("Enter a valid number: "))
            if x == 1:
                print("\n" * 80)
                self.mainMenu()
            elif x == 2:
                return

    def login(self):
        print("************************ LogIn ************************")
        Name = str(input("Enter your Name :"))
        PW = str(input("Enter your Password :"))
        if self.head:
            x=self.head
            while x!=None:
                if x.userName==Name and x.pasw==PW:
                    print("Acces granted\nWelcome to the cafe")
                    print("\n" * 80)
                    FUN()
                    return
                else:
                    x=x.next
            print("User Not Found\n")
            x=int(input("1. New here? Do you Want to signUp? (back to main menu)\n2. Try entering the id\password again.\nEnter the number of your choice: "))
            while x>2:
                x= int(input(("Enter a valid number (1/2 ?): ")))
            if x==1:
                self.mainMenu()
            elif x==2:
                self.login()


    def idSearch(self):
        id=int(input("Enter the waiter's Registered id: "))
        x=self.bindarySearch(id)
        if self.bindarySearch(id):
            print(list(self.details.values())[x])
        else:
            print("Sorry!  User Not Found. ")








cafe=loginSignupPage()

# cafe.addWaiter("bilal", "111", "dwad", "dwdgr")
# cafe.addWaiter("areeb", "222", "dwad", "dwdgr")
# cafe.addWaiter("rafay", "333", "33", "dwdgr")
# cafe.addWaiter("rafay", "444", "44", "dwdgr")

cafe.mainMenu()
