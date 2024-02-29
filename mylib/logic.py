import wikipedia
from textblob import TextBlob
from collections import defaultdict


def wiki(name, length=5):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""

    return wikipedia.search(name)


def phrase(name):
    """Returns phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases


def parts_of_speech_tags(name):
    """Returns parts of speech of the response"""

    blob = TextBlob(wiki(name))
    tags_dict = defaultdict(list)
    for i, j in blob.tags:
        tags_dict[j].append(i)
    return tags_dict
