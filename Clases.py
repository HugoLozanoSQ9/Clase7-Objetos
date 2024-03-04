from datetime import date
import convert

class User:

    def __init__(
        self, first_name, last_name, username, password,age
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.age = age

    def as_dict(self):
        return {
        'first_name' : self.first_name,
        'last_name' : self.last_name,
        'username' : self.username,
        'password' : self.password,
        'age' : self.age
        }
    
    def save(self):
        User = self.as_dict()
        json_User= convert.create('User.json',User)
        return json_User

    def raise_age(self):
        self.age+=1

    def saludar(self):
        print(f"Hola, mi nombre es: {self.first_name}")

class Post:


    def __init__(self, author, date_posted, location, modify=False, delete = False ) -> None:
        self.author = author
        self.date_posted = date_posted
        self.location = location
        self.delete = delete
        self.modify = modify

    def as_dict(self):
        return {
        'author' : self.author,
        'date_posted' : self.date_posted,
        'location' : self.location,
        'delete' : self.delete,
        'modify' : self.modify,
        }
    
    def save(self):
        Post = self.as_dict()
        json_Post= convert.create('Post.json',Post)
        return json_Post
    
class Article:

    def __init__(self, title, author,content, date_published, category,views) -> None:
        self.title = title
        self.author = author
        self.content = content
        self.date_published = date_published
        self.category = category
        self.views = views
    
    def as_dict(self):
        return {
        'title' : self.title,
        'author' : self.author,
        'content' : self.content,
        'date_published' : self.date_published,
        'category':self.category,
        'views' : self.views
        }
    
    def save(self):
        Article = self.as_dict()
        json_Article = convert.create('Article.json',Article)
        return json_Article
    

hugo_Article = Article('Titulo del artículo','Hugo','Contenido del artículo','2004/03/04','Todas las categorías',0)
hugo_Article = hugo_Article.save()

hugo = User("Hugo", "Lozano","El karakuri",123,24)
hugo = hugo.save()

hugo_post = Post('Hugo','2004/03/04','México')
hugo_post = hugo_post.save()

