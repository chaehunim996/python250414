# Person, Manager, Employee 클래스 정의 및 테스트 코드

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test_classes():
    print("1. Person 인스턴스 생성")
    p1 = Person(1, "Alice")
    p1.printInfo()
    print()

    print("2. Manager 인스턴스 생성")
    m1 = Manager(2, "Bob", "Project Manager")
    m1.printInfo()
    print()

    print("3. Employee 인스턴스 생성")
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()
    print()

    print("4. Person 리스트에 저장 후 출력")
    people = [p1, m1, e1]
    for person in people:
        person.printInfo()
        print()

    print("5. Manager 여러 개 생성 테스트")
    m2 = Manager(4, "Diana", "HR Manager")
    m2.printInfo()
    print()

    print("6. Employee 여러 개 생성 테스트")
    e2 = Employee(5, "Eve", "JavaScript")
    e2.printInfo()
    print()

    print("7. Manager에서 title 변경 테스트")
    m1.title = "Senior PM"
    m1.printInfo()
    print()

    print("8. Employee에서 skill 변경 테스트")
    e1.skill = "Django"
    e1.printInfo()
    print()

    print("9. 타입 체크 테스트")
    print(f"m1은 Person인가요? {'Yes' if isinstance(m1, Person) else 'No'}")
    print(f"e1은 Manager인가요? {'Yes' if isinstance(e1, Manager) else 'No'}")
    print()

    print("10. 각 인스턴스 타입 확인")
    for person in people:
        print(f"{person.name} is a {type(person).__name__}")

# 테스트 실행
if __name__ == "__main__":
    test_classes()
