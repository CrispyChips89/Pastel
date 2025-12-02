from src.modules import *

commandName = os.path.basename(__file__).replace('.py', '')

def default(args=None, flags=None):
    if not ArgsUtils.boundArgs(commandName, args, 1):
        return

    try:
        os.chdir(args[0])
    except