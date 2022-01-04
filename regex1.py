# Siddharth Shah
# Completed Regular Expressions Tasks

import sys
reg = [ r"/^0$|^10[01]$/",
        r"/^[01]*$/",
        r"/0$/",
        r"/\w*[aeiou]\w*[aeiou]\w*/i",
        r"/^0$|^1[01]*0$/",
        r"/^[01]*110[01]*$/",
        r"/^.{2,4}$/s",
        r"/^\d{3} *-? *\d\d *-? *\d{4}$/",
        r"/^.*?d\w*/im",
        r"/^[01]?$|^0[01]*0$|^1[01]*1$/"]
print(reg[int(sys.argv[1])-40])