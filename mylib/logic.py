import wikipedia


def wiki(name="War Goddess", length=2):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
