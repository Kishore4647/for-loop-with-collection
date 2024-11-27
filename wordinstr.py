#wpt print most repeated word in a given string
s = input("enter a string: ")
words = s.split()
c=0
mrw=" "
for i in words:
    if words.count(i) > c:
        c = words.count(i)
        mrw = i

print(mrw)

'''
iteration...

1.getting str as a input('bro hai bro')

2.split the given string as words.

3,assume that str is empty.

4.create a empty str to store the most repeated word.

5.iterate each element in the word using for loop.
   #first it will 'bro' as i and count how many times bro present in the string.

   #Next it will 'hai' as i and count how many times bro present in the string.
   

6.using count() the element in word 


'''