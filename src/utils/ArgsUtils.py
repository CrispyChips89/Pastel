from src.utils.ErrorUtils import ErrorUtils

class ArgsUtils:
    @staticmethod
    def boundArgs(commandName: str, args: list, minArgs: int, maxArgs: int = None) -> bool:
        if len(args) < minArgs:
            ErrorUtils.ePrint(commandName, 0x010001)
            return False

        if maxArgs is not None and len(args) > maxArgs:
            ErrorUtils.ePrint(commandName, 0x010003)
            return False
        
        return True

    @staticmethod
    def getArgument(args: list, index: int, default=None):
        return args[index] if index < len(args) else default
