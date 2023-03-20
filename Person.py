class Person:
    def __init__(self, name, birthday, relationship):
        self.name = name
        self.birthday = birthday
        self.relationship = relationship
    def get_name(self):
        return self.name
    def get_birthday(self):
        return self.birthday
    def get_rel(self):
        return self.relationship
