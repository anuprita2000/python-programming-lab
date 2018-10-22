def factorial(a):
 f=1
 if a>1:
  f=(a-1)
  f=f*a
  return f
 elif a==0:
  return 1
 elif a==1:
  return 1
fact=factorial(4)
print("factorial=",fact)