import engine

from engine import (os, random, sys, datetime, Environment, PackageLoader, markdown)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        engine.main(sys.argv[1])
    else:
        print("Enter section name you want to generate")
