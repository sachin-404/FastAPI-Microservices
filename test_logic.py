from mylib.logic import wiki


def test_wiki():
    assert "Wikimedia" in wiki(name="wikipedia")
