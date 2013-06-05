from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['.'])

mytemplate = Template(filename="first.tpl", lookup=mylookup)
buf = StringIO()
ctx = Context(buf, name="jack")
mytemplate.render_context(ctx)
print buf.getvalue()
