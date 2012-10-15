monthlyInterestRate=annualInterestRate/12
assumedPayment=0
updateBalance=balance
while updateBalance>=0:
	assumedPayment+=10
	updateBalance=balance
	month=0
	while month<12:
		month+=1
		updateBalance=(updateBalance-assumedPayment)*(1+monthlyInterestRate)
print("Lowest Payment: "+str(assumedPayment))
