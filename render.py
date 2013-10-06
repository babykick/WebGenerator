from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
import os
import copy


myLookup = TemplateLookup(directories=['.'])
OUTDIR = './pages/html/'
MATDIR = './materials/'


class Page(object):
    def __init__(self, tpl, title, subtitle, student=None, **kwargs):
        self.tpl = tpl
        self.posts = []
        self.title = title
        self.subtitle = subtitle
        self.designer = student
        self.nav = None
        self.cssFiles = []
        self.jsFiles = []

    def addNav(self, nav):
        if self.nav is None:
           self.nav = nav

    def addPost(self, post):
        self.posts.append(post)

    def addCSS(self, cssFile):
        self.cssFiles.append(cssFile)

    def addJS(self, jsFile):
        self.jsFiles.append(jsFile)

    def _makePage(self, template, outfile, **context):
        myTemplate = Template(filename=template, lookup=myLookup)
        buf = StringIO()
        ctx = Context(buf, **context)
        myTemplate.render_context(ctx)
        print buf.getvalue()
        outfile = os.path.join(OUTDIR, outfile)
        open(outfile, 'w').write(buf.getvalue())

    def render(self, pageName):
        ctx = {
               'page': self,
               'imgdir': '../images',
              }

        self._makePage(self.tpl, pageName, **ctx)

    def duplicated(self):
        return copy.deepcopy(self)


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

# Utils
def readContent(subdir, contentFile):
    return open(os.path.join(MATDIR, subdir, contentFile)).read()



if __name__ == "__main__":
    nav = NavBar()
    nav.addLink(Home="index.html")
    nav.addLink(Introduction="intro.html")
    nav.addLink(Audience="aud.html")
    nav.addLink(Design="design.html")
    nav.addLink(Resources="resources.html")

    student = Student(name="Lu Zhe Xuan", id="174047", email="xxxx@xx.com", course="KXX133 web management")

    # Base page
    basePage = Page(tpl="base.mako", title='Wild world', subtitle='Mammals of Tasmania', student=student)
    basePage.addCSS('main.css')
    basePage.addJS('validate.js')
    basePage.addNav(nav)

    # Home page
    page = basePage.duplicated()
    post = Post(title="Animals", content="animal introduction")
    post.addImage("animal_x.jpg")
    page.addPost(post)
    for i in range(4):
        p = Post(title="", content="animal introduction")
        p.addImage("animal_x.jpg")
        page.addPost(p)
    post = Post(title="", content=readContent("kxx-ass2", "animals.txt"))
    page.addPost(post)
    page.render("index.html")

    # Intro page
    page2 = basePage.duplicated()  #Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    introPost = Post(title="Introduce", content=readContent("kxx-ass2", "intro.txt"))
    page2.addPost(introPost)
    page2.render("intro.html")

   # audience
    page3 = basePage.duplicated() #Page(title='Wild world', subtitle='Mammals of Tasmania', student=student)
    audPost = Post(title="Audience", content=readContent("kxx-ass2", "aud.txt"))
    page3.addPost(audPost)
    page3.render("aud.html")

    # design page
    page4 =  basePage.duplicated()
    designPost = Post(title="Design", content=readContent("kxx-ass2", "design.txt"))
    page4.addPost(designPost)
    page4.render( "design.html")

    # resource page
    page5 = basePage.duplicated()
    p = Post(title="Resources", content=readContent("kxx-ass2", "resource.txt"))
    page5.addPost(p)
    page5.render("resources.html")

