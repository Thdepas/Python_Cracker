#!/usr/bin/env python3
# coding:utf-8
import time
import atexit
import hashlib
import argparse
import multiprocessing
from utils import *
from crackFunc import *


parser = argparse.ArgumentParser(
    description="(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆ Password Cracker")
parser .add_argument("-f", "--file", dest="file",
                     help="path of the dictionary file", required=False)
parser .add_argument("-g", "--gen", dest="gen",
                     help="generate MD5 hash of password", required=False)
parser .add_argument("-md5", dest="md5",
                     help="hashed password (MD5)", required=False)
parser .add_argument("-l", dest="plength",
                     help="Password length", required=False, type=int)
parser .add_argument("-o", dest="online",
                     help="Look for hash online", required=False, action='store_true')
parser .add_argument("-p", dest="pattern",
                     help="Use pattern for pswd (^⁼MAJ, *=MIN, -=DIGIT)", required=False)

args = parser.parse_args()
print(args.file)

processes = []
work_queue = multiprocessing.Queue()
done_queue = multiprocessing.Queue()
cracker = Cracker()


def display_time():
    print("Durée : " + str(time.time() - debut) + " secondes")


debut = time.time()
atexit.register(display_time)

if args.gen:
    print("MD5 HASH OF " + args.gen + " : " +
          hashlib.md5(args.gen.encode("utf8")).hexdigest())

if args.md5:
    print('CRACKING HASH ' + args.md5)
    if args.file:
        print("USING DICTIONNARY FILE " + args.file)
        p1 = multiprocessing.Process(target=Cracker.work, args=(
            work_queue, done_queue, args.md5, args.file, Order.ASCEND))

        work_queue.put(cracker)
        p1.start()

        p2 = multiprocessing.Process(target=Cracker.work, args=(
            work_queue, done_queue, args.md5, args.file, Order.DESCEND))

        work_queue.put(cracker)
        p2.start()

        notfound = 0

        while True:
            data = done_queue.get()
            if data == "FOUND" or data == "NOT FOUND":
                p1.kill()
                p2.kill()
                break

        #hash_crack(args.md5, args.file)
    elif args.plength:
        print("USING INCREMENTAL MODE " + str(args.plength) + " LETTER(s)")
        Cracker.crack_incr(args.md5, args.plength)
    elif args.online:
        print("USING ONLINE MODE ")
        Cracker.crack_online(args.md5)
    elif args.pattern:
        print("USING PATTERN MODE " + args.pattern)
        Cracker.crack_smart(args.md5, args.pattern)
    else:
        print("Please choose either -f or -l argument")
else:
    print("MD5 HASH NOT PROVIDED")
