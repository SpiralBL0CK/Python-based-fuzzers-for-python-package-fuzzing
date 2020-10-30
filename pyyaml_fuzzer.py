import yaml
from pythonfuzz.main import PythonFuzz
# import target library here

@PythonFuzz
def fuzz(buf):
    try:
    	# fuzz code here
        yaml.load(str(buf))
    except yaml.YAMLError as e: # handle expected errors here
        #print(e)
        #print("we crash")
        pass

if __name__ == '__main__':
    fuzz()

