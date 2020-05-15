import sys

def set_api():
    key = sys.argv[1]
    
    file = open(sys.path[0] + "key.txt", "w")
    file.write(key)
    file.close()