import os
import hashlib
import struct

class Secret():
    def __init__(self):
        self.Value = os.urandom(8)
    def ToInt(self):
        return (struct.unpack('<L', self.Value [:4])[0] | struct.unpack('<L', self.Value [4:])[0] << 32) & 0x7FFFFFFFFFFFFFFF
    def Hex(self):
        return str('0x%016x' % self.ToInt())
    def __str__(self):
        return self.Value
    def __repr__(self):
        return self.Hed()
    
def Digest(password, salt):
    return hashlib.sha256(str(password) + str(salt)).hexdigest()