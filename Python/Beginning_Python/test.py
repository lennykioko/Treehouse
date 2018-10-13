def num_teachers(teachers):
    return len(teachers.keys())

def num_courses(teachers):
    courses = 0
    for value in teachers.values():
        courses += len(value)
    return courses

def courses(teachers):
    courses = []
    for value in teachers.values():
        courses.extend(value)
    return courses

def most_courses(teachers):
    max_count = 0
    max_teacher = ""
    for item in teachers.items():
        if len(item[1]) > max_count:
            max_count = len(item[1])
            max_teacher = item[0]

    return max_teacher

def stats(teachers):
    stats = []
    for item in teachers.items():
        stat = [item[0], len(item[1])]
        stats.append(stat)

    return stats


print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections', 'Flask Basics']}))