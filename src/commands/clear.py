from src.modules import *

commandName = os.path.basename(__file__).replace('.py', '')

def default(args=None, flags=None):
    if not ArgsUtils.boundArgs(commandName, args, 0):
        return
    
    print('\033[3J\033[H\033[2J')