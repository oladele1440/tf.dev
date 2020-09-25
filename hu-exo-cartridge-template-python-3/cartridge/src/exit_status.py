from typing import Any # noqa pylint: disable=unused-import


class ExitStatus:
    """ defines the available exit status for EXOHleper container

        Args:
            name : the human-readable text name of the environment.
                Will be coerced to uppercase.
            returnCode : the exit code which will be returned on the sys.exit call
    """

    def __init__(self, name: str, return_code: int):
        self.name = name
        self.return_code = return_code

    @property
    def name(self)->str:
        return self._name

    @name.setter
    def name(self, value: str)->None:
        self._name = value.upper().strip()
    
    @property
    def return_code(self)->int:
        return self._return_code
    
    @return_code.setter
    def return_code(self, value: int)->None:
        self._return_code = value

    def __str__(self)-> str:
        return self.name


SUCCESS = ExitStatus('SUCCESS',0)
FAIL = ExitStatus('FAIL',1)
