import pytest

import utils

def test_python4_not_found():
    cmd = ["python4", "timer1.py", "2"]
    utils.shell(cmd)
    assert True

def test_timer1_not_found():
    cmd = ["python3", "timer1.py", "2"]
    utils.shell(cmd)
    assert True

@pytest.mark.parametrize("timeout", [
    "1",
    "2"
])
def test_timer_not_expired(timeout):
    cmd = ["python3", "timer.py", timeout]
    utils.shell(cmd)
    assert True

def test_timer_expired():
    cmd = ["python3", "timer.py", "5"]
    utils.shell(cmd, 4)
    assert True

@pytest.mark.parametrize("timeout", [
    "1",
    "2"
])
def test_timer_not_expired2(timeout):
    cmd = ["python3", "timer.py", timeout]
    utils.shell_w_popen(cmd)
    assert True

def test_timer_expired2():
    cmd = ["python3", "timer.py", "5"]
    utils.shell_w_popen(cmd, 4)
    assert True

'''
$ pytest-3 -v test_utils.py 
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.9.2, pytest-6.0.2, py-1.10.0, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/pytest
collected 8 items                                                                                                                                                              

test_utils.py::test_python4_not_found FAILED                                                                                                                             [ 12%]
test_utils.py::test_timer1_not_found FAILED                                                                                                                              [ 25%]
test_utils.py::test_timer_not_expired[1] PASSED                                                                                                                          [ 37%]
test_utils.py::test_timer_not_expired[2] PASSED                                                                                                                          [ 50%]
test_utils.py::test_timer_expired FAILED                                                                                                                                 [ 62%]
test_utils.py::test_timer_not_expired2[1] PASSED                                                                                                                         [ 75%]
test_utils.py::test_timer_not_expired2[2] PASSED                                                                                                                         [ 87%]
test_utils.py::test_timer_expired2 FAILED                                                                                                                                [100%]

=================================================================================== FAILURES ===================================================================================
......

=========================================================================== short test summary info ============================================================================
FAILED test_utils.py::test_python4_not_found - FileNotFoundError: [Errno 2] No such file or directory: 'python4'
FAILED test_utils.py::test_timer1_not_found - subprocess.CalledProcessError: Command '['python3', 'timer1.py', '2']' returned non-zero exit status 2.
FAILED test_utils.py::test_timer_expired - subprocess.TimeoutExpired: Command '['python3', 'timer.py', '5']' timed out after 4 seconds
FAILED test_utils.py::test_timer_expired2 - subprocess.TimeoutExpired: Command '['python3', 'timer.py', '5']' timed out after 4 seconds
========================================================================= 4 failed, 4 passed in 14.49s =========================================================================
'''
