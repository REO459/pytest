import pytest
from school import Classroom, Person, Teacher, Student, TooManyStudents


@pytest.fixture
def harry():
    return Teacher(name="Harry Potter")


@pytest.fixture
def hermione():
    return Student(name="Hermione Granger")


@pytest.fixture
def classroom_with_students(harry, hermione):
    students = [Student(name=f"Student_{i}") for i in range(10)]
    return Classroom(
        teacher=harry, students=students, course_title="Defense Against the Dark Arts"
    )


def test_add_student(classroom_with_students, hermione):
    with pytest.raises(TooManyStudents):
        classroom_with_students.add_student(hermione)


def test_remove_student(classroom_with_students, hermione):
    classroom_with_students.remove_student("Hermione Granger")
    assert hermione not in classroom_with_students.students


def test_change_teacher(classroom_with_students, harry):
    new_teacher = Teacher(name="Albus Dumbledore")
    classroom_with_students.change_teacher(new_teacher)
    assert classroom_with_students.teacher == new_teacher


def test_person_name():
    person = Person(name="Severus Snape")
    assert person.name == "Severus Snape"


def test_teacher_inherits_person_name():
    teacher = Teacher(name="Minerva McGonagall")
    assert teacher.name == "Minerva McGonagall"


def test_student_inherits_person_name():
    student = Student(name="Ron Weasley")
    assert student.name == "Ron Weasley"
