#wpt to print most reapted char in given string
s = 'abi kishore'
d={}
max=0
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for i in d:
    if int(d[i]) > max:
        max = d[i]
        print(f'{i} is repeated {max} times')
'''
iteration....

1.getting input as 'abi kishore'

2.using empyt dict to store output in key and value pairs.

3.using for loop to iterate the given collection.

4.if else statement to check the repeatation of element
    #it will take a and check it is in d , if it is in d than  a value increment by 1.
    #it will take b and check it is in d , if it is in d than  b value increment by 1.
    #it will take i and check it is in d , if it is in d than  i value increment by 1.
    #it will take '' and check it is in d , if it is in d than  '' value increment by 1.
    #it will take k and check it is in d , if it is in d than  k value increment by 1.
    #it will take i and check it is in d , if it is in d than  i value increment by 1.
    #it will take s and check it is in d , if it is in d than  s value increment by 1.
    #it will take h and check it is in d , if it is in d than  h value increment by 1.
    #it will take o and check it is in d , if it is in d than  o value increment by 1.
    #it will take r and check it is in d , if it is in d than  r value increment by 1.
    #it will take e and check it is in d , if it is in d than  e value increment by 1.


5.for loop to get the highest value in dict

6.print the highest value
'''