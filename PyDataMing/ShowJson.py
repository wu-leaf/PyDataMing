# -*- coding: utf-8 -*-
import json

son = json
def showJson(dict):
      str = son.dumps(dict, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
      print str
