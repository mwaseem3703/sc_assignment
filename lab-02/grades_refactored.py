def read_grades(file_path):
    grades = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) > 1:
                grades[parts[0]] = [int(x) for x in parts[1:]]
    return grades


def calculate_grade(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    else:
        grade = 'F'
    return average, grade


def print_main_report(grades):
    print("--- Main Report ---")
    for student, scores in grades.items():
        average, grade = calculate_grade(scores)
        print(f"Student: {student}, Avg: {average}, Grade: {grade}")


def print_honor_roll(grades):
    print("--- Honor Roll ---")
    for student, scores in grades.items():
        _, grade = calculate_grade(scores)
        if grade == 'A':
            print(f"Honor Roll: {student}")


def process_grades(file_path):
    grades = read_grades(file_path)
    print_main_report(grades)
    print_honor_roll(grades)


if __name__ == "__main__":
    process_grades("data.txt")