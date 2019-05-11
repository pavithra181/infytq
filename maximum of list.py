def find_max(num1, num2):
    max_num=-1
    list1=[]
    if(num1<num2):
        for num in range(num1,num2+1):
            temp=num
            sum_of_digits=0
            while(temp!=0):
                a=temp%10
                sum_of_digits=(sum_of_digits+a)
                temp=(temp//10)
            if(sum_of_digits%3==0):
                if((num>9)and(num<100)):
                    if(num%5==0):
                        list1.append(num)
                else:
                    max_num=-1
        if(list1==[]):
            max_num=-1
        else:
            max_num=max(list1)
    else:
        max_num=-1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
