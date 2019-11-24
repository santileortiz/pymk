#!/usr/bin/python3
from mkpy.utility import *

modes = {
        'debug': '-O0 -g -Wall',
        'profile_debug': '-O2 -g -pg -Wall',
        'release': '-O2 -g -DNDEBUG -Wall'
        }
mode = pers('mode', 'debug', get_cli_arg_opt('-M,--mode', modes.keys()))
C_FLAGS = modes[mode]

def default ():
    target = pers ('last_target', 'example_procedure')
    call_user_function(target)

def example_procedure ():
    ex ('echo calling example_procedure in mode: ' + mode, echo=False)

    set_echo_mode ()
    ex ('gcc {C_FLAGS} -o test test.c')

def count_next ():
    i = pers ('i', 0)
    ex ('echo Using counter value: ' + str(i), echo=False)

    pers ('i', value=i+1)

def count_start ():
    cli_counter = get_cli_arg_opt('--counter')
    val = 0
    if cli_counter != None:
        val = int(cli_counter)
    i = pers ('i', value = val)
    ex ('echo Start counter at: ' + str(i), echo=False)

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

