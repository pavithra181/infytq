def factorial(number):
    a=number
    f=1
    if(a==0):
        f=1
    else:
        while(a>0):
            f=f*a
            a-=1
    return f

def find_strong_numbers(num_list):
    n=[]
    for j in range(0,(len(num_list))):
        temp=num_list[j]
        sum=0
        while(temp!=0):
            b=temp%10
            g=factorial(b)
            sum=sum+g
            temp=temp//10
        if(sum==num_list[j]):
            n.append(num_list[j])
    return n

       
num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
