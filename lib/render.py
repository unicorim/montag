from web.contrib.template import render_jinja
import os

src_path = "../monologue"
render = render_jinja(
    'templates',
    encoding='utf-8',
)

def html(now):
    try:
        body = open(os.path.join(src_path, "%s.txt" % now)).read()
    except IOError as err:
        print "Could not open file: %s" % err    
    return render.article(body=body, no=now)

print html("1")
