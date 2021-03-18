"""
Script that encrypts all txt files under the 'plain' sub-directory.
Moves all cipher text to 'cipher' sub-directory.
"""
import subprocess
from pathlib import Path
import os
import shutil
import argparse


def main():
    key = get_args()
    current_dir = Path(__file__).parent.absolute()
    cipher_dir = current_dir / "cipher"
    plain_dir = current_dir / "plain"

    for text_file in plain_dir.glob("*.txt"):
        encryption_command = f"./csencryption/csencryption.exe -key {key} -path {str(text_file)} -e"
        return_code = subprocess.call(encryption_command.split())
        if return_code != 0:
            raise Exception(f"Error while encrypting - return code {return_code}")

    # move all cipher files to cipher directory.
    for cipher_file in plain_dir.glob("*_cipher.txt"):
        remove_file_if_exists(cipher_dir, cipher_file.name)
        shutil.move(cipher_file, cipher_dir)

    print("Completed encrypting files to " + str(cipher_dir))


def remove_file_if_exists(dirpath, filename):
    if dirpath.joinpath(filename).is_file():
        os.remove(dirpath.joinpath(filename))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="Key for AES encrypting all files in 'plain' dir")
    args = parser.parse_args()
    return args.key

if __name__ == "__main__":
    main()
