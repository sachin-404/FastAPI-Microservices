import wikipedia


def wiki(name, length):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
