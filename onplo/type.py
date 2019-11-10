import re
import onpl.conf as conf


def quantifier(token):
    return token in conf.quantifiers


def single(token):
    return token in conf.singles


def double(token):
    return token in conf.doubles


def predicate(token):
    return re.search("^[p-z]\/+[1-9]$", token)


def function(token):
    return re.search("^[f-o]\/+[1-9]$", token)


def constant(token):
    return re.search("^[a-e]$", token)


def variable(token):
    return re.search("^[A-Z]$", token)
