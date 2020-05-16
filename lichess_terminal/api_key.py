import sys
import pathlib

def set_api(key):
    print("THIS RUNS")
    print(str(pathlib.Path(__file__).parent.absolute()) + "key.txt")
    
    file = open(str(pathlib.Path(__file__).parent.absolute()) + "key.txt", "w")
    file.write(key)
    file.close()