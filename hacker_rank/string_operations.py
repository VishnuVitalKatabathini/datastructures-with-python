def string_return(s):
    s.lower()
    numbers=[0,1,2,3,4,5,6,7,8,9]
    alphabets='abcdefghijklmnopqrstuvwxyz'
    num=[]
    string=''
    res=''
    for i in s:
        if i.isdigit():
            num.append(int(i))
        else:
            string+=i
    num=sorted(num)
    print(num)
    for i in numbers:
        if i not in num:
            res=res+str(i)
    for i in alphabets:
        if i not in string:
            res+=i
    print(res)

string_return(input('enter a string'))


