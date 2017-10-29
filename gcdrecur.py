def gcdRecur(a, b):
    
    if(a==b or b%a==0):
      return a
    elif(a%b==0):
      return b
    elif(a>b):
      return(gcdRecur(a%b,b))
    else:
      return(gcdRecur(a,b%a))
print(gcdRecur(105, 91))
