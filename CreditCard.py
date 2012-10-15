b0=float(raw_input("Enter the balance:"))
r=float(raw_input("Enter the rate of interest:"))
pr=float(raw_input("Enter the monthly payment rate:"))
i=0
while i<=12:
	p=(b0*pr)/100
	b1=(b0-p)*(1+(r/1200))
	print(str(i)+" "+str(b0)+" "+str(p)+" "+str((b0-p)*(r/1200)))
	b0=b1
	i+=1
