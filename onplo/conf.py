"""
Configuration-loading module with setup for the type-checkers.

Loads data from `config.json`, where control lists are defined.
"""

import os
import json

_dir = os.path.dirname(__file__)
confFile = os.path.join(_dir, 'config.json')

_conf = open(confFile, 'r', encoding='utf-8').read()
_conf = json.loads(_conf)

# export
match_list = _conf["match"]
match_re = _conf["rematch"]
