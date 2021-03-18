import subprocess
from pathlib import Path
import os
from string import ascii_uppercase
import shutil
import argparse
from encrypt_all import remove_file_if_exists

def main():
    key = get_args()
    current_dir = Path(__file__).parent.absolute()
    cipher_dir = current_dir / "cipher"
    plain_dir = current_dir / "plain"

    if not cipher_dir.is_dir():
        os.mkdir(cipher_dir)
        print("Created directory 'cipher' - Place cipher files in this directory before running")
        exit(1)
    if not plain_dir.is_dir():
        os.mkdir(plain_dir)

    for cipher_file in cipher_dir.glob("*.txt"):

        decryption_command = f"./csencryption/csencryption.exe -key {key} -path {str(cipher_file)}"
        return_code = subprocess.call(decryption_command.split())
        if return_code == 5:
            print(f"Cannot decrypt '{cipher_file.name}': Invalid key")
        elif return_code != 5 and return_code != 0:
            print(f"Cannot decrypt '{cipher_file.name}':  return code {return_code}")
    
    # move all plain files to plain directory.
    for plain_file in cipher_dir.glob("*_plain.txt"):
        remove_file_if_exists(plain_dir, plain_file.name)
        shutil.move(plain_file, plain_dir)
        
    print("Completed decrypting files to " + str(plain_dir))
    


        
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="Key for AES decrypting all files in cipher dir")
    args = parser.parse_args()
    return args.key

if __name__ == "__main__":
    main()
