#!/usr/bin/python3
from mkpy.utility import *

def default ():
    target = store_get ('last_snip', default='usage_new')
    call_user_function(target)

def usage_new ():
    """
    This creates a new usage example. Usage examples use symbolic links to the
    source inside the repository so the dvelopment cycle is fast and we don't
    have copies of the library.
    """
    if len(sys.argv) < 3:
        print ('Usage:')
        print (' ./pymk.py new_usage_example <new example name>')
        return

    ignore = ['cache', '__pycache__']
    new_example_name = sys.argv[2]
    src = '../mkpy'

    ex ('mkdir {}'.format(new_example_name))
    ex ('mkdir {}'.format(path_cat(new_example_name,'mkpy')))
    ex ('cp ../pymk.py {}'.format(new_example_name))
    for fname in os.listdir(src):
        if fname not in ignore:
            dst = path_cat('mkpy', fname)
            ex ('ln -r -s {} {}'.format(path_cat(src,fname), path_cat(new_example_name, dst)))

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

