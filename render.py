from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
import os

myLookup = TemplateLookup(directories=['.'])
OUTDIR = './pages/html/'


class Page(object):
    def __init__(self, title, subtitle, student=None, **kwargs):
        self.posts = []
        self.title = title
        self.subtitle = subtitle
        self.student = student
        self.nav = None

    def addNav(self, nav):
        if self.nav is None:
           self.nav = nav

    def addPost(self, post):
        self.posts.append(post)

    def render(self, template, pageName):
        ctx = {
               'student': self.student,
               'posts': self.posts,
               'links': self.nav.links,
               'baner_text': self.title,
               'baner_text_sub': self.subtitle,
               'imgdir': '../images'
              }

        makePage(template, pageName, **ctx)



class Post(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
class NavBar(object):
    def __init__(self):
        self.links = []

    def addLink(self, **links):
        """
           link: A tuple include name and link url
        """
        for link in links.items():
            self.links.append(link)


class Student(object):
    def __init__(self, name, id, email, course):
        self.name=name
        self.id = id
        self.course = course
        self.email = email
     

def makePage(template, outfile, **context):
    myTemplate = Template(filename=template, lookup=myLookup)
    buf = StringIO()
    ctx = Context(buf, **context)
    myTemplate.render_context(ctx)
    print buf.getvalue()
    outfile = os.path.join(OUTDIR, outfile)
    open(outfile, 'w').write(buf.getvalue())
    
    

if __name__ == "__main__":
    student = Student(name="Name", id="Student ID", email="xxxx@xx.com", course="SC/NATS1700B-computer,information and society")
    page = Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    nav = NavBar()
    nav.addLink(Home="index.html", Other="other.html")
    articleContent = open("animals.txt").read()
    post = Post(title="Animals", content=articleContent)
    page.addNav(nav)
    page.addPost(post)
    page.render("index.tpl", "index.html")
