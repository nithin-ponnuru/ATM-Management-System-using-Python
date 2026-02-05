from datetime import datetime, timezone, timedelta

# Account Details
IPPB_account = {
    "account_no": 52210084905,
    "last5": 84905,
    "account_holder": "Ponnuru Nithin",
    "mobile_no": 7569961434,
    "ATM PIN": 2005,
    "balance": 5000,
    "current_account" : 100000,
    "credit_card" : 50000,
    "otp": 123456,
    "last 5 transactions": {
        1: "UPI~603013046347~CR~Ponnuru Nithin~IPOS +500",
        2: "UPI~603012797553~DR~Ponnuru Nithin~IPOS -222",
        3: "UPI~603958878636~CR~Ponnuru Nithin~IPOS +2035",
        4: "UPI~639469052267~DR~Ponnuru Nithin~IPOS -555",
        5: "UPI~639463603329~DR~Ponnuru Nithin~IPOS -554"
    },
    "Dollars" : 10000,
}

receipt_txn = "No Transaction"
receipt_amount = ""
receipt_extra = ""

# Language Selection
print("Welcome to ATM")
print("\nInsert the Card")
print("\n1. English")
print("2. Hindi")
lang = int(input("Select Language: "))
if lang == 1:
    print("Language Selected: English")
elif lang == 2:
    print("भाषा चुनी गई: हिंदी")
else:
    print("Invalid Language Selection")
    print("ATM Session Ended")

# ATM PIN attempts
if lang == 1 or lang == 2:
    attempts = 1
    while attempts <= 3:
        pin = int(input("\nEnter 4-Digit ATM PIN: "))
        if pin < 1000 or pin > 9999:
            print("PIN Must be Exactly 4 digits")
            continue
        if pin == IPPB_account["ATM PIN"]:
            print("PIN Verified Successfully")
            break
        else:
            if attempts < 3:
                print("Wrong PIN. Remaining attempts:", 3 - attempts)
            attempts = attempts + 1
    if attempts > 3:
        print("ATM Card Blocked Due to 3 Wrong Attempts")

    else:
        print("\n1. Domestic" "\n2. International")
        transaction_type = int(input("Enter Transaction Type: "))
        if transaction_type == 1:
# ATM Menu
            print("\nATM Menu" "\n1. Balance Inquiry" "\n2. Mini Statement" "\n3. PIN Generation" "\n4. PIN Change" "\n5. Cash Withdraw" "\n6. Deposit" "\n7. Last 5 Transactions" "\n8. Money Transfer" "\n9. Exit")
            choice = int(input("\nEnter Your Choice: "))    
# Balance
            if choice == 1:
                print("\nAvailable Balance:", IPPB_account["balance"])
                receipt_txn = "Balance Inquiry"
                receipt_extra = IPPB_account["balance"]

# Mini Statement
            elif choice == 2:
                print("\nMini Statement: ")
                for i in IPPB_account["last 5 transactions"]:
                    print(IPPB_account["last 5 transactions"][i])
                    receipt_txn = "Mini Statement"

# PIN Generation
            elif choice == 3:
                last = int(input("\nEnter last 5 digits of account number: "))
                if last == IPPB_account["last5"]:
                    print("OTP sent to registered mobile number")
                    otp_enter = int(input("Enter OTP: "))
                    if otp_enter == IPPB_account["otp"]:
                        new_pin = int(input("Create new 4 digit PIN: "))
                        IPPB_account["ATM PIN"] = new_pin
                        print("ATM PIN generated successfully")
                        receipt_txn = "PIN Generation"
                    else:
                        print("Wrong OTP")
                        receipt_txn = "PIN Generation Failed"
                else:
                    print("Invalid account details")
                    receipt_txn = "PIN Generation Failed"

# PIN Change
            elif choice == 4:
                oldpin = int(input("\nEnter old pin: "))
                if oldpin == IPPB_account["ATM PIN"]:
                    print("OTP sent to registered mobile number")
                    otp_enter = int(input("Enter OTP: "))
                    if otp_enter == IPPB_account["otp"]:
                        new_pin = int(input("Enter new 4 digit PIN: "))
                        IPPB_account["ATM PIN"] = new_pin
                        print("PIN changed successfully")
                        receipt_txn = "PIN Change"
                    else:
                        print("Wrong OTP")
                        receipt_txn = "PIN Change Failed"
                else:
                    print("Invalid account")
                    receipt_txn = "PIN Change Failed"

