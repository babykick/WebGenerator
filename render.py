from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
import os
import copy


myLookup = TemplateLookup(directories=['.'])
OUTDIR = './pages/html/'
MATDIR = './materials/'
MAIN_JS = 'main.js'

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

    def addImage(self, imgName, width):
        self.images.append({'name':imgName, 'width':width})


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


