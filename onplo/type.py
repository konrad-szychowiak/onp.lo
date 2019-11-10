from re import search as match
import onplo.conf as conf


def quantifier(token):
    return token in conf.quantifiers


def single(token):
    return token in conf.singles


def double(token):
    return token in conf.doubles


def predicate(token):
    return match("^[p-z]\/+[1-9]$", token)


def function(token):
    return match("^[f-o]\/+[1-9]$", token)


def constant(token):
    return match("^[a-e]$", token)


def variable(token):
    return match("^[A-Z]$", token)
