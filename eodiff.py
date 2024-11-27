#wpt absoulte diff btw even digit sum and odd digit sum
s = '12948'
c =0
d =0
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            c+=int(i)
        else:
            d+=int(i)
print(abs(c-d))
'''
iterations....

1.geting str input()

2.using for loop for itreration

3.checking wheather it is a digit or not.
    #it will take the int(1) and check odd or even.

    #it will take the int(2) and check odd or even.

    #it will take the int(9) and check odd or even.

    #it will take the int(4) and check odd or even.
    
    #it will take the int(8) and check odd or even.

4.condition true do addition of element.

5.print the absolute diff btw c and d 
'''