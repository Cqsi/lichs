import sys
import pathlib

def set_api(key):
    
    file = open(str(pathlib.Path(__file__).parent.absolute()) + "\\key.txt", "w")
    file.write(key)
    file.close()
    print("The API-key " + key + " was entered and saved.")