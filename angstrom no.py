a=int(input("enter no."))
y=a
sum=0
while a>0:
 x=a%10
 sum=(x*x*x +sum)
 a=a//10
if sum==y:
 print("number is an angstrom number")
else:
 print("number is not angstrom")