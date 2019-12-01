#!/usr/bin/python3
from mkpy.utility import *

def update_usage_library ():
    """
    This copies the current mkpy library into each of the directories inside
    ./usages. It makes it easy to maíntain all usage examples up to date with
    respect to the library.
    """
    print ('Updating mkpy...')
    for fname in os.listdir('usage'):
        dst = path_cat ('usage', fname)
        if os.path.isdir (dst):
            print (dst)
            if path_exists (dst):
                ex ('rm -r ' + path_cat(dst, 'mkpy'), echo=False)
            ex ('cp -r mkpy ' + dst, echo=False)

if __name__ == "__main__":
    pymk_default()

