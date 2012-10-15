monthlyInterestRate=annualInterestRate/12
totalAmountPaid=0
month=0
while month<12:
	month+=1
	print("Month: "+str(month))
	monthlyPayment=monthlyPaymentRate*balance
	print("Minimum monthly payment: "+str(round(monthlyPayment,2)))
	balance=(balance-monthlyPayment)*(1+monthlyInterestRate)
	print("Remaining balance: "+str(round(balance,2)))
	totalAmountPaid+=monthlyPayment
print("Total paid: "+str(round(totalAmountPaid,2)))
print("Remaining balance: "+str(round(balance,2)))
