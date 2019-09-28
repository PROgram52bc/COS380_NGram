import random

class NGramCollector:
    DELIMITER="&"
    def __init__(self, n):
        """ 'n' is the size of the n-gram """
        if n < 2:
            raise Exception("n cannot be less than 2")
        self.N = n
        self.collection = {  }
        self.collectionCount = 0
        pass

    def _hash(self, multi_token):
        """ multi_token should be a string (n=2) or an iterable of strings (n>2)
        returns a single string """
        if isinstance(multi_token, str):
            return multi_token
        else:
            tokens = list(multi_token)
            if len(tokens) != self.N-1:
                raise Exception("size of the multi_token ({:d}) does not correspond to the size of n-gram - 1 ({:d})".format(len(tokens), self.N-1))
            return self.DELIMITER.join(multi_token)

    def train(self, data):
        """ 'data' should be an iterable of strings 
        which represents the sequence of tokens """
        c = self.collection
        for i in range(len(data)-self.N+1):
            current_token = self._hash(data[i:i+self.N-1]) # a string representing current n-1 tokens
            next_token = data[i+self.N-1] # the next token
            # print("{:d}: {}".format(i, current_token))
            if current_token in c: # if the 'given' already exists
                c[current_token]['count'] += 1 # increment its count
                if next_token in c[current_token]['children']: # if the 'follower' exists
                    c[current_token]['children'][next_token] += 1 # increment its count as well
                else: # if 'follower' does not exist
                    c[current_token]['children'][next_token] = 1 # set it to 1
            else: # if the 'given' does not exist, create both the count for itself and its children
                c[current_token] = {'count': 1, 'children': {
                    next_token: 1
                }}
            self.collectionCount += 1

    def getRawProbability(self, given):
        """ returns a number between 0 and 1 as the probability of 'token' among all tokens. 
        token should be an iterable of length n-1, or a string, if n=2 """
        c = self.collection
        given_hash = self._hash(given)
        return c[given_hash]['count']/self.collectionCount if given_hash in c else 0.0

    def getProbability(self, follower, given):
        """ 'follower' is the token that should follow 'given' 
        'given' is a token or an iterable of tokens
        returns a number between 0 and 1 as the probability of 'follower' following 'given' """
        c = self.collection
        given_hash = self._hash(given)
        if given_hash in c and follower in c[given_hash]['children']:
            return c[given_hash]['children'][follower]/c[given_hash]['count']
        else:
            return 0.0

    def getProbabilities(self, given):
        """ returns a dict, where all possible words that follows 'given' are keys, and their probabilities are the values """
        c = self.collection
        given_hash = self._hash(given)
        if given_hash in c:
            return { k: c[given_hash]['children'][k]/c[given_hash]['count'] for k in c[given_hash]['children'] }
        else:
            return {  }
            
    def getSuggestions(self, given, noProbability=False):
        """ returns a sorted list of tuples, sorted by their probabilities of appearing after 'given', where the first value in the tuple is the token, the second is the probability """
        suggestions = sorted(self.getProbabilities(given).items(), key=lambda kv:kv[1], reverse=True)
        if noProbability:
            suggestions = [ wp[0] for wp in suggestions ]
        return suggestions
    
    def randomWord(self, given):
        """ get a random word that follows the 'given', based on the probability """
        if self.getRawProbability(given) == 0.0: 
            return None
        word_list = self.getSuggestions(given)
        probability = random.random()
        for wp in word_list:
            if probability < wp[1]:
                print("hit word-probability: ({},{}) with probability {}".format(wp[0],wp[1],probability))
                return wp[0]
            else:
                print("missed word-probability: ({},{}) with probability {}".format(wp[0],wp[1],probability))
                probability -= wp[1]
                print("new probability: {}".format(probability))
