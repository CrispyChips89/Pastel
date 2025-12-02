from src.modules import *

commandName = os.path.basename(__file__).replace('.py', '')

def default(args=None, flags=None):
    if not ArgsUtils.boundArgs(commandName, args, 0):
        return
    
    message = f'%BOLD%%MAGENTA%#Pastel %RESET%: %BLUE%{env.getCommitHash()}%RESET% - %BOLD%Session ID: %BLUE%{env.session.id}%RESET%'

    if '-commithash' in flags:
        message = env.getCommitHash()

    print(StringUtils.addColor(message))