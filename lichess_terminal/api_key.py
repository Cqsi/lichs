import sys

def set_api():
    key = sys.argv[0]
    
    file = open("api_key.txt", "w")
    file.write(key)
    file.close()