class atm:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def check_balance(self):
        print("50")

    def withdrawal(self, amount):
        new_amount = 50 - amount
        print("You have withdrawn amount: " + str(amount) + " " + "Amount Left: " + str(new_amount))

def main():
    cardNumber = input("Enter Card Number: ")
    pinNumber = input("Enter your pin: ")

    NewUser = atm(cardNumber, pinNumber)
    
    print("Choose your options: ")
    print("1. Balance Enquiry")
    print("2. Withdraw Amount")
    
    options = int(input("Enter option number: "))

    if options == 1 :
        NewUser.check_balance()
    elif options == 2 :
        userAmount = int(input("Enter Amount: "))
        NewUser.withdrawal(userAmount)
    else:
        print("Enter a valid option")

main()
     
