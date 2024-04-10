def calculate_total_score(scores):
    return sum(scores)

def calculate_average_score(scores):
    return sum(scores) / len(scores)

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def calculate_rank(scores):
    sorted_scores = sorted(scores, reverse=True)
    rank_dict = {score: index + 1 for index, score in enumerate(sorted_scores)}
    return [rank_dict[score] for score in scores]

def insert_student(students, student_data):
    students.append(student_data)

def delete_student_by_id(students, student_id):
    for student in students:
        if student['학번'] == student_id:
            students.remove(student)
            break

def delete_student_by_name(students, name):
    for student in students:
        if student['이름'] == name:
            students.remove(student)
            break

def search_student_by_id(students, student_id):
    for student in students:
        if student['학번'] == student_id:
            return student
    return None

def search_student_by_name(students, name):
    for student in students:
        if student['이름'] == name:
            return student
    return None

def sort_students_by_total_score(students):
    return sorted(students, key=lambda x: x['총점'], reverse=True)

def count_students_above_80(students):
    count = 0
    for student in students:
        if student['평균'] >= 80:
            count += 1
    return count

def display_all_students(students):
    print("전체 학생 정보")
    print("---------------")
    print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\t등수")
    print("---------------")
    for student in students:
        print(f"{student['학번']}\t{student['이름']}\t{student['영어']}\t{student['C언어']}\t{student['파이썬']}\t"
              f"{student['총점']}\t{student['평균']:.2f}\t{student['학점']}\t{student['등수']}")

def input_student_data():
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    eng_score = float(input("영어 점수를 입력하세요: "))
    c_score = float(input("C언어 점수를 입력하세요: "))
    python_score = float(input("파이썬 점수를 입력하세요: "))

    total_score = calculate_total_score([eng_score, c_score, python_score])
    average_score = calculate_average_score([eng_score, c_score, python_score])
    grade = calculate_grade(average_score)
    rank = 0
    return {'학번': student_id, '이름': name, '영어': eng_score, 'C언어': c_score, '파이썬': python_score,
            '총점': total_score, '평균': average_score, '학점': grade, '등수': rank}

# 학생 정보 입력
students = []
for i in range(5):
    student_data = input_student_data()
    students.append(student_data)

# 등수 계산
scores = [student['총점'] for student in students]
ranks = calculate_rank(scores)
for student, rank in zip(students, ranks):
    student['등수'] = rank

# 메뉴 표시
while True:
    print("\n====== 메뉴 ======")
    print("1. 학생 정보 출력")
    print("2. 학생 추가")
    print("3. 학생 삭제")
    print("4. 학생 검색 (학번)")
    print("5. 학생 검색 (이름)")
    print("6. 학생 성적 정렬")
    print("7. 평균 80점 이상 학생 수")
    print("8. 종료")
    print("=================")

    choice = input("메뉴를 선택하세요: ")

    if choice == '1':
        display_all_students(students)

    elif choice == '2':
        student_data = input_student_data()
        insert_student(students, student_data)
        print("학생 정보가 추가되었습니다.")

    elif choice == '3':
        delete_option = input("학생 삭제 옵션을 선택하세요 (1. 학번, 2. 이름): ")
        if delete_option == '1':
            student_id = input("삭제할 학생의 학번을 입력하세요: ")
            delete_student_by_id(students, student_id)
        elif delete_option == '2':
            name = input("삭제할 학생의 이름을 입력하세요: ")
            delete_student_by_name(students, name)
        else:
            print("올바른 옵션을 선택해주세요.")

    elif choice == '4':
        student_id = input("검색할 학생의 학번을 입력하세요: ")
        searched_student_by_id = search_student_by_id(students, student_id)
        if searched_student_by_id:
            print("학번으로 조회된 학생:", searched_student_by_id)
        else:
            print("해당 학번의 학생이 존재하지 않습니다.")

    elif choice == '5':
        name = input("검색할 학생의 이름을 입력하세요: ")
        searched_student_by_name = search_student_by_name(students, name)
        if searched_student_by_name:
            print("이름으로 조회된 학생:", searched_student_by_name)
        else:
            print("해당 이름의 학생이 존재하지 않습니다.")

    elif choice == '6':
        sorted_students = sort_students_by_total_score(students)
        print("총점을 기준으로 정렬된 학생 목록:")
        display_all_students(sorted_students)

    elif choice == '7':
        students_above_80 = count_students_above_80(students)
        print("평균이 80점 이상인 학생 수:", students_above_80)

    elif choice == '8':
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력해주세요.")
