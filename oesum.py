#wpt find sum of even and odd dig present in a string 
s="1a2b3i"
c =0
d = 0
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            c+=int(i)
        else:
            d+=int(i)
                
print("sum of even digit is",c)
print("sum of odd digit is",d)

'''
iterations....

1.getting the input as str.

2.assume that odd and even num in a str is 0.

3.using for loop to iterate in str.

4.checking the element is int type.
    #it will take and check 1 is digit than again check int(1) IS even or odd

    #it will take and check a is digit return false

    #it will take and check 2 is digit than again check int(1) IS even or odd

    #it will take and check b is digit return false

    #it will take and check 3 is digit than again check int(1) IS even or odd

    it will take and check 1 is digit return false.


6.add the element to c if it is even else add to d (odd)

'''