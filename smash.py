from pwn import *

import errno
import os
import signal
import functools

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            # pass
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator

@timeout(2)
def pwn_hello(exploit=''):
    # Start the process
    # exploit = 'f'
    input = 'ff' + exploit
    p = process(['./hello',  input])

    # Print the response
    print(p.recvall())
    
    print(p.proc.returncode)   
    return p.proc.returncode 

returns = []
for i in range(20):
    exploit = 'f'*i
    try:
        return_code = pwn_hello(exploit=exploit)
    except:
        print('timed out')
        return_code = -1
    
    returns.append({'exploit': exploit, 'len': len(exploit), 'code': return_code})

for item in returns:
    print(item)
