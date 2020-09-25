import pytest
from src.exo_helper import EXOHelper

def test_exo_vars_set(monkeypatch):
    """ Ensures that the helper correctly consumes 
        exo_vars."""
    ## encoded '{ "Mitch" : "eyebrows", "Dylan" : 3 }'
    encoded_vars = "eyAiTWl0Y2giIDogImV5ZWJyb3dzIiwgIkR5bGFuIiA6IDMgfQo="
    with monkeypatch.context() as mp:
        mp.setenv('EXO_VARS', 
                  encoded_vars)
        helper = EXOHelper()
        assert helper.vars.Mitch == "eyebrows"
        assert helper.vars.Dylan == 3