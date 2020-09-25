import os
import yaml
import pytest
from development_setup import DevelopmentSetup, \
DEVELOPMENT_ENVARS_PATH
from src.exo_helper import EXOHelper

@pytest.fixture(autouse=True,
                scope="session")
def manage_leakage():
    """ These are naturally leaky tests
        because they simulate manual testing. 
        Clean accordingly."""
    beginning_exo_vars = os.getenv("EXO_VARS", None)
    try:
        with open(DEVELOPMENT_ENVARS_PATH, 'r') as test_exo_vars_file:
            envars_content = test_exo_vars_file.read()
    except FileNotFoundError:
        envars_content = None 

    yield
    if beginning_exo_vars:
        os.environ("EXO_VARS",
                    beginning_exo_vars)
    if envars_content:
        with open(DEVELOPMENT_ENVARS_PATH, 'w') as test_exo_vars_file:
            test_exo_vars_file.write(envars_content)


def test_sets_dev_envars_directly(manage_leakage):
    """ Should look for, and set, EXO_VARS value
        from a development_envars.yml file."""
    test_vars = dict(sandwich="ham",
                     pickles=1)
    DevelopmentSetup.set_test_exo_vars(test_vars)
    helper = EXOHelper()
    assert helper.vars.sandwich == "ham"
    assert helper.vars.pickles == 1

def test_sets_dev_envars_file(manage_leakage):
    """ Should look for, and set, EXO_VARS value
        from a development_envars.yml file."""
    test_vars = dict(liu_ji="swordholder",
                     commodore=64)
    with open(DEVELOPMENT_ENVARS_PATH, 'w') as test_exo_vars_file:
        yaml.dump(test_vars,
                  test_exo_vars_file)

    DevelopmentSetup.set_test_exo_vars()
    helper = EXOHelper()
    assert helper.vars.liu_ji == "swordholder"
    assert helper.vars.commodore == 64

def test_allows_no_file(manage_leakage):
    """ If no development_envars.yml file exists, 
        thats OK. Ignore it."""
    os.remove(DEVELOPMENT_ENVARS_PATH)
    DevelopmentSetup.set_test_exo_vars()

