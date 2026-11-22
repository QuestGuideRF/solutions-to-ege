alf =sorted ('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alf [:27 ]:
    s =int ('123'+x +'24',27 )+int ('135'+x +'78',27 )
    if s %26 ==0 :
        print (s //26 )