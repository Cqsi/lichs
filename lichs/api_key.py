import sys
from pathlib import Path

def set_api(key):

    token_file = Path(__file__).parent.absolute() / "key"
    token_file.write_text(key)
    print("The API-token " + key + " was entered and saved.")
