# -*- coding: UTF-8 -*-

from random import randint, choice
from string import ascii_lowercase as lowercase
from time import ctime
import numpy as np

doms = ('com', 'edu', 'net', 'org', 'gov')
k = ('D', 'I', 'N', 'W', 'E')
v = ('DEBUG', 'INFO', 'NOTICE', 'WARNING', 'ERROR')
loglevel = dict(zip(k, v))


def genloglevel():
    n = randint(0, 99)
    if n < 85:
        return loglevel['N']
    elif n < 95:
        return loglevel['W']
    elif n < 100:
        return loglevel['E']
    else:
        return False


def genkeyword1():
    n = randint(0, 99)
    if n < 70:
        return "net key"
    else:
        return "others"


def genkeyword2():
    n = randint(0, 99)
    if n < 70:
        return "net key rate"
    else:
        return "others"


f = open("genlog.txt", "w")

lines = randint(10000, 100000)
net_key_num = np.random.normal(250000, 5000, lines)
net_key_rate = np.random.normal(40000, 1000, lines)
for i in range(lines):
    dtint = randint(0, 8999999999)  # pick date
    dtstr = ctime(dtint)  # date string

    loglv = genloglevel()

    shorter = randint(4, 7)  # login shorter
    em = ''
    for j in range(shorter):  # generate login
        em += choice(lowercase)

    longer = randint(shorter, 12)  # domain longer
    dn = ''
    for j in range(longer):  # create domain
        dn += choice(lowercase)

    msg = ''
    for j in range(randint(5, 10)):
        wordlen = randint(3, 10)
        word = ''
        for w in range(wordlen):
            word += choice(lowercase)
        msg += word + ' '

    # net_key_num = randint(150000, 250000)
    # net_key_rate = randint(3000000, 5000000) / 100.0
    kw1 = genkeyword1()
    kw2 = genkeyword2()

    f.write(
        '[%s] %s::%s@%s.%s::%d-%d-%d %s %d, %s %s %.2f\n' % (
            dtstr, loglv, em, dn, choice(doms), dtint, shorter, longer,
            kw1, net_key_num[i], msg, kw2, net_key_rate[i]))

f.close()
