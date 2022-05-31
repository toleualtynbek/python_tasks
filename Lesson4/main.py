
import sys
a = sys.argv[1:]

k = [int(x) for x in a]
result = k[0] * k[1] + k[2]
print("Employee salary: ", result)