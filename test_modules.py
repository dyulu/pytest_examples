import pytest

import utils

def is_module_loaded(module):
    cmd = ['lsmod']
    output = utils.shell(cmd)
    for line in output:
        result = line.strip().split(" ")
        if result[0] == module:
            return True

    return False

@pytest.mark.parametrize("module, module_loaded", [
    ('ext4', True),
    ('nfs', True),
    ('nvme', False)
])
def test_module_loaded(module, module_loaded):
    assert is_module_loaded(module) == module_loaded

'''
pytest-3 -v test_modules.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.9.2, pytest-6.0.2, py-1.10.0, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/pytest
collected 3 items                                                                                                                                                              

test_modules.py::test_module_loaded[ext4-True] PASSED                                                                                                                    [ 33%]
test_modules.py::test_module_loaded[nfs-True] PASSED                                                                                                                     [ 66%]
test_modules.py::test_module_loaded[nvme-False] PASSED                                                                                                                   [100%]

============================================================================== 3 passed in 0.05s ===============================================================================
'''
