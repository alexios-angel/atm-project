# ATM

You are tasked with creating an ATM (Automated Teller Machine) monitoring and alert application. The application will process transactions and generate alerts for specific events. This simulation represents a simplified version of an actual ATM system.

## Requirements
Your task is to implement an ATM monitoring and alert application with the following requirements:

1. Transaction Handling: Implement an ATM class that can handle basic transactions, including balance inquiries, deposits, and withdrawals.

2. Balance Inquiry: Allow users to check the balance of their checking and savings accounts.

3. Deposit: Allow users to deposit funds into their checking or savings account. After a successful deposit, display the updated account balance.

4. Withdrawal: Allow users to withdraw funds from their checking or savings account. Ensure that the ATM checks for sufficient funds and provides appropriate error messages. After a successful withdrawal, display the updated account balance.

5. Interest Calculation: Implement a savings account that calculates interest on a monthly basis. Use a predefined annual interest rate for the calculations.

6. Alert Generation: Generate alerts for the following situations:

    * If a user attempts to withdraw more money from an account than they have.
    * If a user's savings account is credited with monthly interest.

### Input Format
The program should not take input from external files or sources. Input should be obtained through user interaction in the console or terminal.



### Output Format
The program should output messages to the console or terminal. Alerts should be displayed with relevant information, including account details, transaction details, and timestamps.



## Sample Data
As this program relies on user interaction, there is no specific sample data for input. Users will input their actions, such as balance inquiries, deposits, withdrawals, and the program will provide corresponding output.


### Ouput
Here's a sample of what the program's output might look like during user interaction:


```text
Options:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 1
Checking Balance: $1000
Savings Balance: $5000

Options:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 2
Enter account type (checking/savings): savings
Enter the amount to deposit: 100
Deposit of $100 into savings account successful.
Checking Balance: $1000
Savings Balance: $5100

Options:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 3
Enter account type (checking/savings): checking
Enter the amount to withdraw: 500
Withdrawal of $500 from checking account successful.
Checking Balance: $500
Savings Balance: $5100

Options:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 3
Enter account type (checking/savings): checking
Enter the amount to withdraw: 1200
Insufficient funds in checking account.

Options:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice: 4
Exiting the ATM. Have a nice day!

```
