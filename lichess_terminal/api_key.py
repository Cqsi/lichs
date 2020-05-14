import sys

def set_api():
    key = sys.argv[0]
    
    file = open("key.txt", "w")
    file.write(key)
    file.close()