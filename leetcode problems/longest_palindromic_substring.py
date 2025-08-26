from operator import indexOf

from linear_search import index_value


def longestPalindrome(s):
    sub_string = {}
    for i in range(len(s)+1):
        for k in range(i):
            substring=s[k:i]
            rev=substring[-1::-1]
            if substring==rev:
                sub_string[len(substring)]=substring
    print(sub_string)
    m=max(sub_string.keys())
    print(sub_string[m])

longestPalindrome('cbbd')
