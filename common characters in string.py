def find_common_characters(msg1,msg2):
    msg1=msg1.replace(" ",'')
    msg2=msg2.replace(" ",'')
    common=''
    a=len(msg1)
    b=len(msg2)
    for i in range(0,a):
        for j in range(0,b):
            if msg1[i]==msg2[j]:
                common+=msg1[i]
                break
    if(common!=''):
        l1=[]
        list1=[]
        for k in common:
            if k not in l1:
                l1.append(k)
                list1.append(k)
        common=''.join(list1)
    if common=='':
        return -1
    else:
        return common
                
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
