#Day 0 of coding w/ statistics on hackerrank.com
#Goal: Compute mean, median, and mode of the input.
#It was easy to use numpy to compute the mean and median.
#I was not aware that numpy did not have a 'mode' function.
#Version 1 of my solution attempted to use 2d arrays to add up the occurences of each item.
#After further thought I took a more iterative approach for a much cleaner solution.
#Using the list.count function I simply looped through the list, recording the max count and value which indicated the mode.
#I like this solution at lot better as it is much more organic in the algorithm.
import numpy as np 


array_length = 20
input_string = '6392 51608 71247 14271 48327 50618 67435 47029 61857 22987 64858 99745 75504 85464 60482 30320 11342 48808 66882 40522'
input_values = list(map(int, input_string.split(" ")))
input_values.sort()

values = np.array(input_values).astype(np.int)


mean = np.mean(values)
median = np.median(values)
mode_value = 0
mode_count = 0

for value in input_values:
    current_count = input_values.count(value)
    if current_count > mode_count:
        mode_value = value
        mode_count = current_count

print(mean)
print(median)
print(mode_value)