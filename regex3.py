# Siddharth Shah
# Completed Regular Expressions Tasks

import sys
reg = [ r"/(\w)+\w*\1\w*/i",
        r"/(\w)+(\w*\1){3}\w*/i",
        r"/^(1|0)([10]*\1)?$/",
        r"/(?=\w*cat)\b\w{6}\b/i",
        r"/(?=\w*bri)(?=\w*ing)\b\w{5,9}\b/i",
        r"/(?!\w*cat)\b\w{6}\b/i",
        r"/(?!(\w)+\w*\1)\b\w+/i",
        r"/^(?!.*10011)[10]*$/",
        r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",
        r"/^(?!.*1.1)[10]*$/"]
print(reg[int(sys.argv[1])-50])