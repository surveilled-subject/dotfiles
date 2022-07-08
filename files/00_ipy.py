#!/usr/bin/env python3

    # snips to load on ipython3 start

import yaml
import json
import re
import os

from pprint import pprint as pp

def loadit(infi):
    if re.search(r'\.ya?ml', infi):
        with open(infi) as f:
            outfi = yaml.safe_load(f)
    if re.search(r'\.json', infi):
        with open(infi) as f:
            outfi = json.load(f)
    if re.search(r'\.txt', infi):
        with open(infi) as f:
            outfi = f.read().splitlines()
    return(outfi)

def dumpit(inobj, infi):
    if re.search(r'\.ya?ml', infi):
        with open(infi, 'w') as f:
            yaml.dump(inobj, infi, sort_keys=False)
    if re.search(r'\.json', infi):
        with open(infi, 'w') as f:
            json.dump(inobj, infi)
    if re.search(r'\.txt', infi):
        with open(infi, 'a') as f:
            if type(inobj) == list:
                for l in inobj:
                    f.write(f"{l}\n")
    return(0)
