from hello_world import hello
import pytest

#hello()

def test_hello():
    assert hello() == 'hello world'
