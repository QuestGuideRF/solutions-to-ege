from ipaddress import *
k =0
for ip in ip_network ('112.208.0.0/255.255.128.0',0 ):
    ip_2 =f'{ip :b}'
    if ip_2 .count ('1')%11 ==0 :
        k +=1
print (k )