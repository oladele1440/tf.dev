import pytest
import time
from src.exo_helper import EXOHelper

def test_complete_logs_automagically():
    """ logs should just work without 
        any extra effort from the user."""

    message = 'This is the test!'
    helper = EXOHelper()
    helper.log.info(message)
    time.sleep(1)
    returned_logs = helper.get_logs(10)

    correct_log_count = 0
    for log in returned_logs:
        if message in log.message:
            correct_log_count += 1
    
    assert correct_log_count >= 1
