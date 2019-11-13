import json
import os

_dir = os.path.dirname(__file__)
confFile = os.path.join(_dir, 'config.json')

_conf = open(confFile, 'r', encoding='utf-8').read()
_conf = json.loads(_conf)

# export
quantifiers = _conf['quantifiers']
doubles = _conf['doubles']
singles = _conf['singles']
