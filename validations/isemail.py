# https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script

import re

def emailAddress(addressToVerify):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    if match is None:
        return False
    else:
        return True
