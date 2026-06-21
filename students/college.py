from sortedcontainers import SortedSet, SortedKeyList


class College:
    def __init__(self):
        self.__students = SortedSet()
        self.__sorted_score_students = SortedKeyList(key=lambda s: (s.score, s.id))

    def add_student(self, student):
        if student in self.__students:
            raise ValueError(f'student with id {student.id} already exists')
        self.__students.add(student)
        self.__sorted_score_students.add(student)

    def remove_student(self, student):
        if student not in self.__students:
            raise ValueError(f"student with id {student.id} does not exist")
        self.__students.remove(student)
        self.__sorted_score_students.remove(student)

    def get_students_sorted_by_id(self):
        return list(self.__students)

    def get_students_sorted_by_score(self):
        return list(self.__sorted_score_students)

    def get_students_by_scores_between(self, min_score, max_score):
        return list(
            self.__sorted_score_students.irange_key((min_score, 0), (max_score, float('inf')), inclusive=(True, True),
                                                    reverse=False))
