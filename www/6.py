import numpy as np
var=np.empty((10,10),dtype='str')
kot=np.array(list('kot'))
kolo=np.array(list('kolo'))
np.put(var,[2,1,0],kot)
np.put(var,[11,21,31,41],kolo)
tkac=np.array(list('tkac'))
np.put(var,[0,11,22,33],tkac)

print(var)

