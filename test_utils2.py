import pytest

import utils

@pytest.mark.xfail
def test_python4_not_found():
    cmd = ["python4", "timer1.py", "2"]
    utils.shell(cmd)
    assert True

@pytest.mark.xfail
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

@pytest.mark.xfail
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

@pytest.mark.xfail
def test_timer_expired2():
    cmd = ["python3", "timer.py", "5"]
    utils.shell_w_popen(cmd, 4)
    assert True

'''
pytest-3 -v --durations=3 test_utils2.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.9.2, pytest-6.0.2, py-1.10.0, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/pytest
collected 8 items                                                                                                                                                              

test_utils2.py::test_python4_not_found XFAIL                                                                                                                             [ 12%]
test_utils2.py::test_timer1_not_found XFAIL                                                                                                                              [ 25%]
test_utils2.py::test_timer_not_expired[1] PASSED                                                                                                                         [ 37%]
test_utils2.py::test_timer_not_expired[2] PASSED                                                                                                                         [ 50%]
test_utils2.py::test_timer_expired XFAIL                                                                                                                                 [ 62%]
test_utils2.py::test_timer_not_expired2[1] PASSED                                                                                                                        [ 75%]
test_utils2.py::test_timer_not_expired2[2] PASSED                                                                                                                        [ 87%]
test_utils2.py::test_timer_expired2 XFAIL                                                                                                                                [100%]

============================================================================= slowest 3 durations ==============================================================================
4.01s call     test_utils2.py::test_timer_expired2
4.01s call     test_utils2.py::test_timer_expired
2.04s call     test_utils2.py::test_timer_not_expired[2]
======================================================================== 4 passed, 4 xfailed in 14.45s =========================================================================
'''
