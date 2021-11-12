from activity.utils import hello_world


def test_hello_world():
    hello_world_ans = hello_world()
    assert hello_world_ans == "hello world"
