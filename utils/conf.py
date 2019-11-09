import json

_conf = open('config.json', 'r').read()
_conf = json.loads(_conf)

_tokens = _conf['tokens']


# export
quantifiers = _tokens['quantifiers']
doubles = _tokens['doubles']
singles = _tokens['singles']
