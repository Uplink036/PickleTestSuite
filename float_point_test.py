import pickle
import random
from decimal import *

getcontext().prec = 32
a = Decimal(0.61287368787123)
b = Decimal(0.01231234556892)
c = a + b
print(c)

c1 = pickle.dumps(a)

c2 = pickle.loads(a)

print(c2)
print(c)
