#!/usr/bin/python3
from mkpy.utility import *
import psutil

server_pid_pname = 'server_pid'
def server_start ():
    last_pid = store_get (server_pid_pname, default=None)
    if last_pid != None and psutil.pid_exists(last_pid):
        print (f'Server is already running, PID: {last_pid}')
    else:
        pid = ex_bg (f"python3 -m http.server 8000", cwd='Base Directory')
        print (f'Started server, PID: {pid}')
        store (server_pid_pname, pid)

def server_stop ():
    pid = store_get (server_pid_pname, default=None)
    if pid != None and psutil.pid_exists(int(pid)):
        ex (f'kill {pid}')
    else:
        print ('Server is not running.')

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

