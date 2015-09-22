#!/usr/bin/env python

import web
import os
import sys
import inspect

if __name__ != "__main__":              # mod_wsgi has no concept of where it is
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)

from operations import *

urls = (
    '/','Other',
    '/wallpapers(.*)','Wallpapers',
    '/(.*)','Other',
)

t_globals = {
    'get_wallpapers': get_wallpapers,
    'get_wallpaper_dirs': get_wallpaper_dirs,
}

render = web.template.render('template',base='base', globals=t_globals)

class Other:
    def GET(self, path=None):
        raise web.seeother("/wallpapers?dir=%s" % get_wallpaper_dirs()[0])

class Wallpapers:
    def GET(self, path=None):
        data = web.input()
        try:
            wallpapers_dir = "static/res/wallpapers/%s/" % data.dir
        except AttributeError:
            wallpapers_dir = "static/res/wallpapers/%s/" % get_wallpaper_dirs()[0]

        print "DEBUG (%s::%s): %s" % (self.__class__.__name__, inspect.stack()[0][3], wallpapers_dir)
        return render.wallpapers(get_wallpapers(wallpapers_dir), wallpapers_dir)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run() # devel
else:
    application = app.wsgifunc() # apache2 + wsgi
