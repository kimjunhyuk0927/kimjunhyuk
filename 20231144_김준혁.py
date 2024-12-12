import random

# 학생 데이터 생성
def generate_students(num_students=30):
    """30명의 무작위 학생 데이터를 생성 (이름 중복 방지)."""
    students = []
    used_names = set()
    while len(students) < num_students:
        name = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        if name in used_names:
            continue
        used_names.add(name)
        students.append({
            "이름": name,
            "나이": random.randint(18, 22),
            "성적": random.randint(0, 100),
        })
    return students

# 정렬 알고리즘 설정
def selection_sort(data, key, reverse=False):
    """선택 정렬 알고리즘"""
    for i in range(len(data)):
        target_index = i
        for j in range(i + 1, len(data)):
            if (data[j][key] < data[target_index][key]) != reverse:
                target_index = j
        data[i], data[target_index] = data[target_index], data[i]
    return data

def insertion_sort(data, key, reverse=False):
    """삽입 정렬 알고리즘"""
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and (current[key] < data[j][key]) != reverse:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
    return data

def quick_sort(data, key, reverse=False):
    """퀵 정렬 알고리즘"""
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if (x[key] <= pivot[key]) != reverse]
    greater = [x for x in data[1:] if (x[key] > pivot[key]) != reverse]
    return quick_sort(less, key, reverse) + [pivot] + quick_sort(greater, key, reverse)

def radix_sort(data, reverse=False):
    """기수 정렬 알고리즘 (성적 전용)."""
    max_grade = max(student["성적"] for student in data)
    exp = 1
    while max_grade // exp > 0:
        buckets = [[] for _ in range(10)]
        for student in data:
            buckets[(student["성적"] // exp) % 10].append(student)
        data = [student for bucket in buckets for student in bucket]
        exp *= 10
    return data[::-1] if reverse else data

# 유틸리티 함수
def display_students(students, message="학생 목록"):
    """학생 데이터를 보기 좋게 출력."""
    print(f"\n{message}:")
    for idx, student in enumerate(students, 1):
        print(f"{idx}. 이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

# 메인 프로그램
def main():
    students = generate_students()
    display_students(students, "초기 학생 데이터")

    while True:
        print("\n[메뉴]")
        print("1. 이름 기준 정렬")
        print("2. 나이 기준 정렬")
        print("3. 성적 기준 정렬")
        print("4. 종료")
        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ").strip()

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        key_map = {"1": "이름", "2": "나이", "3": "성적"}
        key = key_map.get(choice)
        if not key:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        print("\n정렬 방식을 선택하세요:")
        print("1. 오름차순")
        print("2. 내림차순")
        order_choice = input("정렬 방식을 선택하세요 (1, 2): ").strip()
        reverse = order_choice == "2"

        print("\n사용할 정렬 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if choice == "3":
            print("4. 기수 정렬")
        algo_choice = input("알고리즘을 선택하세요: ").strip()

        try:
            sorted_students = students[:]
            if algo_choice == "1":
                sorted_students = selection_sort(sorted_students, key, reverse)
            elif algo_choice == "2":
                sorted_students = insertion_sort(sorted_students, key, reverse)
            elif algo_choice == "3":
                sorted_students = quick_sort(sorted_students, key, reverse)
            elif algo_choice == "4":
                if choice != "3":
                    print("기수 정렬은 성적 기준에서만 사용할 수 있습니다.")
                    continue
                sorted_students = radix_sort(sorted_students, reverse)
            else:
                print("잘못된 알고리즘 선택입니다. 다시 시도하세요.")
                continue

            display_students(sorted_students, f"정렬된 학생 데이터 (기준: {key}, {'내림차순' if reverse else '오름차순'})")

        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
