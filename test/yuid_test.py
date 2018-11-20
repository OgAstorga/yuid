from yuid import yuid

def test_length():
    uuid = yuid()

    assert len(uuid) <= 11
