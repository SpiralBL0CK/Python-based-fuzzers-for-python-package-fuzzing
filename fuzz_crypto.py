from Cryptodome.IO import PKCS8, PEM
from pythonfuzz.main import PythonFuzz
from Crypto.PublicKey import ECC
# import target library here

@PythonFuzz
def fuzz(buf):
    try:
    	# fuzz code here
        ECC.import_key(str(buf))
        PEM.decode(str(buf), str(buf))
    except ValueError: # handle expected errors here
        pass

if __name__ == '__main__':
    fuzz()

