import sys

def process_grades(file_path):
    d = {} 
    
    # 1. Input parsing
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) > 1:
                d[parts[0]] = [int(x) for x in parts[1:]]
    
    # 2. Calculation and primary report
    print("--- Main Report ---")
    for student, scores in d.items():
        total = 0
        for s in scores:
            total += s
        avg = total / len(scores)
        
        if avg >= 90: 
            grade = 'A'
        elif avg >= 80: 
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        else: 
            grade = 'F'
            
        print(f"Student: {student}, Avg: {avg}, Grade: {grade}")

    # 3. Honor roll with duplicated grade-boundary logic
    print("--- Honor Roll ---")
    for student, scores in d.items():
        total = sum(scores)
        avg = total / len(scores)
        
        if avg >= 90: 
            grade = 'A'
        elif avg >= 80: 
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        else: 
            grade = 'F'
            
        if grade == 'A':
            print(f"Honor Roll: {student}")

if __name__ == "__main__":
    process_grades("data.txt")