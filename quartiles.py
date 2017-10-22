
#a function which takes in a list and returns the median
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

#the middle index of the starting list
middle = int(count/2)

#the median of the first half of the list
q1 = int(median(values[:middle]))

#the median on the main list
q2 = median(values)

#the median on the second half of the list
q3 = int(median(values[middle + 1:]))


#output
print(q1)
print(q2)
print(q3)


