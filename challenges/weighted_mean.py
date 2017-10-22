#DAY 0: Weighted Mean Statistics challenge
#This challenge was easy to complete.
#My first thought was to simply use numpy's flexibility to multiply 2 arrays for the solution. (commented below)
#Hackerrank did not allow the use of numpy so I came up with this implementation.
#This challenge just required multiplying each value * its weight, and summing the totals for a mean.
#My only roadblock was forgetting to format the output as required by the challenge.

input_length = 5
input_values = '10 40 30 50 20 10 40 30 50 20'
input_weights = '1 2 3 4 5 6 7 8 9 10'

values = list(map(int, input_values.split(" ")))
weights = list(map(int, input_weights.split(" ")))

weighted_values = []

for index, value in enumerate(values):
    weighted_values.append(value * weights[index])

print(weighted_values)

print("{0:0.1f}".format(sum(weighted_values) / sum(weights)))


###Same challenge using numpy
#import numpy as np
#
#input_length = 5
#input_values = '10 40 30 50 20'
#input_weights = '1 2 3 4 5'
#
#values = np.array(input_values.split(" ")).astype(np.int)
#weights = np.array(input_weights.split(" ")).astype(np.int)
#
#print(sum(values * weights) / sum(weights))