import shelve
import uuid
from datetime import date

class Blog:
    def __init__(self, id):
        self.id = id
        self.username = ''
        self.title = ''
        self.body = ''
        self.created = ''

blogs = shelve.open('blog')

def clear_blog():
    klist = list(blogs.keys())
    for key in klist:
        del blogs[key]

def create_blog(username, title, body):
    id = str(uuid.uuid4())
    blog = Blog(id)
    blog.title = title
    blog.username = username
    blog.body = body
    blog.created = str(date.today())
    blogs[id] = blog

def init_blogs():
    clear_blog()
    for i in range(5):
        create_blog('user'+str(i), 'title'+str(i), 'body'+str(i))

def get_blogs():
    klist = list(blogs.keys())
    x = []
    for i in klist:
        x.append(blogs[i])
    return x
