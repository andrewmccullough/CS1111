import urllib.request

def return_courses (department):

    with urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + department) as f:
        html = f.read().decode("utf-8")
        courses = html.split("\n")
        courses.pop()

    return courses

def instructors (department):

    instructors_list = []

    courses = return_courses (department)

    for course in courses:
        course = course.split("|")
        instructor = course[4]

        if "+" in instructor:
            instructor = instructor[:-2]

        if instructor not in instructors_list:
            instructors_list.append(instructor)

    instructors_list.sort()

    return instructors_list

def class_search (dept_name, has_seats_available = True, level = None, not_before = None, not_after = None):

    courses = return_courses (dept_name)

    matches = []

    for course in courses:
        course = course.split("|")

        if has_seats_available == True:

            if course[15] >= course[16]:
                continue

        if level is not None:

            if int(course[1][0]) != int(str(level)[0]):
                continue

        if not_before is not None:

            if int(course[12]) < not_before:
                continue

        if not_after is not None:

            if int(course[12]) > not_after:
                continue

        matches.append(course)

    return matches
