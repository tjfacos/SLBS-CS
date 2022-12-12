import random

class Person():

    def __init__(self, first_name, surname, dob) -> None:
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = dob
    
    def create_username(self):
        return self.first_name[0]+self.surname+self.date_of_birth[len(self.date_of_birth)-4:]

    def create_password(self):
        password = ""
        characters = self.first_name+self.surname+self.date_of_birth
        
        for _ in range(len(characters)):
            password += random.choice(characters)

        return password
    
print(Person("Tom", "Facos", "27/10/2005").create_username())
print(Person("Tom", "Facos", "27/10/2005").create_password())

person2 = Person("Qhomas", "Zamos", "27/10/7896")
print(person2.create_username())
print(person2.create_password())
