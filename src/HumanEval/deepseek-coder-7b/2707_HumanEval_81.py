
def numerical_letter_grade(grades):
    def grade_to_letter(grade):
        if grade == 4.0:
            return 'A+'
        elif grade > 3.7:
            return 'A'
        elif grade > 3.3:
            return 'A-'
        elif grade > 3.0:
            return 'B+'
        elif grade > 2.7:
            return 'B'
        elif grade > 2.3:
            return 'B-'
        elif grade > 2.0:
            return 'C+'
        elif grade > 1.7:
            return 'C'
        elif grade > 1.3:
            return 'C-'
        elif grade > 1.0:
            return 'D+'
        elif grade > 0.7:
            return 'D'
        elif grade > 0.0:
            return 'D-'
        else:
            return 'E'

    return [grade_to_letter(grade) for grade in grades]

# Test the function
