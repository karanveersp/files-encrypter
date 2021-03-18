import os
import shutil
from pathlib import Path

def main():
    
    current_dir = Path(__file__).parent.absolute()
    cipher_dir = current_dir / "cipher"

    for cf in cipher_dir.glob("*.txt"):
        os.remove(cf)
    
    print("Cleared cipher dir")


if __name__ == "__main__":
    main()
