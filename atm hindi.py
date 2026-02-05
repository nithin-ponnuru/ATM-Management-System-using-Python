from datetime import datetime, timezone, timedelta

# ---------------- ACCOUNT DETAILS ----------------
IPPB_account = {
    "account_no": 52210084905,
    "last5": 84905,
    "account_holder": "Ponnuru Nithin",
    "mobile_no": 7569961434,
    "ATM PIN": 2005,
    "balance": 5000,
    "otp": 123456,
    "Dollars": 10000
}

receipt_txn = ""
receipt_amount = ""
receipt_extra = ""

# ---------------- LANGUAGE SELECTION ----------------
print("Welcome to ATM")
print("Please Insert the Card")
print("\n1. English")
print("2. Hindi")
lang = int(input("Select Language: "))

if lang != 1 and lang != 2:
    print("Invalid Language Selection")
    exit()

# ---------------- LANGUAGE DICTIONARY ----------------
if lang == 1:  # ENGLISH
    L = {
        "pin_ok": "PIN Verified Successfully",
        "wrong_pin": "Wrong PIN. Remaining attempts:",
        "menu": "ATM Menu",
        "bal": "Balance Inquiry",
        "mini": "Mini Statement",
        "pin_gen": "PIN Generation",
        "pin_chg": "PIN Change",
        "withdraw": "Cash Withdraw",
        "deposit": "Deposit",
        "transfer": "Money Transfer",
        "exit": "Exit",
        "avail_bal": "Available Balance:",
        "enter_choice": "Enter Your Choice:",
        "collect": "Please collect your cash",
        "rem_bal": "Remaining Balance:",
        "otp_sent": "OTP sent to registered mobile number",
        "invalid": "Invalid Details",
        "thank": "Thank you for using ATM",
        "take_card": "Please take your card",
        "receipt": "IPPB ATM RECEIPT",
        "txn": "Transaction",
        "amount": "Amount",
        "balance": "Balance",
        "status": "Status : SUCCESS",
        "print_rcpt": "Do you want to print receipt (yes/no):"
    }
else:  # HINDI
    L = {
        "pin_ok": "पिन सफलतापूर्वक सत्यापित",
        "wrong_pin": "गलत पिन। शेष प्रयास:",
        "menu": "एटीएम मेनू",
        "bal": "शेष राशि जांच",
        "mini": "मिनी स्टेटमेंट",
        "pin_gen": "पिन निर्माण",
        "pin_chg": "पिन परिवर्तन",
        "withdraw": "नकद निकासी",
        "deposit": "जमा",
        "transfer": "धन हस्तांतरण",
        "exit": "बाहर निकलें",
        "avail_bal": "उपलब्ध शेष राशि:",
        "enter_choice": "अपना विकल्प दर्ज करें:",
        "collect": "कृपया अपना नकद लें",
        "rem_bal": "शेष राशि:",
        "otp_sent": "ओटीपी भेजा गया",
        "invalid": "अमान्य विवरण",
        "thank": "एटीएम का उपयोग करने के लिए धन्यवाद",
        "take_card": "कृपया अपना कार्ड लें",
        "receipt": "आईपीपीबी एटीएम रसीद",
        "txn": "लेनदेन",
        "amount": "राशि",
        "balance": "शेष राशि",
        "status": "स्थिति : सफल",
        "print_rcpt": "क्या आप रसीद प्रिंट करना चाहते हैं (yes/no):"
    }

# ---------------- PIN VERIFICATION ----------------
attempts = 1
while attempts <= 3:
    pin = int(input("\nEnter 4-Digit ATM PIN: "))
    if pin == IPPB_account["ATM PIN"]:
        print(L["pin_ok"])
        break
    else:
        if attempts < 3:
            print(L["wrong_pin"], 3 - attempts)
        attempts += 1

if attempts > 3:
    print("ATM Card Blocked")
    exit()

# ---------------- ATM MENU ----------------
print("\n" + L["menu"])
print("1.", L["bal"])
print("2.", L["mini"])
print("3.", L["pin_gen"])
print("4.", L["pin_chg"])
print("5.", L["withdraw"])
print("6.", L["deposit"])
print("7.", L["transfer"])
print("8.", L["exit"])

choice = int(input(L["enter_choice"]))

# ---------------- BALANCE ----------------
if choice == 1:
    print(L["avail_bal"], IPPB_account["balance"])
    receipt_txn = L["bal"]
    receipt_extra = IPPB_account["balance"]

# ---------------- PIN GENERATION ----------------
elif choice == 3:
    last = int(input("Enter last 5 digits: "))
    if last == IPPB_account["last5"]:
        print(L["otp_sent"])
        if int(input("Enter OTP: ")) == IPPB_account["otp"]:
            IPPB_account["ATM PIN"] = int(input("Create new PIN: "))
            receipt_txn = L["pin_gen"]
        else:
            receipt_txn = L["invalid"]

# ---------------- PIN CHANGE ----------------
elif choice == 4:
    if int(input("Enter old PIN: ")) == IPPB_account["ATM PIN"]:
        print(L["otp_sent"])
        if int(input("Enter OTP: ")) == IPPB_account["otp"]:
            IPPB_account["ATM PIN"] = int(input("Enter new PIN: "))
            receipt_txn = L["pin_chg"]
        else:
            receipt_txn = L["invalid"]

# ---------------- WITHDRAW ----------------
elif choice == 5:
    amt = int(input("Enter amount: "))
    if amt <= IPPB_account["balance"]:
        IPPB_account["balance"] -= amt
        print(L["collect"])
        print(L["rem_bal"], IPPB_account["balance"])
        receipt_txn = L["withdraw"]
        receipt_amount = amt
        receipt_extra = IPPB_account["balance"]

# ---------------- DEPOSIT ----------------
elif choice == 6:
    amt = int(input("Enter amount: "))
    IPPB_account["balance"] += amt
    receipt_txn = L["deposit"]
    receipt_amount = amt
    receipt_extra = IPPB_account["balance"]

# ---------------- TRANSFER ----------------
elif choice == 7:
    amt = int(input("Enter transfer amount: "))
    if amt <= IPPB_account["balance"]:
        IPPB_account["balance"] -= amt
        receipt_txn = L["transfer"]
        receipt_amount = amt
        receipt_extra = IPPB_account["balance"]

# ---------------- EXIT ----------------
else:
    receipt_txn = L["exit"]

# ---------------- RECEIPT ----------------
if input("\n" + L["print_rcpt"]) == "yes":
    ist = timezone(timedelta(hours=5, minutes=30))
    now = datetime.now(ist)

    print("\n==========", L["receipt"], "==========")
    print("Name :", IPPB_account["account_holder"])
    print("Acc  :", IPPB_account["account_no"])
    print("Date :", now.strftime("%d-%m-%Y"))
    print("Time :", now.strftime("%H:%M:%S"))
    print(L["txn"], ":", receipt_txn)
    print("----------------------------------")

    if receipt_amount != "":
        print(L["amount"], ":", receipt_amount)
    if receipt_extra != "":
        print(L["balance"], ":", receipt_extra)

    print("----------------------------------")
    print(L["status"])
    print("==================================")

print(L["thank"])
print(L["take_card"])
