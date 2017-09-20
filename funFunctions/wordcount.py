# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(value):
    my_list = value.lower().split()
    my_dict = {}
    
    for word in my_list:
        if word in my_dict.keys():
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict


value = "I do not like it Sam I Am"

print(word_count(value))