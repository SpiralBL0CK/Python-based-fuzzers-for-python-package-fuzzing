from urllib.parse import parse_qs
from pythonfuzz.main import PythonFuzz
# import target library here

@PythonFuzz
def fuzz(buf):
    try:
    	# fuzz code here
        parse_qs("https://www.example.com/{}adi-url={}".format(str(buf),str(buf)))
    except Error: # handle expected errors here
        pass

if __name__ == '__main__':
    fuzz()
