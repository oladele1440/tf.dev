import pytest
from src.exo_helper import EXOHelper
from exit_status import ExitStatus, SUCCESS, FAIL

def test_exit_success():
    """ Test to check if the sys exits properly after calling terminate(SUCCESS)
        """

    t=EXOHelper()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            t.terminate(SUCCESS)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_exit_failure():
    """ Test to check if the sys exits properly after calling terminate(SUCCESS)
        """

    t=EXOHelper()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            t.terminate(FAIL)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1