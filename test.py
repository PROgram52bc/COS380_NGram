from NGramCollector import NGramCollector
from utility import tokenize_from_file_name
import time
import random
TEXT_FILES = ['data.txt','data2.txt','data3.txt', 'data4.txt']
IMPLEMENTATIONS = [NGramCollector]

for name in TEXT_FILES:
    print("="*50)
    print("text file: {}".format(name))
    tokens = tokenize_from_file_name(name)
    print("# of tokens: {}".format(len(tokens)))
    print("# of unique tokens: {}".format(len(set(tokens))))
    for Collector in IMPLEMENTATIONS:
        print("-"*50)
        print("implementation: {}".format(Collector.__name__))
        collector = Collector() # initialize
        start = time.time()
        collector.train(tokens)
        end = time.time()
        print("training used: {} secs".format(end-start))
        n = 1000 # Take an average of n experiments

        total_time = 0
        for i in range(n):
            word = random.choice(tokens)
            follow = random.choice(tokens)
            start = time.time()
            suggestions = collector.getProbability(word, follow)
            end = time.time()
            total_time += end - start
        print("{} getProbability: {} secs".format(n, total_time))

        total_time = 0
        for i in range(n):
            word = random.choice(tokens)
            start = time.time()
            suggestions = collector.getSuggestions(word)
            end = time.time()
            total_time += end - start
        print("{} getSuggestions: {} secs".format(n, total_time))
    print()
