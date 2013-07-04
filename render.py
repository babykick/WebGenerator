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
    articleContent = open("content.essay.txt").read()
    post = Post(title="Computers and Children", content=articleContent)    
    student = Student(name="Jing Tao", id="123456", email="taojing0814@126.com", course="SC/NATS1700B-computer,information and society")
    ctx = {
            'student': student,
            'post': post,
            'baner_text': 'Computer Life',
            'baner_text_sub': 'A view about computer',
    }
    
    env = {
        'imgdir': '../images'
    }
    
    ctx.update(env)
    makePage("index.tpl", "index.html", **ctx)
    