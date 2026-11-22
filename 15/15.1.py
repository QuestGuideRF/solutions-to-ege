def F (A ,x ):
    return (not (x %A ==0 ))<=((x %28 ==0 )<=(not (x %49 ==0 )))
for A in range (1 ,1000 ):
    if all (F (A ,x )for x in range (1 ,1000 )):
        print (A )