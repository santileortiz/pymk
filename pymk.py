#!/usr/bin/python3
from mkpy.utility import *

modes = {
        'debug': '-O0 -g -Wall',
        'profile_debug': '-O2 -g -pg -Wall',
        'release': '-O2 -g -DNDEBUG -Wall'
        }
mode = store('mode', get_cli_arg_opt('-M,--mode', modes.keys()), 'debug')
C_FLAGS = modes[mode]

def default ():
    target = store_get ('last_target', default='example_procedure')
    call_user_function(target)

def example_procedure ():
    ex ('echo calling example_procedure in mode: {mode}', echo=False)

    set_echo_mode ()
    ex ('gcc {C_FLAGS} -o test test.c')

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

