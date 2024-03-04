#Ver desde 2:40
#User, Posts y articles (todo a Json)
#recuperar toda la info 

""" 
HW.

Definir 3 clases: User, Post, Article

Definir en cada clase un método (save) que permita guardar los 
datos de la instancia en el archivo respectivo (users.json, posts.json, articles.json)
users.json -> Contiene una lista de usuarios
posts.json -> Contiene una lista de posts
article.json -> contiene una lista de artículos

Resultado esperado:
user = User('Alfredo','Altamirano')

user.save() -> Guarde los datos del usuario en users.json

Propiedades quedan a criterio de c/u

Como referencia por lo que ya vimos en clase jeje (lo que está en el README.md)

"""

from datetime import date


class User:

    race = "Human"

    # dunder: double underscore (doble guion bajo)

    def __init__(
        self, first_name, last_name, username, password,age,birth_date = date(1999,7,26)
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.username = username
        self.password = password
        self.age = age

    def as_dict(self):
        return {
        'first_name' : self.first_name,
        'last_name' : self.last_name,
        'birth_date' : self.birth_date,
        'username' : self.username,
        'password' : self.password,
        }

    def raise_age(self):
        self.age+=1


    def saludar(self):
        print(f"Hola, mi nombre es: {self.first_name}")


hugo = User("Hugo", "Lozano","El karakuri",123,'ojo@void.com')
francisco = User("Francisco", "Rivera",'koko',237897489127,'hola@void.com',date(1998,6,12))

print(hugo.as_dict())
print(francisco.as_dict())

# print(hugo.first_name, hugo.race)
# print(francisco.first_name, francisco.race)
# hugo.saludar()