# Withdraw
            elif choice == 5:
                print("\n1. Saving Account" "\n2. Current Account" "\n3. Credit Card")
                acc_type = int(input("Enter Account type: "))
                if acc_type == 1:
                    amt = int(input("\nEnter withdrawal amount: "))
                    if amt % 100 == 0:
                        if amt <= IPPB_account["balance"]:
                            IPPB_account["balance"] = IPPB_account["balance"] - amt
                            print("Please collect your cash")
                            print("Remaining Balance:", IPPB_account["balance"])
                            receipt_txn = "Cash Withdraw Saving Account (Domestic)"
                            receipt_amount = amt
                            receipt_extra = IPPB_account["balance"]
                        else:
                            print("Insufficient Funds")
                            receipt_txn = "Withdraw Failed"
                    else:
                        print("Please enter amount in multiples of 100")
                        receipt_txn = "Withdraw Failed"
                        
                if acc_type == 2:
                    amt1 = int(input("\nEnter withdrawal amount: "))
                    if amt1 % 100 == 0:
                        if amt1 <= IPPB_account["current_account"]:
                            print("OTP sent to registered mobile number")
                            otp_enter = int(input("Enter OTP: "))
                            if otp_enter == IPPB_account["otp"]:
                                IPPB_account["current_account"] = IPPB_account["current_account"] - amt1
                                print("Please collect your cash")
                                print("Remaining Balance:", IPPB_account["current_account"])
                                receipt_txn = "Cash Withdraw Current Account (Domestic)"
                                receipt_amount = amt1
                                receipt_extra = IPPB_account["current_account"]
                            else:
                                print("Invalid OTP")
                                receipt_txn = "Withdraw Failed"
                        else:
                            print("Insufficient Funds")
                            receipt_txn = "Withdraw Failed"
                    else:
                        print("Please enter amount in multiples of 100")
                        receipt_txn = "Withdraw Failed"
                        
                if acc_type == 3:
                    amt2 = int(input("\nEnter Withdrawal Amount: "))
                    if amt2 % 100 == 0:
                        if amt2 <= IPPB_account["credit_card"]:
                            print("OTP sent to registered mobile number")
                            otp_enter = int(input("Enter OTP: "))
                            if otp_enter == IPPB_account["otp"]:
                                IPPB_account["credit_card"] -= amt2
                                print("Please collect your cash")
                                print("Remaining Balance:", IPPB_account["credit_card"])
                                receipt_txn = "Cash Withdraw Credit Card (Domestic)"
                                receipt_amount = amt2
                                receipt_extra = IPPB_account["credit_card"]
                            else:
                                print("Invalid OTP")
                                receipt_txn = "Withdraw Failed"
                        else:
                            print("Insufficient Funds")
                            receipt_txn = "Withdraw Failed"
                    else:
                        print("Please enter amount in multiples of 100")
                        receipt_txn = "Withdraw Failed"
                    
# Deposit
            elif choice == 6:
                amt = int(input("\nEnter deposit amount: "))
                IPPB_account["balance"] = IPPB_account["balance"] + amt
                print("Amount deposited successfully")
                print("Total Balance:", IPPB_account["balance"])
                receipt_txn = "Cash Deposit"
                receipt_amount = amt
                receipt_extra = IPPB_account["balance"]

# Transaction History
            elif choice == 7:
                print("\nHistory: ")
                for i in IPPB_account["last 5 transactions"]:
                    print(IPPB_account["last 5 transactions"][i])
                    receipt_txn = "Last 5 Transactions"


# Money Transfer
            elif choice == 8:
                receiver = int(input("\nEnter receiver account number: "))
                amt = int(input("Enter transfer amount: "))
                if amt <= IPPB_account["balance"]:
                    IPPB_account["balance"] = IPPB_account["balance"] - amt
                    print("Money transferred successfully")
                    print("Remaining Balance:", IPPB_account["balance"])
                    receipt_txn = "Money Transfer"
                    receipt_amount = amt
                    receipt_extra = IPPB_account["balance"]
                else:
                    print("Insufficient balance")
                    receipt_txn = "Money Transfer Failed"

