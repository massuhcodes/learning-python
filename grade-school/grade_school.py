class School:
    def __init__(self):
        self.class_by_grade = dict()
        self.__added_boolean = []

    def add_student(self, name, grade):
        """
        Add a student by grade and update the added_boolean list
        
        :param name: str - student name to be added
        :param grade: int - grade student belongs to
        
        If a student is in the roster (regardless if grade exists or not), append False, otherwise append True.
        Student will not be added if name already exists in roster.
        """
        if grade not in self.class_by_grade: 
            if name not in self.roster():
                # grade doesn't exist and name not in roster
                self.class_by_grade[grade] = [name]
                self.__added_boolean.append(True)
            else:
                # grade doesn't exist but name is in roster
                self.__added_boolean.append(False)
        else:
            if name not in self.roster():
                # grade does exist but name not in roster
                self.class_by_grade[grade].append(name)
                self.__added_boolean.append(True)
            else:
                # grade does exist but name is in roster
                self.__added_boolean.append(False)
            
    def roster(self):
        """
        Returns a list of student names of all grades
        
        :return: list(str)
        """
        return [
            student for grade in sorted(self.class_by_grade.keys())
            for student in sorted(self.class_by_grade[grade])
        ]

    def grade(self, grade_number):
        """
        Returns a list of student names from a specified grade
        
        :return: list(str)
        """
        return sorted(self.class_by_grade.get(grade_number, []))

    def added(self):
        """
        Returns a list of boolean as a way to notify whether a student's name
        was added or not
        
        :return: list(bool)
        """
        return self.__added_boolean
