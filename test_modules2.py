import pytest

import utils

@pytest.fixture        # Default: scope='function'
# @pytest.fixture(scope="module")
def loaded_modules():
    print(f"Running lsmod ...")
    cmd = ['lsmod']
    output = utils.shell(cmd)
    modules = []
    for line in output:
        result = line.strip().split(" ")
        modules.append(result[0])

    return modules

@pytest.mark.parametrize("module, module_loaded", [
    ('ext4', True),
    ('nfs', True),
    ('nvme', False)
])
def test_module_loaded(module, module_loaded, loaded_modules):
    loaded = module in loaded_modules
    assert loaded == module_loaded

'''
# With default (scope='function')
$ pytest-3 -vs test_modules2.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.9.2, pytest-6.0.2, py-1.10.0, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/pytest
collected 3 items                                                                                                                                                              

test_modules2.py::test_module_loaded[ext4-True] Running lsmod ...
PASSED
test_modules2.py::test_module_loaded[nfs-True] Running lsmod ...
PASSED
test_modules2.py::test_module_loaded[nvme-False] Running lsmod ...
PASSED

============================================================================== 3 passed in 0.07s ===============================================================================

# With (scope="module")
$ pytest-3 -vs test_modules2.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.9.2, pytest-6.0.2, py-1.10.0, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/pytest
collected 3 items                                                                                                                                                              

test_modules2.py::test_module_loaded[ext4-True] Running lsmod ...
PASSED
test_modules2.py::test_module_loaded[nfs-True] PASSED
test_modules2.py::test_module_loaded[nvme-False] PASSED

============================================================================== 3 passed in 0.04s ===============================================================================
'''
