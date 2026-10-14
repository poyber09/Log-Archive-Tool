#!/usr/bin/python3

import argparse
import os
import tarfile
from datetime import datetime
import sys

def compressing_files(log_path, arg_flag):

    if os.path.isdir(log_path):

        time_format = datetime.now().strftime("%Y%m%d_%H%M%S")

        compressed_files_directory_path = os.path.expanduser("~/system_log_archive/")
        os.makedirs(compressed_files_directory_path, exist_ok=True)
        with tarfile.open(f"{compressed_files_directory_path}logs_archive_{time_format}.tar.gz", "w:gz") as tar:
            tar.add(log_path)
        print(f"log directory compressed in {compressed_files_directory_path} as ---> logs_archive_{time_format}.tar.gz")
        
        if arg_flag:
                decompress_tar(f"{compressed_files_directory_path}logs_archive_{time_format}.tar.gz")
    
    else:
        
        print("Your log path doesn't exist!", file=sys.stderr)
        sys.exit(1)        

def decompress_tar(tar_path):
    print(tar_path)
    if not os.path.isfile(tar_path):
        print("Archive doesn't exist!")
        sys.exit(1)

    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=os.path.expanduser("~/system_log_archive/"))

    print(f"Extracted: {tar_path}")

def parse_args():

    parser = argparse.ArgumentParser(prog='log-archive', description='Archives the log files')

    parser.add_argument('log_directory', metavar='<log-directory>', help='the directory which contains log file')
    parser.add_argument('-d', '--decompress', action="store_true",help="decompress the output tar")
    return parser.parse_args()

def main():

    args = parse_args()
    compressing_files(args.log_directory, args.decompress)

if __name__ == "__main__":
    main()
