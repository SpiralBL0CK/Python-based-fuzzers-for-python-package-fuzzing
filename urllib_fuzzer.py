#from pyasn1.codec.der.decoder import decode
#from pyasn1_modules import rfc2459
#from pyasn1.error import PyAsn1Error
from pythonfuzz.main import PythonFuzz
from urllib.parse import urlparse

@PythonFuzz
def fuzz(buf):
    try:
    #	certType = rfc2459.Certificate(); 
    #	cert, rest = decode(buf, asn1Spec=certType)
        urlparse(buf)
        
    except UnicodeDecodeError:
        pass
    except ValueError:
        pass

if __name__ == '__main__':
    fuzz()

