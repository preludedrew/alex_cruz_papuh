import os
__all__ = (
        "get_wallpapers",
        "get_wallpaper_dirs",
)

# Used by Wallpapers

def get_wallpapers(location):
    if not location:
        location = 'static/res/wallpapers'
    pics = []
    try:
        pics = [ f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f)) ]
    except OSError as e:
        pass
    return pics

def get_wallpaper_dirs(location='static/res/wallpapers'):
    dirs = []
    try:
        dirs = [x for x in os.listdir(location) if os.path.isdir(os.path.join(location, x))]
    except OSError as e:
        pass
    return dirs
