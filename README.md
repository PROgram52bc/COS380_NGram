# Ngram project

> This project contains multiple parts

-   `NGramCollector.py`

    This file contains a single class `NGramCollector`, which can have a configurable `n` parameter in constructor. It then collects all `n`-grams and `n-1`-grams and does analysis with those data. It also takes a parameter `subcollectorclass` parameter which specifies the underlying structure that it uses to collect the `n-1`-grams.

-   `SortedCounter.py`

    This file has multiple classes that can be used as `subcollectorclass` in `NGramCollector`

-   `test.py`

    This file tests the efficiency of method `train` and `getSuggestions` in `NGramCollector` for different combination of text corpuses and `subcollectorclass`

-   `data*.txt`

    These are data files that contains tokens to be analyzed.

-   `wordHintDemo.py`

    This file is a small interactive demonstration of how `NGramCollector` can be used to do word prediction.

-   `utility.py`
    contains some helper methods (that can be modified) for processing the stream of tokens
