#wpt to find max number in given list of numbers
'''s=eval(input("enter a list"))
s.sort(reverse=True)
print(s[0])
'''
l=[1,20,4,10]
max=0
for i in l:
    if i>max:
        max=i
print(max)

'''
1.getting input as eval to get any collection 

2.assuming that  given collection is empyt.

3.using for loop in given input.

4.checking that element is max.
    #it will take 1 and check it is max and it is max than it is asigned to max.

    #it will take 20 and check it is max and it is max than it is asigned to max.

    #it will take 4 and check it is max and it is max than it is asigned to max.
    
    #it will take 10 and check it is max and it is max than it is asigned to max.

5.print the max element.

'''