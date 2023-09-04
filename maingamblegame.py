
def deposit():
    while True:
        amount = input("How much money you wanna lo- sorry when back in great spades today? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 ya big goof.")
        else:
            print("I SAID Please enter a number.")
            
    return amount



deposit()
