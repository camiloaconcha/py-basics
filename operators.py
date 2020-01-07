
import math

swallow_limit = 60 / 3
swallow_per_cherry = 8 / swallow_limit

# example 2

perc = 1/3

coco_wt = 1450

macaw_wt = 900

macaw_limit = macaw_wt * perc

num_macaws = coco_wt / macaw_limit

#print('Number of macaws \n' + str(num_macaws))

print(f'Number of macaws \n {math.ceil(num_macaws)}')
