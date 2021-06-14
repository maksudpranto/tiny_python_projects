print("""
Welcome to Basic ATM Transaction Service.
Please choose an option from below:
1) Check Balance
2) Withdraw Money
3) Deposit Money
4) Send Money
5) Exit
""")


class AtmTransaction:
    def transaction(self):
        initial_balance = 50000
        option = int(input("Choose an Option: "))
        if option == 1:
            print("Your Current Account Balance is: ", initial_balance)
        if option == 2:
            withdraw_amount = float(input("Enter the amount you want to withdraw: "))
            if withdraw_amount < initial_balance:
                balance = initial_balance - withdraw_amount
                print("Withdraw success. Your current balance is: ", balance)
            else:
                print("You have entered invalid amount. Your account balance is: ", initial_balance)
        if option == 3:
            deposit_money = float(input("Enter the amount you want to Deposit: "))
            total_balance = initial_balance + deposit_money
            print("Deposit success. Your current account balance is: ", total_balance)
        if option == 4:
            account_number = int(input("Enter the account number you want to send: "))
            send_amount = float(input("Enter the amount you want to send: "))

            if send_amount > initial_balance:
                print("You have entered an invalid amount. Your current balance is: ", initial_balance)
            else:
                print("Send success")
        if option == 5:
            print("Thanks for using our services.")
            exit()


obj = AtmTransaction()
obj.transaction()
