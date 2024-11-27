#wpt print the sum of numbers that are greater than 10
l = [1,99,44,33,10]
c=0
for i in l:
    
    if type(i) == int or int(i) > 10:
        c+=i
print(c)

'''
iteration....

1. using eval() to get any type of collection dt.

2.assuming that input is empyt

3.using for loop to iterate the input.
    #it will checking '1' type is int or int(i) is greater than 10 

    #it will checking '99' type is int or int(i) is greater than 10 and add to c

    #it will checking '44' type is int or int(i) is greater than 10 and add to c

    #it will checking '33' type is int or int(i) is greater than 10 and add to c

    #it will checking '10' type is int or int(i) is greater than 10


5.print the op outside the loop

'''