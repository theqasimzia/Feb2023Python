with open ("data.txt", "r") as f:
    data = [float(line.strip()) for line in f]

print ("The minimum value is: ", min(data))
print ("The maximum value is: ", max(data))
print ("The sum is ", sum(data))
print ("The mean is ", sum(data)/len(data))    