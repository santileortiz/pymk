#!/usr/bin/python3
from mkpy.utility import *

# This example shows how to simplify calling gcc with several CLI options that
# make it more convenient for developers.

# This is how we can set different compiler flags that will be selected by
# using a command line option (in this case --mode or -M). The last mode used
# will be persisted acrosss runs of the script so --mode can be ommited in
# later calls. Tab complete will work to complete --mode after -- is typed, and
# to complete the possible values for its argument.
modes = {
        'debug': '-O0 -g -Wall',
        'profile_debug': '-O2 -g -pg -Wall',
        'release': '-O2 -g -DNDEBUG -Wall'
        }
mode = store('mode', get_cli_arg_opt('-M,--mode', modes.keys()), 'debug')
C_FLAGS = modes[mode]

# This function will be called if no argument is passed to pymk.py
def default ():
    target = store_get ('last_snip', default='simple_build')
    call_user_function(target)

def simple_build ():
    ex (f'echo calling example_procedure in mode: {mode}', echo=False)

    # After setting echo mode, all calls to ex() will only echo the command
    # that would have been called. This is useful to debug the commands that
    # are being called here, before we accidentally run commands cause
    # unintended results. Here we use it because there is no actual test.c
    # file, in a normal use case the following line would be removed.
    set_echo_mode ()

    # Call the compiler by using the ex() function. Note how an f-string is
    # used to substitute the flags variable.
    ex (f'gcc {C_FLAGS} -o test test.c')

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

