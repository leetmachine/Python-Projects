def combiner(values):

    combine = ''
    sum = 0

    for value in values:
        if isinstance(value, (int, float)):
            sum += value
        elif isinstance(value, str):
            combine += value


    return combine + str(sum)

print(combiner(["apple", 5.2, "dog", 8]))