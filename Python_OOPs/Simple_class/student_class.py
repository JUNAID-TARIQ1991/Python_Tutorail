class Student:
    def __init__(self, name, id, subject):
        self.set_attr(name, id, subject)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_subj(self):
        return self.__subject

    def set_attr(self, name, id, subject):
        if id > 0:
            self.__name = name
            self.__id = id
            self.__subject = subject
        else:
            raise ValueError("ID is invalid")


student1 = Student("junaid", '01', "physics")
print(student1.get_id())
