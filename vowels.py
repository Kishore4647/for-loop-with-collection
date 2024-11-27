#wpt find how many vowels are in given string
s =input("enter a string:")
s = s.lower()
v = "aeiou"
c =0
for i in s:
    if i in v:
        c +=1

print(c)

'''
iteration...

1.getting str as the input('abi')

2.converting str into lowercase compare with vowels string.

3.assuming that str is empty.

4.iterate str element using for loop.

5.check that ele is in vowels .
     #it will check 'a' is in v if it is true than execute the statement.

     #it will check 'b' is in v if it is true than execute the statement.

     #it will check 'i' is in v if it is true than execute the statement.

6.if it is in vowels increament by 1.

7.print the final output.

'''