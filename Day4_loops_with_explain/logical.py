credit=int(input("Enter you minimum credit amount in $  >\t"))
income=int(input("Pease enter you monthly income in $ >\t"))

if credit > 10000 and income > 4000:
    has_good_income=True
    has_good_credit=True
else:
    has_good_income=False
    has_good_income=False


if has_good_income and has_good_credit:
    print("you are eligible for a loan amount = $10000")
else:
    print("you are not elligible for any laon amount\n")

'''If applicant has high income > 10000 or high credit > 10000 then elligible for loan'''

print("Now If you have high income or high credit then you can apply for loan")
credit=int(input("Enter the credit amount in $ > \t"))
income=int(input("Enter your income in $ \t"))

if credit >= 10000:
    has_good_credit=True
else:
    has_good_credit=False
if income>=5000:
    has_good_income=True
else:
    has_good_income=False
 
if has_good_income or has_good_credit:
    print("you are eligible for a loan amount = $10000")
else:
    print("you are not elligible for any laon amount\n") 


print("**************************************")
has_criminal_record =False
if has_good_credit and not has_criminal_record:
    print(f"you are elligible for a loan amount {credit} ")