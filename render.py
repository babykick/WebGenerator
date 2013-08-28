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
        self.cssFiles = []

    def addNav(self, nav):
        if self.nav is None:
           self.nav = nav


    def addPost(self, post):
        self.posts.append(post)

    def addCSS(self, cssFile):
        self.cssFiles.append(cssFile)

    def render(self, template, pageName):
        ctx = {
               'student': self.student,
               'posts': self.posts,
               'links': self.nav.links,
               'baner_text': self.title,
               'baner_text_sub': self.subtitle,
               'imgdir': '../images',
               'cssFiles': self.cssFiles
              }

        makePage(template, pageName, **ctx)



class Post(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.images = []

    def addImage(self, imgName):
        self.images.append(imgName)

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
    nav = NavBar()
    nav.addLink(Home="index.html")
    nav.addLink(Introduction="intro.html")
    nav.addLink(Audience="aud.html")
    nav.addLink(Design="design.html")
    nav.addLink(Resources="resources.html")

    student = Student(name="Name", id="Student ID", email="xxxx@xx.com", course="SC/NATS1700B-computer,information and society")

    # Home page
    page = Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    page.addCSS("main_alter.css")
    page.addNav(nav)

    post = Post(title="Animals", content="animal introduction")
    post.addImage("animal_x.jpg")

    page.addPost(post)
    for i in range(4):
        p = Post(title="", content="animal introduction")
        p.addImage("animal_x.jpg")
        page.addPost(p)
    post = Post(title="", content=open("animals.txt").read())
    page.addPost(post)
    page.render("index.tpl", "index.html")

    # Intro page
    page2 = Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    page2.addNav(nav)
    introPost = Post(title="Introduce", content=open("intro.txt").read())
    page2.addPost(introPost)
    page2.render("index.tpl", "intro.html")

   # audience
    page3 = Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    page3.addNav(nav)
    audPost = Post(title="Audience", content=open("aud.txt").read())
    page3.addPost(audPost)
    page3.render("index.tpl", "aud.html")

    # design page
    page4 = Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    page4.addNav(nav)
    designPost = Post(title="Design", content=open("design.txt").read())
    page4.addPost(designPost)
    page4.render("index.tpl", "design.html")

    # resource page
    page5 = Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    page5.addNav(nav)
    p = Post(title="Resources", content=open("resource.txt").read())
    page5.addPost(p)
    page5.render("index.tpl", "resources.html")

