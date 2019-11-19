#!/usr/bin/python3
from mkpy.utility import *

def default():
    target = pers ('last_target', 'example_procedure')
    call_user_function(target)

def example_procedure ():
    ex ('echo calling example_procedure().', echo=False)

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

