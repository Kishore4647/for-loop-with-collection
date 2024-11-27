#wpt print lengtiest word in a given str
s = 'abi kishore'
word = s.split()
lw = ""
c=0
for i in word:
    if len(i) > c:
        c = len(i)
        lw = i
print(lw)

#using max()
'''
print(max(words,key=len)) 

 by default max() will return value based on the ascii value

 iteration....

 1.getting str as input.

 2.split the ginen word by space

 3.define a empyt str and c =0.

 3.using for loop to iterate through word

 4.checking the len word and compare every word
 
    # it will take 'abi' and check the length 

    #it will take 'kishore' and check the length if 'kishore' len is > 'abi' len than asign 'kishore' to lw.

 5.print the op outside the loop,

'''