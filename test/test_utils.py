import os
import sys

from utils import hello_world

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def test_hello_world():
    hello_world_ans = hello_world()
    assert hello_world_ans == "hello world"
