#count how many odd and even digit are in given string
s = 'a2b4i1'
c = 0
d = 0
for i in s:
    if i.isdigit():
         
        if  int(i)%2==0:
            c+=1
        else:
            d+=1
print(c,"even numbers")
print(d,"odd numbers")
'''
iteerations...

1.getting input as str.

2.assume that odd and even num in a str is 0.

3.using for loop to iterate in str.

4.checking the element is int type.

    #it will take and check a is digit return false

    #it will take and check 2 is digit than again check int(1) IS even or odd

    #it will take and check b is digit return false

    #it will take and check 4 is digit than again check int(1) IS even or odd

    #it will take and check i is digit return false.

    # #it will take and check 1 is digit than again check int(1) IS even or odd


5.if it is in int than check the evevn or odd.

6.if it is ture than increment  c by 1 else d by 1
  '''      
   

        
        