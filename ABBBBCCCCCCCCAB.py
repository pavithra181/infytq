
def encode(message):
    count=1
    a=(len(message)-1)
    st=""
    for i in range(0,a):
        if message[i]==message[i+1]:
            count=count+1
        else:
            x=str(count)
            y=message[i]
            st=st+x+y
            count=1
        if((i+1)==a):
            x=str(count)
            y=message[i+1]
            st=st+x+y
    if (a==0):
        x=str(count)
        y=message[0]
        st=st+x+y
        
    
        
    return st

    
        
    
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
