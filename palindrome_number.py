def palindrome(num):#121
    res=0
    temp=num
    while temp!=0:
        rem=temp%10
        res=res*10+rem
        temp=temp//10
    if num==res:
        return 'palindrome'
    else:
        return 'not palindrome'

print(palindrome(121))
print(palindrome(12222221))