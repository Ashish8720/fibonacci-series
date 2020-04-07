r=1
while r==1:                                              
  x=int(input("enter the terms: "))       
  f1=0                                                   #first number              
  f2=1                                                   #secand number
  count=0
  if x<=0:                                               #negative numbers are not allowed
    print("please enter the positive number")
  else:
   print("The fibonacci series of",x,"terms is")
   while i < x:
    print(f1)
    series=f1+f2                                         
    f1=f2                                                #updating first number
    f2=series                                            #updating secand number
    count +=1
   break
print("thank you")
