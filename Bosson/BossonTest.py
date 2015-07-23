# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import json

file_path = r"C:\workspace\Taikor_NLP_service\Thirdparty_NLP_WebAPI\Bosson\corpos\msr_test.txt"
with open(file_path, "r", encoding="utf8") as f:
    s = f.read()

nlp = BosonNLP('2ZmFSLeL.3212.Y6W7eOViuyZZ')
pos = nlp.tag(s)

dump = json.dumps(pos)

with open("pos", "w") as f:
    f.write(dump)