amt=float(input("enter purchase amount:"))
if amt < 0 :
    print("invalid amount")
else :
      discount=0.0
if amt >= 5000 :
    discount= amt*20/100
elif amt>=2000 and amt< 5000 :
    discount=amt*10/100
print("discount amount:",discount)
print("final payable amount:",amt-discount)


