from ipaddress import *
for mask in range (33 ):
    net =ip_network (f'192.75.64.98/{mask }',0 )
    if str (net .network_address )=='192.75.64.0':
        print (mask )