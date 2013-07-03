from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
import os

myLookup = TemplateLookup(directories=['.'])
OUTDIR = './pages/html/'


class Post(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content
        

class Student(object):
    def __init__(self, name, id, course):
        self.name=name
        self.id = id
        self.course = course
     

def makePage(template, outfile, **context):
    myTemplate = Template(filename=template, lookup=myLookup)
    buf = StringIO()
    ctx = Context(buf, **context)
    myTemplate.render_context(ctx)
    print buf.getvalue()
    outfile = os.path.join(OUTDIR, outfile)
    open(outfile, 'w').write(buf.getvalue())
    
    

if __name__ == "__main__":
    articleContent = open("content.essay.txt").read()
    post = Post(title="Private v. Public in Social Networking", content=articleContent)    
    student = Student(name="Jing Tao", id="123456", course="Course info")
    ctx = {
            'student': student,
            'post': post,
            'baner_text': 'Internet Today',
            'baner_text_sub': 'A view about internet',
    }
    
    env = {
        'imgdir': '../images'
    }
    
    ctx.update(env)
    makePage("index.tpl", "index.html", **ctx)
    