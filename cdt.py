#wpt find how many time each and every element is present in given collection
cdt = ['a','b','i','k','i','s','h','o','r'],
d={}
values = 0
for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d) 
dict=d
max_values=max(dict.values())
max_keys = [(key, value) for key, value in dict.items() if value == max_values]
print(max_keys)


    
        
 #framekey method      
'''
cdt = eval(input())
d={}.framekey(cdt,0)            
for i in cdt:
   d[i]+=1
print(d)
'''

#count method
'''
cdt = eval(input())
d={}
for i in cdt;
   d[i]=cdt.count(i)
print(d)

iteration
1.using eval() to get any collection dt.

2.defining the dict to store the output in key value pairs

3.using for loop to iterate every element.

4.if else to check element in given collection or not.
    #check 'a' is in cdt and if its true than keys value increament by 1.

    #check 'b' is in cdt and if its true than keys value increament by 1.

    #check 'i' is in cdt and if its true than keys value increament by 1.

    #check 'k' is in cdt and if its true than keys value increament by 1.

    #check 'i' is in cdt and if its true than keys value increament by 1.

    #check 's' is in cdt and if its true than keys value increament by 1.

    #check 'h' is in cdt and if its true than keys value increament by 1.

    #check 'o' is in cdt and if its true than keys value increament by 1.

    #check 'r' is in cdt and if its true than keys value increament by 1.

5.print that dict after compleletion of loop.

'''