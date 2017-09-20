
teachers = {'Keegan': ['math', 'english'], 'Ang': ['art']}

def courses(teachers):
    total = 0

    for teacher in teachers:
        total += len(teachers[teacher])
    return total



print(courses(teachers))

