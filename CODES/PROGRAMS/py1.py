#Prog 1
'''num=int(input("Enter a number:"))
if((-2147483648 <= num <= 2147483648)and(num%2==0)):
    print("Even Number!")
else:
    print("Odd NUmber!")
'''
#prog 2
'''h,m,s=map(int,input("Enter Time in HH:MM:SS:\n").split())
if(h<=12 and m<60 and s<60):
    print(h,":",m,":",s, "Valid Time!")
else:
    print(h,":",m,":",s,"Invalid Time!")
'''
#prog 3
'''n1,n2,n3=map(int,input("Enter 3 Numbers:").split())
l=[n1,n2,n3]
l.sort()
if((-1000 <= n1, n2, n3 <=1000) and (n1!=n2!=n3)):
   print(max(l),">",l[-2],">",l[-3])
elif((n1==n2==n3) or ((n1==n2)or(n1==n3))):
    print("Input is not Unique!")
'''
#prog 4
'''
d,m,y=map(int,input("Enter a random date in DD:MM:YYYY:\n").split())
if(d<=31 and m<=12 and 0<= y <=9999):
    print(d,":",m,":",y, "Valid Date!")
else:
    print(d,":",m,":",y,"Invalid Date!")
'''
