import psutil
from operator import itemgetter
import collections
from collections import Counter 


socket_connections = psutil.net_connections()
#print "I am printing socket_connections\n",socket_connections
#print type(socket_connections)
socket_connection_tu = (socket_connections[1])
#print (socket_connection_tu[3])
final_dic={}

for a in socket_connections:
    if a.laddr != ('0.0.0.0', 0) and a.raddr != ():
    #print a.pid
        final_list=[a.laddr,a.raddr,a.status]
        if not a.pid in final_dic:
            final_dic[a.pid] = [final_list]
        else:
            final_dic[a.pid].append(final_list)
new_dic = {}
for keys in final_dic:
    new_dic[keys] = len(final_dic[keys])
    

for key, value in sorted(new_dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    for a in final_dic[key]:
        print "%s: %s" % (key, a)
        #print "\n"
print new_dic


#[list(group) for key,group in itertools.groupby(socket_connections,operator.itemgetter(1))]

