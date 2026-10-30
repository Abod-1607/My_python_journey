print ("welcome to the menu")
print ("tea price = 5$ ")
print ("coffee price = 10$ ")
print ("juice price = 10$ ")

drink = input("choose your drink: ")

if drink == "tea":
    tea = input ("choose your tea (hot tea or ice tea): ")
    if tea == "hot tea":
        print ("your hot tea will be ready in 10 mins")
    if tea == "ice tea":
        print ("your ice tea will be ready in 10 mins")

elif drink == "coffee":
    coffee = input ("choose your coffee (hot or cold): ")
    if coffee == "hot":
        hot = input ("americano or espresso: ")
        if hot == "espresso":
            print ("your espresso will be ready in 10 mins")
        if hot == "americano":
            print ("your espresso will be ready in 10 mins")
    if coffee == "cold":
        cold = input ("cappuccino or latte: ")
        if cold == "latte":
            print ("your latte will be ready in 10 mins")
        if cold == "cappuccino":
            print ("your cappuccino will be ready in 10 mins")

elif drink == "juice":
    juice = input ("choose your juice type: ")
    if juice == "orange":
        print ("your orange juice will be ready in 5 min")
    if juice == "strawberry":
        print ("your strawberry juice will be ready in 5 min")
    if juice == "mango":
        print ("your mango juice will be ready in 5 min")

else :
    print ("sry your drink is not available")

payment = input ("choose your payment: ")
if payment == "visa":
    vise = input ("choose your vise number: ")
    amount = input ("choose your money amount: ")
    exp = int(input ("choose your expire year : "))
    if exp > 2027:
        print ("payment done")
    if exp < 2027:
        print ("your visa is expired")

elif payment == "cash":
    print ("pls give the cash to the casher")

else:
    print (" invalied payment")
