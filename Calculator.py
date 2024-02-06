num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print("Choose option 1 for Add\n Choose option 2 for sub\n Choose option 3 for mul \n Choose option 4 for div \n")
option= int(input("Enter the option:"))
if(option==1):
    result=num1+num2
    print('Answer is',result)
elif(option==2):  
    result=num1-num2
    print('Answer is',result)
elif(option==3):   
    result=num1*num2
    print('Answer is',result)
elif(option==4):
    if(num2==0):
        print("Not possible")
    else:    
        result=num1/num2
        print('Answer is',result)
else:
   print("Invaild")
