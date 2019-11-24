def wrapper(*args, **kwargs):
    allow = 1
    if 'allow' in kwargs:
        allow = kwargs['allow']

    def __outer__(func):
        def __inner__(*tokens):

            form = func(*tokens)
            lenS = len(form.split())
            lenC = len(form.split(', '))

            if lenS not in [allow, lenC]:
                return f"({form})"

            else:
                return f"{form}"

        return __inner__
    return __outer__


@wrapper()
def predicate(token, terms):
    return f"{token}({terms})"


@wrapper(allow=2)
def quantifier(token, variable, formula):
    return f"{token} {variable} {formula}"


@wrapper()
def single(token, formula):
    return f"{token} {formula}"


@wrapper()
def double(token, left, right):
    return f"{left} {token} {right}"
