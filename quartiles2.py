# DAY 1: Quartiles Statistics Challenge
# This challenge became more difficult as I thought through scenarios of both even and odd list lengths.
# I decided a function would be best to calculate the median of the main list, and its lower and upper halves.
# I realized the indices to include for each halve, differed with a starting list of even or odd length.
# This was easy to handle with a simple if statement, allowing me to continue using the median function
# but easily pass in differen indices.
# I have a new appreciation for the numpy median function! -which was not allowed for use in this challenge.


# a function which takes in a list and returns the median
def median(sublist):
    list_length = len(sublist)
    #even list
    if list_length % 2 == 0:
        upper_index = int(list_length / 2)
        lower_index = int(upper_index - 1)
        median = sum(sublist[lower_index:upper_index + 1])/2
        return median

    #odd list
    else:
        return sublist[int(list_length/2)]


#input
count = 10
input_values = '3 7 8 5 12 14 21 15 18 14'
values = list(map(int, input_values.split(" ")))
values.sort()
print(values)

#even list
if count % 2 == 0:
    middle = int(count/2)
    q2 = int(median(values))
    q1 = int(median(values[:middle+1]))
    q3 = int(median(values[middle:]))

#odd list
else:
    middle = int(count/2)
    q2 = median(values)
    q1 = int(median(values[:middle]))
    q3 = int(median(values[middle + 1:]))


#output
print(q1)
print(q2)
print(q3)


