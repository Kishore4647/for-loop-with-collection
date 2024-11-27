#wpt find how many consonant are in given string
s ='kishore'
s = s.lower()
v = "aeiou"
c =0
for i in s:
    if  not i.isdigit() and i not in v :
        c+=1
print(c)

'''
iteration.....

1,getting str as input

2.converting all char into lower

3.using for loop to iterate
    #check 'k' is not digit and not a vowel.

    #check 'i' is not digit and not a vowel.

    #check 's' is not digit and not a vowel.

    #check 'h' is not digit and not a vowel.

    #check 'o' is not digit and not a vowel.

    #check 'r' is not digit and not a vowel.

    #check 'e' is not digit and not a vowel.

5.print output outside the loop
'''