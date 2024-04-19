# ATM bank operations display & perform  using python

def greetings(my_fun):
    def wrap():
        print('_____________Hello Welcome to DKG Bank_____________')
        return my_fun()
    return wrap


@greetings
def insert_card():
    print('\nPlease insert your ATM Card PIN Number:')


class ATM():

    def __init__(self, balance=20000):
        self.balance = balance

    def available_balance(self):
        print('The Available balance is: {}'.format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -= amount
            print('The amount {} successfully withdrawn, \n___Please collect your cash___'.format(amount))
            self.available_balance()

    def deposit(self, amount):
        self.balance += amount
        print('The amount {} is successfully deposited into your account'.format(amount))
        self.available_balance()

    def pin_change(self):
        print('Please enter your new pin:')
        pin = input()
        if len(pin) == 4:
            print('_______your pin successfully changed_______')
        else:
            print('Invalid PIN: Please enter 4-digit PIN number')


def main():
    atm = ATM()
    card_details = input()  # Enter the 4 digit-pin number
    while True:
        if len(card_details) == 4:
            print('Please select the following options:')
            print('1.Balance \t 2.Withdraw \t 3.Deposit \t 4.Pin_change \t 5.Exit')
            user_input = int(input())
            if user_input == 1:
                atm.available_balance()
            elif user_input == 2:
                amount = int(input('Please enter the amount to be withdrawn:'))
                atm.withdraw(amount)
            elif user_input == 3:
                amount = int(input('Please enter the amount to be deposited:'))
                atm.deposit(amount)
            elif user_input == 4:
                atm.pin_change()
            elif user_input == 5:
                print('____Thank you for visiting DKG bank ATM____')
                break
            elif user_input >= 6:
                print('Please insert valid option')

        else:
            print('Please insert valid PIN number')
            break


if __name__=='__main__':
    insert_card()
    main()


