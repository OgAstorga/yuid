import random
from math import log2
import time
import uuid

def base62(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    alen = len(alphabet)

    parts = []
    while x != 0:
        parts.append(alphabet[x % alen])
        x = int(x / alen)

    parts.reverse()

    return ''.join(parts)


def getnode():
    fullnode = uuid.getnode()

    p0 = (fullnode & 0x000000000fff) >> 0
    p1 = (fullnode & 0x000000fff000) >> 12
    p2 = (fullnode & 0x000fff000000) >> 24
    p3 = (fullnode & 0xfff000000000) >> 36

    return p0 ^ p1 ^ p2 ^ p3

def yuid():
    rand = random.SystemRandom().getrandbits(10) # 10 bits
    node = getnode() # 12 bits
    tnow = int(time.time() * 1000) # 42 bits

    bits = (rand << 54) + (node << 42) + (tnow)

    return base62(bits)
