from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
import os

myLookup = TemplateLookup(directories=['.'])
OUTDIR = './pages/html/'

def makePage(template, outfile, **context):
    myTemplate = Template(filename=template, lookup=myLookup)
    buf = StringIO()
    ctx = Context(buf, **context)
    myTemplate.render_context(ctx)
    print buf.getvalue()
    outfile = os.path.join(OUTDIR, outfile)
    open(outfile, 'w').write(buf.getvalue())
    
    

if __name__ == "__main__":
    ctx = {
            'baner_text': 'See world',
            'baner_text_sub': 'Internet view',
            'articleTitle': "Private v. Public in Social Networking",
            'name': "Jing Tao",
            'studentID': "123456",
            'articleContent': open("content.essay.txt").read(),
            'courseInfo' : "Course info"
    }
    
    env = {
        'imgdir': '../images'
    }
    
    ctx.update(env)
    makePage("index.tpl", "index.html", **ctx)
    