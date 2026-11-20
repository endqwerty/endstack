from pager import page


def test_size():
    assert len(page(list(range(25)), 1)) == 10


if __name__ == "__main__":
    test_size()
    print("ok")
