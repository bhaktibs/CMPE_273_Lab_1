import psutil
from operator import itemgetter
import collections
from collections import Counter 


socket_connections = psutil.net_connections(kind="tcp")

final_dic={}

for a in socket_connections:
    if a.laddr != ('0.0.0.0', 0) and a.raddr != ():
        laddr_split=list(a.laddr)
        raddr_split=list(a.raddr)
        laddr_final = laddr_split[0]+"@"+str(laddr_split[1])
        raddr_final=raddr_split[0]+"@"+str(raddr_split[1])
        final_list=[laddr_final,raddr_final,a.status]
        if not a.pid in final_dic:
                final_dic[a.pid] = [final_list]
        else:
                final_dic[a.pid].append(final_list)
    new_dic = {}
for keys in final_dic:
    new_dic[keys] = len(final_dic[keys])   
print '"Pid","laddr","raddr","Status"'
for key, value in sorted(new_dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    for a in final_dic[key]: 
        print '"%s", "%s", "%s", "%s"' % (key,a[0],a[1],a[2]) 
   

