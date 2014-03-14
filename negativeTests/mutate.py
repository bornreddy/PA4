import sys
import random
lines = sys.__stdin__.readlines()
indices = [ i for i in range(len(lines)) if lines[i] == "identifier\n" ]
for i in range(100): 
  scrambled = list(lines) 
  scrambled[random.choice(indices) + 2] = \
        scrambled[random.choice(indices) + 2] 
  f = open('random' + str(i) + '.cl-ast', 'w') 
  for line in scrambled: 
    f.write(line)
  f.close()
