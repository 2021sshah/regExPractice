# Siddharth Shah
# Completed Regular Expressions Tasks

import sys
reg = [ r"/^1?(0|11+)*1?$/",
        r"/^(?!.*(010|101))[01]*$/",
        r"/^(1|0)([10]*\1)?$/",
        r"/(?!(\w)+\w*\1\b)\b\w+/i",
        r"/(\w)+(\w)*\w*(\1(\w)+\w*(\2|\4)|\2\w*\1)\w*/i",
        r"/(?=(\w)+(\w*\1){2})\b(\1|(\w)(?!\w*\4))+\b/i",
        r"/(?!\w*([aeiou])\w*\1)\b(\w*[aeiou]){5}\w*/i",
        r"/^(?=(0|10*1)*$).(..)*$/",
        r"/^(?!00)(0|1(01*0)*1)+$/",
        r"/^(?!(0|1(01*0)*1)+$)[01]+$/"]
print(reg[int(sys.argv[1])-60])

# All Passed with 270 Length