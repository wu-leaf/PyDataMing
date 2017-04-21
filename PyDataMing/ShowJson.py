# -*- coding: utf-8 -*-
import json


son = json
def showJson(url,dict):
      str = son.dumps(dict, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
      string = str.encode("utf-8")

      allstr = url+" "+string+"\n"
      if allstr:
       fo = open("result.txt", "a+")
       fo.writelines(allstr);
      # 关闭打开的文件
       fo.close()
      print allstr
