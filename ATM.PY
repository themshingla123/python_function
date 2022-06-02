option_language=["english","hindi","manipuri","thailand","koren"]
def code():
    user_choose=input("what do you want to do ")
    balance=10000
    if user_choose=="w" :
        amount=int(input("enter the amount"))
        user2=int(input("enter the secret_pin"))
        if user2==3456:
            print(balance-amount,"is your current balance")
    elif user_choose=="d":
        amount=int(input("enter the amount"))
        user2=int(input("enter the secret_pin"))
        if user2==3456:
            print(balance+amount,"is your current balance")
    elif user_choose=="balance_i":
        user2=int(input("enter the secret_pin"))
        if user2==3456:
            print(balance,"is your current balance")
            return "thank Q for visiting"
    else:
        print("wrong pin")
def choose():
    i=0
    while i<len(option_language):
        print("language=",option_language)
        user=input("enter the language")
        if user=="english" or "hindi":
            print("welcome to indian overseas bank")
            print(code())
            break
        
        i=i+1
choose()