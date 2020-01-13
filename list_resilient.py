'''
Below code finds out the lowest resilience till 'n' (as given as 100 in the for loop)
'''

from datetime import datetime
import math

tim=datetime.now()

min_resilient = 1
for input_num in range(2, 100, 2):
    non_fractionals = [i for i in range(input_num) if math.gcd(input_num, i) == 1]            
    resilience = len(non_fractionals)/(input_num-1)
    (exec('min_resilient=resilience'), print('Minimum resilient: ', input_num, 'at', min_resilient)) if min_resilient > resilience else 1
    
print('\nTime spent:', datetime.now() - tim)

