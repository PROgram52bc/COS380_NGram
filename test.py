from NGramCollector import NGramCollector
from SortedCounter import SortedCounterDictionary, SortedCounterLinkedList
from utility import tokenize_from_file_name
import time
import random
TEXT_FILES = ['data1.txt', 'data2.txt', 'data3.txt', 'data4.txt']
SUBCOLLECTORS = [SortedCounterLinkedList, SortedCounterDictionary]
# IMPLEMENTATIONS = [NGramCollector]

for name in TEXT_FILES:
    print("="*50)
    print("text file: {}".format(name))
    tokens = tokenize_from_file_name(name)
    print("# of tokens: {}".format(len(tokens)))
    print("# of unique tokens: {}".format(len(set(tokens))))
    for Subcollector in SUBCOLLECTORS:
        print("-"*50)
        print("Subcollector: {}".format(Subcollector.__name__))
        collector = NGramCollector(Subcollector) # initialize
        start = time.time()
        collector.train(tokens)
        end = time.time()
        print("training used: {} secs".format(end-start))
        n = 10000 # Take total time of n experiments

        # total_time = 0
        # for i in range(n):
        #     word = random.choice(tokens)
        #     follow = random.choice(tokens)
        #     start = time.time()
        #     suggestions = collector.getProbability(word, follow)
        #     end = time.time()
        #     total_time += end - start
        # print("{} getProbability: {} secs".format(n, total_time))

        total_time = 0
        for i in range(n):
            word = random.choice(tokens)
            start = time.time()
            suggestions = collector.getMostLikely(word)
            end = time.time()
            total_time += end - start
        print("{} getSuggestion: {} secs".format(n, total_time))
    print()
