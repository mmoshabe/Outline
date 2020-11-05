

def create_outline():
    """
    FUnction that Prints Courses and problems
    """
    
    course_topics = {"Introduction to python", "Tools of the Trade", "How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules"}
    course_topics = list(course_topics)
    print("Course topics:")
    for topic in course_topics:
        print('* ' + topic)
    problem_list = ["Problem 1", "Problem 2", "Problem 3"]
    problems = {}
    print("Problems:")
    for topic in course_topics:
        problems.update({topic : problem_list})
        print('* ' + topic + ' : ' + problem_list[0] +', ' + problem_list[1] + ', ' + problem_list[2])
    # print(problems)
    #for i in problems:
    #    print('* ' + i + ' : ' + problem_list[0] +', ' + problem_list[1] + ', ' + problem_list[2])
    student_name = ("Helena","Ruth", "Nyari", "Verena", "Nyari")
    for 
        


if __name__ == "__main__":
    create_outline()
