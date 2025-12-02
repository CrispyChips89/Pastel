from src.core.Errors import *
from src.utils.StringUtils import StringUtils

class ErrorUtils:
    @staticmethod
    def ePrint(commandName: str, targetCode: int, exc: Exception | None = None):
        error = ErrorCollection.get(targetCode)

        description = error.description.replace("&cmd_name&", commandName).replace("&unkwn_err&", str(targetCode))
        message = StringUtils.addColor(f"%BOLD%%BG_BRIGHT_RED% @pastel ERR! %RESET%%BOLD%%BG_BRIGHT_BLACK% {error.stringCode} %RESET% (%BLUE%{hex(error.code)}%RESET%%BOLD%)%RESET%: %BRIGHT_RED%{description}%RESET%")

        if exc:
            message += f" Exception: {exc}"

        print(message.strip())
