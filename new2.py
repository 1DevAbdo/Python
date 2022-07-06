from turtle import begin_fill


print("Welcome to my coffee shop")

name = input("what is your name:\n")


print("welcome", name, "we are happy to see you in our coffee shop\n\n")

menu = ("Latte   Black Coffee\n Espresso   Cappucino\n Frappuccino   Mocha")

print("this is our Menu\n",menu, "\nwhat would you like to drink\n ")


order = input("which cofee would you like to take:\n")

if order == "Latte":
    price = 26
elif order == "Black Coffee":
    price = 21
elif order == "Mocha":
    price = 34
elif order == "Frappuccino":
    price = 37
elif order == "Espresso":
    price = 25
elif order == "Cappucino":
    price = 29
else:
    print("sorry we dont have that coffee here")
    exit()

quan = input("how many cofee would you like to get? \n")

total = price * int(quan)

print("thank you", name, "your total is:\n₺", str(total))


print("sound's nice", name, "\nyoure", int(quan), order, "will be ready in a bit\n")

print("thank you for choosing us", name, ":)")