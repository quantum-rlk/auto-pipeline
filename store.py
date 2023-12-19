#! /usr/bin/python3

from store_mgr import S3Mgr
import sys

if __name__ == '__main__':
   
    if len(sys.argv) < 3:
        print("missing argument")
        print("store <store_name> <option>")
        print("options: --flush,--list,--count")
        sys.exit()

    s3=S3Mgr(sys.argv[1])
    if '--flush' in sys.argv:
        s3.flush()
    elif '--list' in sys.argv:
        s3.list()
    elif '--count' in sys.argv:
        s3.count()


