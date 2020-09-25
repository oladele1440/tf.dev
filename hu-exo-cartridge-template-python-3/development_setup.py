import base64
import os
import json
import yaml
from typing import Optional  # noqa pylint:disable=syntax-error

DEVELOPMENT_ENVARS_PATH = "/app/development_envars.yml"

class DevelopmentSetup:
    """ Allows for simple local manual testing 
        via a ``development_envars.yml`` file. 
        This enables local developers to either import
        the class and use it in test cases, or manually set
        local test envars when chicken-peck testing. """

    @staticmethod
    def set_test_exo_vars(vars: Optional[dict]= dict())->None:  # noqa: pylint:disable=dangerous-default-value
        """ Sets the EXO_VARS envar representing the test 
            values provided. If no vars are provided, looks
            for a file at ./development_envars.yml.

            Args:
                vars: the dictionary to convert to EXO_VARS encoded json
                per the `spec <https://exodocs.healthunion.io/specifications/general_exo_specification_0_0_1/exo_vars_specification.html>`_.
                If not provided will look for a ./development_envars.yml file
                and parse that for envars.
        """
        exo_vars_string = os.getenv('EXO_VARS',
                                    "")
        if vars.keys():
            exo_vars_string = str(base64.b64encode(
                                    json.dumps(
                                        vars).encode('ascii')
                                  ),'ascii')
        elif os.path.exists(DEVELOPMENT_ENVARS_PATH):
            with open(DEVELOPMENT_ENVARS_PATH) as config_file:
                exo_vars_string = str(base64.b64encode(
                                        json.dumps(yaml.load(config_file)
                                      ).encode('ascii')
                                    ),'ascii')
            
        os.environ['EXO_VARS'] = exo_vars_string


if __name__ == "__main__":
    DevelopmentSetup.set_test_exo_vars()    