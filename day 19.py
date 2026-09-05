'''
MODULES
---------
A module is a python file(.py) that written using function, variable, operations, etc.
import math
print(math.pow(2,3))

They are 2 types
1. buit-in modules
   Modules are developed by programmer and those comes with installation
  ex:-
  math
  import math
  print(math.pow(2,3))
  
  os
  import os
  print(os.getcwd())

  sys
  import sys
  print(sys.path)
  print(sys.version)
  
  randam
  import random
  print(random.randint(1000,9999))
  
2. user defined modules
   
importing specific function from the module
syntax----> from module import function

from sneha import add_
print(add_(5,7))

from sneha import sub
print(sub(5,7))

from sneha import pw
print(pw(5,7))

using alias name
-------------
import sneha as sn
print(sn.add_(5,7))
