for i in range(5):
  print('A number:', i)
def fact_rec(n):
  if n==0 or n==1:
    return1
  else:
    return n* fact_rec(n-1)
    number=int(input("Enter a value:"))
    res= fact_rec(number)
    print("the factorial of{}.". farmat(number,res))