import assignm.AreaCalc as ac
import assignm.CurrencyConvertor as cc
import assignm.Arithmetic as calc

def area_calc():
    print("Area Calculator")
    choice=int(input("Enter 1 for circle, 2 for triangle, 3 for square:"))
    if choice==1:
        r=int(input("Enter the radius:"))
        print("The area of circle is:",ac.area_circ(r))
    elif choice==2:
        b=int(input("Enter the base of the triangle"))
        h=int(input("Enter the height of the triangle"))
        print("The area of triangle is:",ac.area_tri(b,h))
    elif choice==3:
        s=int(input("Enter the side of the Square"))
        print("The area of Square is:",ac.area_sqr(s))
    else:
        print("Enter a valid choice")
        
def currency():
    print("CurrencyConvertor to INR")
    choice=int(input("Enter 1 for USD,2 for Euro, 3 for Dhirham:"))
    if choice==1:
        usd=int(input("Enter USD:"))
        print("USD to INR:",cc.usd_inr(usd))
    elif choice==2:
        eur=int(input("Enter Euro:"))
        print("EURO to INR:",cc.euro_inr(eur))
    elif choice==3:
        dhs=int(input("Enter Dhirhams:"))
        print("Dhirham to INR",cc.dhs_inr(dhs))
    else:
        print("Enter a valid choice")
        
def arithmetic():
    print("Arithmetic Operations")
    choice=int(input("Enter 1 for Add,2 for Subtract, 3 for Multipy, 4 for Division:"))
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    if choice==1:
        print("Sum:",calc.add(num1,num2))
    elif choice==2:
        print("Subtract:",calc.subtract(num1,num2))
    elif choice==3:
        print("Multiply:",calc.multiply(num1,num2))
    elif choice==4:
        print("Divide:",calc.divide(num1,num2))
    else:
        print("Enter a valid choice")
        
while True:
    print("Choose any one option \n 1 for AreaCalculation \n 2 for CurrencyConversion \n 3 for Calculator \n 4 to Exit")
    option=int(input("Enter a valid choice:"))
    if option==1:
        area_calc()
    elif option==2:
        currency()
    elif option==3:
        arithmetic()
    elif option==4:
        break
    else:
        print("Enter a valid choice")