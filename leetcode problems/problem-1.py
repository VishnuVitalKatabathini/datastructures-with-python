class Solution:
    def romanToInt(self, s):
        self.s=s
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                     'M': 1000,'IV':4,'IX':9,'XL':40,
                     'XC':90,'CD':400,'CM':900}
        roman_num = list(s)
        print(roman_num)#example XVI=16,XXVII=27,MCMXCIV=1994
        int_val=0
        i=0
        while i<len(roman_num):
            j=i+1
            if j<len(roman_num):
                if roman_num[i]=='I'and roman_num[j]=='V':
                    int_val+=roman_val['IV']
                    i = i + 2
                elif roman_num[i]=='I' and roman_num[j]=='X':
                    int_val+=roman_val['IX']
                    i = i + 2
                elif roman_num[i]=='X' and roman_num[j]=='L':
                    int_val+=roman_val['XL']
                    i = i + 2
                elif roman_num[i]=="X" and roman_num[j]=='C':
                    int_val+=roman_val['XC']
                    i = i + 2
                elif roman_num[i]=="C" and roman_num[j]=='D':
                    int_val+=roman_val['CD']
                    i = i + 2
                elif roman_num[i]=="C" and roman_num[j]=="M":
                    int_val+=roman_val['CM']
                    i=i+2
                else:
                    int_val+=roman_val[roman_num[i]]
                    i=i+1
            else:
                int_val += roman_val[roman_num[i]]
                i=i+1

        print(int_val)

s=Solution()
s.romanToInt(input('enter roman digits'))