# Exit
            elif choice == 9:
                print("Thank you for using ATM")
                receipt_txn = "Exit"

            else:
                print("Invalid option")
#international 
        else:
            print("\nATM Menu" "\n1. Balance Inquiry" "\n2. Cash Withdraw"  "\n3. Exit")
            inter_choice = int(input("\nEnter Your International Choice: "))
            if inter_choice == 1:
                print("\nAvailable Balance:", IPPB_account["Dollars"])
                receipt_txn = "Balance Inquiry"
                receipt_extra = IPPB_account["Dollars"]
                
            elif inter_choice == 2:
                inter_amt = int(input("\nEnter Dollars: $"))
                if inter_amt % 100 == 0:
                    if inter_amt <= IPPB_account["Dollars"]:
                        print("Exchange Rate: $1 = 90") 
                        ind_curr = inter_amt * 90
                        print("Indian Currency: ",ind_curr)
                        con_fee = inter_amt * 2
                        print("Conversation Fee: ", con_fee)
                        gst = con_fee * 18 / 100
                        print("GST 18%: ", gst)
                        plat_fee = 50
                        print("Platform Fee: ",plat_fee)
                        total_charges = con_fee + gst + plat_fee
                        print("Total Charges: ",total_charges)
                        final_amt = ind_curr - total_charges
                        print("Final Amount: ",final_amt)
                        IPPB_account["Dollars"]-=inter_amt
                        print("\nWithdraw Successful")
                        print("Remaining Dollars: $",IPPB_account["Dollars"])
                        receipt_txn = "Cash Withdraw (International)"
                        receipt_amount = inter_amt
                        receipt_extra = IPPB_account["Dollars"]
                    else:
                        print("Insufficient Dollars")
                        receipt_txn = "Withdraw Failed"
                else:
                    print("Please Enter Dollars in Multiple of 100")
                    receipt_txn = "Withdraw Failed"
                    
            elif inter_choice == 3:
                print("\nThank You For Using ATM")
                receipt_txn = "Exit"
            else:
                print("Invalid Option")

# Recipit printing                        
recipit = input("\nDo you want to print receipt (yes/no): ")

if recipit == "yes":
    
    ist = timezone(timedelta(hours=5, minutes=30))
    current_datetime = datetime.now(ist)
    current_date = current_datetime.strftime("%d-%m-%Y")
    current_time = current_datetime.strftime("%H:%M:%S")

    print("\n================ IPPB ATM RECEIPT ================")
    print("Account Holder :", IPPB_account["account_holder"])
    print("Account Number :", IPPB_account["account_no"])
    print("Mobile Number  :", IPPB_account["mobile_no"])
    print("Date           :", current_date)
    print("Time (IST)     :", current_time)
    print("Transaction    :", receipt_txn)
    print("-----------------------------------------------")

    if receipt_txn == "Balance Inquiry":
        print("Available Balance :", receipt_extra)

    elif receipt_txn == "Cash Withdraw (Domestic)" or receipt_txn == "Cash Deposit" or receipt_txn == "Money Transfer":
        print("Transaction Amount :", receipt_amount)
        print("Remaining Balance  :", receipt_extra)
        print("Transaction Completed Successfully")
        print("-----------------------------------------------")
        print("Status : SUCCESS")
        print("===============================================") 

    elif receipt_txn == "Cash Withdraw (International)":
        print("Withdraw Amount ($):", receipt_amount)
        print("Indian Currency    :", ind_curr)
        print("Conversion Fee     :", con_fee)
        print("GST (18%)          :", gst)
        print("Platform Fee       :", plat_fee)
        print("Final Amount (INR) :", final_amt)
        print("Remaining Dollars  :", receipt_extra)

    else:
        print("Transaction Completed Successfully")
        print("-----------------------------------------------")
        print("Status : SUCCESS")
        print("===============================================") 
        
# Visting wish
choice = [1,2,3,4,5,6,7,8,9]
for i in choice:
     print("\nThank you for using ATM")
     print("Please take your card")
     break
