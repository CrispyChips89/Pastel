from src.modules import *

commandName = os.path.basename(__file__).replace('.py', '')

def default(args=None, flags=None):
    sys.exit(0)