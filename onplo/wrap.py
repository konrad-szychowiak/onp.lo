

def _wrap(token, allow=1):
    lenS = len(token.split())
    lenC = len(token.split(', '))

    if lenS not in [allow, lenC]:
        return f"({token})"

    else:
        return f"{token}"


def predicate(token, terms):
    return _wrap(f"{token}({terms})")


def quantifier(token, variable, formula):
    return _wrap(f"{token} {variable} {formula}")


def single(token, formula):
    return _wrap(f"{token} {formula}", allow=2)


def double(token, left, right):
    return _wrap(f"{left} {token} {right}")
