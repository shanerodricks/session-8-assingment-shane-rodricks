import pytest
from datetime import datetime
import time
import inspect
import os
from io import StringIO
import sys

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_odd_it_even():
    from session8 import odd_it  # Import the relevant functions

    @odd_it
    def adder(a: int, b: int) -> int:
        return a + b

    if datetime.now().second % 2 != 0:
        assert adder(1, 2) is not None
    else:
        assert adder(1, 2) is None

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout

def test_logger():
    from session8 import logger

    @logger 
    def function_name(var1: str, var2: int) -> str:
        return 'output'

    with Capturing() as output:
        function_name('red', 1)

    assert any(["function_name" and "called at" in o for o in output])
    assert any(["Execution time" in o for o in output])
    assert any(["Function description" in o for o in output])
    assert "This is a function's writeup" in function_name.__doc__
    assert any(["Function annotation" in o for o in output])
    assert "function_name" == function_name.__name__

def test_access_rights_function():
    from session8 import decorator_factory

    def func(*args):
        return args

    assert len(decorator_factory('high')(func)(1, 2, 3, 4)) == 4
    assert len(decorator_factory('mid')(func)(1, 2, 3, 4)) == 3
    assert len(decorator_factory('low')(func)(1, 2, 3, 4)) == 2
    assert len(decorator_factory('no')(func)(1, 2, 3, 4)) == 1

def test_authenticate_function():
    from session8 import authenticate

    @authenticate("secret")
    def my_func():
        return "Amazing!"

    with pytest.raises(TypeError) as execinfo:
        my_func()

    assert my_func("random") == "Wrong Password"
    assert my_func("secret") == "Amazing!"

def test_timed_function():
    from session8 import timed

    @timed(10)
    def func(*args):
        time.sleep(0.2)
        pass

    with Capturing() as output:
        func()

    assert any(["Avg" or "Average" in o for o in output])
    assert any(["0.2" or "0.3" in o for o in output])
    assert any(["10" in o for o in output])
