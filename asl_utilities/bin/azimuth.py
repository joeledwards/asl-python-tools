#!/usr/bin/env python
import asl

import os

def main():
    os.popen('java -jar %s/utils/Azimuth.jar' % asl.path)

if __name__ == '__main__':
    main()

