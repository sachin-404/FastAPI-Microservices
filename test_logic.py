from mylib.logic import wiki


def test_wiki(name):
    assert "god" in wiki(name)
