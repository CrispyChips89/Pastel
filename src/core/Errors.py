from src.modules import dataclass

@dataclass
class Error:
    code: int
    stringCode: str
    description: str

class ErrorCollection:
    map: dict[int, tuple[str, str]] = {
        0x000000: ("UNKNOWN_CODE", "Unknown error code (&unkwn_err&)."),
        0x010000: ("COMMAND_NOT_FOUND", "'&cmd_name&' is not recognized as a command."),
        0x010001: ("MISSING_ARGUMENTS", "Missing arguments for '&cmd_name&'."),
        0x010002: ("MALFORMED_VARIABLE_DECLARATION", "Variable '&cmd_name&' is malformed."),
        0x010003: ("EXCEEDED_MAX_ARGUMENTS", "Exceeded max arguments for '&cmd_name&'."),
        0x020000: ("CONNECTION_TIMEOUT", "The connection has timed out."),
        0x030000: ("FILE_NOT_FOUND", "The file was not found."),
        0x030001: ("NOT_A_DIRECTORY", "This is not a directory."),
        0x030002: ("PERMISSION_DENIED", "Permisssion denied..."),
        0x040000: ("COMMAND_DEFAULT_FUNCTION_MISSING", "Function 'default()' in '&cmd_name&' is missing."),
        0x040001: ("INTERNAL_COMMAND_EXCEPTION", "'&cmd_name&' failed to execute.")
    }

    @staticmethod
    def get(target_code: int) -> Error:
        stringCode, description = ErrorCollection.map.get(target_code, ErrorCollection.map[0x000000])
        
        return Error(target_code, stringCode, description)