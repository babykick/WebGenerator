from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup

myLookup = TemplateLookup(directories=['.'])


def makePage(template, outfile, **context):
    myTemplate = Template(filename=template, lookup=myLookup)
    buf = StringIO()
    ctx = Context(buf, **context)
    myTemplate.render_context(ctx)
    print buf.getvalue()
    open(outfile, 'w').write(buf.getvalue())
    

if __name__ == "__main__":
    makePage("template.tpl", "out.html",articleTitle="first page", name="Stephen", studentID="123456", articleContent=open("first_sol.txt").read())
    