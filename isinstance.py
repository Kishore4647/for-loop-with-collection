#wpt print the sum of digits in the list
l = ['a',2,5,9]
c=0
for i in l:
    if type(i)==int:
        c+=i
print(c)

'''l = eval(input())
c=0
for i in l:
    if isinstance(i,int):
        c+=i
print(c)'''
'''
1,eval() to get input

2.checking the type of elemrnt.

    #it will take 'a' and check the type is int or not

    #it will take 2 and check the type is int or not

    #it will take 5 and check the type is int or not
    
    #it will take 9 and check the type is int or not

3. if type is int then add element to the c

4.print outside the loop.
'''