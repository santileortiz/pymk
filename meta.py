#!/usr/bin/python3
from mkpy.utility import *

usage_dir = 'usage'
file_info = {
    'mkpy/pymk.py' : None,
    'mkpy/utility.py' : None,
}

def usage_upgrade_all ():
    for fname in os.listdir(usage_dir):
        usage_path = path_cat(usage_dir, fname)
        if path_isdir(usage_path):
            install_files (file_info, prefix=usage_path)

def usage_new ():
    """
    This creates a new usage example.
    """
    if len(sys.argv) < 3:
        print ('Usage:')
        print (' ./pymk.py new_usage_example <new example name>')
        return

    # Also copy the sample pymk.py file
    file_info['pymk.py'] = None

    new_example_name = sys.argv[2]
    usage_path = path_cat(usage_dir, new_example_name)
    ex (f'mkdir {usage_path}')
    install_files (file_info, prefix=usage_path)

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

