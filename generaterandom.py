import random

with open ("data.txt", "w") as f:
    for i in range (10):
        data_point = random.uniform(0.0, 100.0)
        f.write(str(data_point) + "\n")
                
                