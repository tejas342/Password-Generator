def password(length):
    import random

    ch = "abcdefghijklmnopqrstuvwxyz"
    CH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    num = "0123456789"
    sym = "@#$&!*+"
    cmn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$&!*+abcdefghijklmnopqrstuvwxyz"

    if(length == 1):
        pw = random.choice(cmn)
        return pw
    elif(length == 2):
        pw = random.choice(CH) + random.choice(sym)
        return pw
    elif(length == 3):
        pw = random.choice(num) + random.choice(CH) + random.choice(sym)
        return pw
    elif(length == 4):
        pw = random.choice(ch) + random.choice(num) + random.choice(sym) + random.choice(CH)
        return pw
    elif(length > 4 and length < 100):
        pw = random.choice(CH) + random.choice(num) + random.choice(sym) + random.choice(ch)
        for i in range(length-4):
            pw += random.choice(cmn)
        return pw
    elif(length >= 100):
        pw=''
        q=input("You want password which has length > 100, It may take some time would you like to cotinue ? (y/n) : ")
        if(q == 'y' or q == 'Y'):
            for i in range(length):
                pw += random.choice(cmn)
            return pw
        else:
            return pw
    else:
        print("OOPS YOU ENTERED INCORRECT LENGTH !!")
        return ''

    
print("THIS PROGRAM WILL GENERATE STRONG PASSWORD FOR YOU \n\t\tcreated by Tejas Prajapati\n\n")
flag=1
while(flag):
    length = int(input("Please enter length(integer) for your password : "))
    if length < 1:
        a=int(input("\n\nLength of password must be greater than 0 \nPlease enter new length for your password : "))
        print(password(a))
        flag = input('\n\nDo you want to generate more password y/n : ')
        if(flag != 'y' and flag != 'Y'):
            print("\n\nTHANK YOU!!")
            b=input()
            break
            
    else:
        print(password(length))
        flag = input('\n\nDo you want to generate more password y/n : ')
        if(flag != 'y' and flag != 'Y'):
            print("\n\nTHANK YOU!!")
            b=input()
            break
