import rlcompleter
import readline
import atexit
import os
    # http://stackoverflow.com/questions/7116038/python-tab-completion-mac-osx-10-7-lion
if'libedit'in readline.__doc__:
    readline.parse_and_bind('bind ^I rl_complete')
else:
    readline.parse_and_bind('tab: complete')
    histfile = os.path.join(os.environ['HOME'],'.pyhist')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
    atexit.register(readline.write_history_file, histfile)
    del readline, rlcompleter, histfile, os
