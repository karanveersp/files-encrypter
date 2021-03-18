from pathlib import Path
import os
import shutil

def main():
    
    current_dir = Path(__file__).parent.absolute()
    plain_dir = current_dir / "plain"
    
    for pf in plain_dir.glob("*.txt"):
        os.remove(pf)

    print("Cleared plain files")

if __name__ == "__main__":
    main()
