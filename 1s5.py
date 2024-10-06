def find_students_with_max_score(input_string):
    student_scores = []
    i = 0

    while i < len(input_string):
        if input_string[i:i+8] == 'student_': 
            student_id = input_string[i+8:i+11]  
            i += 11  
            score = ""

            while i < len(input_string) and input_string[i].isdigit():
                score += input_string[i]
                i += 1

            student_scores.append((student_id, int(score)))
        else:
            i += 1

    max_score = max(score for _, score in student_scores)

    max_score_students = [student_id for student_id, score in student_scores if score == max_score]

    print('-'.join(max_score_students))
    
input_string = input("Введите строку с номерами студентов и их баллами: ")
find_students_with_max_score(input_string)
