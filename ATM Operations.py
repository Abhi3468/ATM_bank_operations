import mysql.connector  # version 8.0.24

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Abhi@6362751007',
    'database': 'DKG_ATM',
}


def greetings(my_fun):
    def wrap():
        print('_____________Hello Welcome to DKG Bank_____________')
        return my_fun()
    return wrap


@greetings
def insert_card():
    print('\nPlease insert your ATM Card PIN Number:')


class ATM:

    def __init__(self, balance=0):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.balance = balance
        self.pin = None  # Initialize pin attribute

    def __del__(self):
        self.conn.close()

    def available_balance(self):
        self.cursor.execute("SELECT balance FROM accounts WHERE card_pin = %s", (self.pin,))
        # The %s in the query is  a placeholder for parameterized queries
        result = self.cursor.fetchone()
        # If pin matched with account in database.
        # The fetchone() method is called on the cursor object to retrieve the result of the query.
        # (By means if fetch available balance).

        if result:  # if result is not NONE
            self.balance = result[0]
            # The above line updates the balance attribute with the available balance fetched from the database.
            print('The Available balance is:', self.balance)
        else:
            print('Error: Account not found')

    def withdraw(self, amount):
        self.cursor.execute("SELECT balance FROM accounts WHERE card_pin = %s", (self.pin,))
        result = self.cursor.fetchone()
        if result:
            current_balance = result[0]
            if amount > current_balance:
                print('Insufficient balance')
            else:
                # Amount is deducted from available_balance
                self.cursor.execute("UPDATE accounts SET balance = balance - %s WHERE card_pin = %s", (amount, self.pin))
                # update the withdraw_history column in the database
                self.cursor.execute("UPDATE accounts SET withdraw_history = withdraw_history + %s WHERE card_pin = %s",
                                    (amount, self.pin))
                # commit the changes made in python code to the database
                self.conn.commit()
                print('The amount {} successfully withdrawn, \n___Please collect your cash___'.format(amount))
                self.available_balance()
        else:
            print('Error: Account not found')

    def deposit(self, amount):
        # update the available_balance with deposit amount in database
        self.cursor.execute("UPDATE accounts SET balance = balance + %s WHERE card_pin = %s", (amount, self.pin))
        # update the deposit_history column in the database
        self.cursor.execute("UPDATE accounts SET deposit_history = deposit_history + %s WHERE card_pin = %s",
                            (amount, self.pin))
        # commit the changes made in python code to the database
        self.conn.commit()
        print('The amount {} is successfully deposited into your account'.format(amount))
        self.available_balance()

    def pin_change(self):
        print('Please enter your new pin:')
        new_pin = input()
        if len(new_pin) == 4:
            # update the PIN_change in database
            self.cursor.execute("UPDATE accounts SET card_pin = %s WHERE card_pin = %s", (new_pin, self.pin))
            # commit the changes made in python code to the database
            self.conn.commit()
            print('_______your pin successfully changed_______')
        else:
            print('Invalid PIN: Please enter 4-digit PIN number')


def main():
    atm = ATM()
    card_details = input()  # Enter the 4 digit-pin number
    atm.pin = card_details
    while True:
        if len(card_details) == 4:
            print('Please select the following options:')
            print('1.Balance \t 2.Withdraw \t 3.Deposit \t 4.Pin_change')
            user_input = int(input())
            if user_input == 1:
                atm.available_balance()
                print('____Thank you for visiting DKG bank ATM____')
                break
            elif user_input == 2:
                amount = int(input('Please enter the amount to be withdrawn:'))
                atm.withdraw(amount)
                print('____Thank you for visiting DKG bank ATM____')
                break
            elif user_input == 3:
                amount = int(input('Please enter the amount to be deposited:'))
                atm.deposit(amount)
                print('____Thank you for visiting DKG bank ATM____')
                break
            elif user_input == 4:
                atm.pin_change()
                print('____Thank you for visiting DKG bank ATM____')
                break
            elif user_input >= 5:
                print('Please insert valid option')
                break

        else:
            print('Please insert valid PIN number')
            break


if __name__ == '__main__':
    insert_card()
    main()

