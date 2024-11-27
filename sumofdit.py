s = input('enter the string:')
c = 0
for i in s:
    if i.isdigit():  # check i is digit
        c+=int(i) #typecast str to int
print(f"the sum of digit in string:{c}")

'''
iteration....

1.getting str as input('abi123')

2.assuming that given str is empty.

3.iterate every ele in str using for loop.

4.check ele is digit .
    #it will take 'a' and check it is digit and if it is true than it will execute the statement.

    #it will take 'b' and check it is digit and if it is true than it will execute the statement.

    #it will take 'i' and check it is digit and if it is true than it will execute the statement.

    #it will take '1' and check it is digit and if it is true than it will execute the statement.

    #it will take '2' and check it is digit and if it is true than it will execute the statement.
    
    #it will take '3' and check it is digit and if it is true than it will execute the statement.


5.if it is true than typecast i into int and add to c.

6.print the sum of all digit.
'''