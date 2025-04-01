import random
import my_number
nr_random = random.randint(1,45)
print(nr_random)
print(my_number.my_favorite_nr)

nr_float = random.random() * 10
print(nr_float)

nr_float_index = random.uniform(3,25)
print(nr_float_index)

nr_float_head_or_tail=random.randint(0,1)
if(nr_float_head_or_tail==0):
    print("Head")
else:
    print("Tail")