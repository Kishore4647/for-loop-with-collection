#wpt find how many special character are present in given string
s="a$b#i"
c=0
for i in s:
    if  not i.isalnum() :
        c+=1
print(c)

'''
iteration....

1. getting str as input('a$b#i')

2.assume that given str is empty.

3.iterating each element in for loop.

4.checking that element is not alphabet.

    1.it will take 'a' as i and check it is alpha numeric or not, if its not than execute the statement.

    2.it will take '$' as i and check it is alpha numeric or not, if its not than execute the statement.

    3.it will take 'b' as i and check it is alpha numeric or not, if its not than execute the statement.

    4.it will take '#' as i and check it is alpha numeric or not, if its not than execute the statement.

    5.it will take 'I' as i and check it is alpha numeric or not, if its not than execute the statement.

5.if it true than increament by 1.

6.print the final output.
'''