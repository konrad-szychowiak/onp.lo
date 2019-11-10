import json

_conf = open('./config.json', 'r').read()
_conf = json.loads(_conf)

# export
quantifiers = _conf['quantifiers']
doubles = _conf['doubles']
singles = _conf['singles']
