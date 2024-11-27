#wpt print even num in given str.
s = "abi321"
c = 0
for i in s:
    if i.isdigit():
        if int(i)%2 == 0:
            c+=int(i)

print(f"sum of even digit in given string:{c}")
'''
1.getting str input()
2.using for loop 
3.checking the char using isdigit
4.checking it is even or not.
    #it will take 'a' and check it is digit and is it even
    #it will take 'b' and check it is digit and is it even
    #it will take 'i' and check it is digit and is it even
    #it will take '1' and check it is digit and is it even
    #it will take '2' and check it is digit and is it even
    #it will take '3' and check it is digit and is it even

5.inrement the value if true.
5,print outside the loop.
'''