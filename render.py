from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
import os

print os.path.dirname(__file__)
mylookup = TemplateLookup(directories=['.'])


buf = open("../first.html", "w")
ctx = Context(buf, name="xxxxxxx")
mytemplate = Template(filename='first.tpl', lookup=mylookup)
mytemplate.render_context(ctx)
 

