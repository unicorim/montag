from web.contrib.template import render_jinja
import os, sys

script, filename = sys.argv
src_path = "../monologue"
render = render_jinja(
    'templates',
    encoding='utf-8',
)

def html(now):
    try:
        body = open(os.path.join(src_path, "%s.txt" % now)).read()
    except IOError:
        print "Could not open file :("
    static_ver = open(os.path.join(src_path, "%s.html" % now), 'w')
    return static_ver.write(render.article(body=body, no=now))

html(filename)
