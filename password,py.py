d = {'kishore':'madurai','sundar':'selur'}
username = input('enter username: ') 
if username in d :                    #check given username is avail in dict
    password = input('enter password:')
    if d[username] == password:          #check given username is match password
        print('login successfully')

    else:
        print('password is incorrect')

else: 
    print('Username is not available')


'''
iteration....

1.creating the dict with name as userid and palce as password.

2.getting username form the user. and user name is kishore.

3.using nested if , first check the kishore is in dict or not. if not than go to outer else part

4.if it is true than get the password. and password is 'madurai'

5.check that userid and password is matcing or not. it will print 'login successfully'.

6.if it is false print --> password is wrong

'''