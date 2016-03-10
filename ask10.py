
from bitarray import bitarray
import mmh3

class BloomFilter:

    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "--" + string + "--"
        return

bf = BloomFilter(500000, 7)
huge = []
# Open american-english dictionary
lines = open("c:/Python27/american-english.dic").read().splitlines()
for line in lines:
    bf.add(line)
    huge.append(line)
# Open the file "texteng", this file includes the text in english to see if there are mistakes
phrase = open("c:/Python27/texteng.py").read()
# Creating a list called "w"
w = phrase.split()
for word in w:
    print bf.lookup(word)
