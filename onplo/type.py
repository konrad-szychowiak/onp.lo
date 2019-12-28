import re
from onplo.conf import match_list, match_re


def match(type, token):
    """
    Matches token (str) to a given type (str)
    using *list* provided by config file.

    Returns bool:
    True    when match is successful
    False   otherwise
    """
    return token in match_list[type]


def rematch(type, token):
    """
    Matches token (str) to a given type (str)
    using *regexes* provided by config file.

    Returns bool:
    True    when match is successful
    False   otherwise
    """
    return re.search(match_re[type], token)
