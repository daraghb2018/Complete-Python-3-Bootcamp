import string


def cap_text(text):
    """Capitalize each word in the given text.

    This function behaves similarly to :meth:`str.title` but keeps
    apostrophes intact. Using :func:`string.capwords` avoids capitalising
    characters that follow an apostrophe which is required for the unit
    tests in this repository.
    """

    return string.capwords(text)
