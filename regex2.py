# Siddharth Shah
# Completed Regular Expressions Tasks

import sys
reg = [ r"/^[.xo]{64}$/i",
        r"/^[xo]*\.[xo]*$/i",
        r"/^(x+o*)?\.|\.(o*x+)?$/i",
        r"/^.(..)*$/s",
        r"/^(0|1[01])([01]{2})*$/",
        r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
        r"/^(1?0)*1*$/",
        r"/^[bc]*[abc][bc]*$/",
        r"/^(c|b|a[bc]*a)+$/",
        r"/^(2[02]*|(1[02]*){2})+$/"]
print(reg[int(sys.argv[1])-40])