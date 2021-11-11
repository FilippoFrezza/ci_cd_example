import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *

def test_hello_world():
    hello_world_ans = hello_world()
    assert  hello_world_ans == 'hello world'