def grade_text(grade):

    if grade < 3:
        return 'Fail'
    elif grade < 3.50:
        return 'Poor'
    elif grade < 4.50:
        return 'Good'
    elif grade < 5.50:
        return 'Very Good'
    else:
        return 'Excellent'


grade_data = float(input())
print(grade_text(grade_data))
