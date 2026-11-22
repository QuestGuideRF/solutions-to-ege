a =[int (i )for i in open ('17')]
mx_39 =max ([i for i in a if 999 <abs (i )<10000 and abs (i )%100 ==39 ])
otvet =[]
for i in range (len (a )-1 ):
    if ((999 <abs (a [i ])<10000 )+(999 <abs (a [i +1 ])<10000 ))==1 :
        if (a [i ]+a [i +1 ])**2 <=mx_39 **2 :
            otvet .append (a [i ]+a [i +1 ])
print (len (otvet ),max (otvet ))