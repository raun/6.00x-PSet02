monthlyInterestRate=annualInterestRate/12
lowerBound=balance/12
upperBound=(balance*pow((1+monthlyInterestRate),12))/12
updateBalance=balance
midValue=0
while abs(updateBalance)>0.1:
	updateBalance=balance
	midValue=(lowerBound+upperBound)/2.0
	month=0
	while month<12:
		month+=1
		updateBalance=(updateBalance-midValue)*(1+monthlyInterestRate)
	if updateBalance>0:
		lowerBound=midValue
	elif updateBalance<0:
		upperBound=midValue
print("Lowest Payment: "+str(round(midValue,2)))
