from exo import EXO
from exit_status import ExitStatus
from types import SimpleNamespace as Namespace
import json
import os
import sys
import base64

class EXOHelper(EXO):
    """Wrapper class for EXO. with basic functionality 
        logging - initialized as the object is created
        secrets
        variable access - Store json obj in 'EXO_VARS' as attributes
        exit code - calls sys.exits with 0 for Success and 1 for Failure
        """

    def __init__(self):
        super().__init__()
        super().init_logger()
        self.get_exo_vars()
        

    def get_exo_vars(self)-> None:
        """ Captures the exo_vars from env
            and sets them on the current object.

            Returns:
                None: 
        """
        try:
            encoded_string = os.environ["EXO_VARS"]
            decoded_string = base64.b64decode(encoded_string)
            self.vars=json.loads(decoded_string,
                        object_hook= lambda d: Namespace(**d))
        except KeyError:
            self.log.error('EXO_VARS not properly set in the environment variable')
            # raise EnvironmentError('EXO_VARS not currently set in the enviroment variables')
                
    def terminate (self, status: ExitStatus)-> None:
        """Terminates the object by making a sys.exit call.

            Args:
                status: An ExitStatus object that provides 
                the exit status for sys.exit call. 
                0 for all good, 1 for issue

        """
        sys.exit(status.return_code)
        