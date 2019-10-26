from NGramCollector import NGramCollector
from utility import tokenize_from_file

def main():
    with open('data1.txt') as f:
        print("Tokenizing...")
        tokens = tokenize_from_file(f)
        ng2 = NGramCollector(n=2)
        ng3 = NGramCollector(n=3)
        print("Training...")
        ng2.train(tokens)
        ng3.train(tokens)
        ngrams = (None, None, ng2, ng3)
    print("Done training!")
    
    new_token = input("Please enter an initial word => ")
    user_tokens = [new_token]
    LIMIT = 10
    while True:
        print(" ".join(user_tokens))
        suggestions = []
        for n in range(3,1,-1):
            if len(suggestions) < LIMIT and len(user_tokens) >= n-1:
                suggestions += [ w for w in ngrams[n].getSuggestions(user_tokens[-(n-1):], noProbability=True) if w not in suggestions]
        suggestions = suggestions[0:10] if len(suggestions) > 10 else suggestions # limit to 10
        print("Suggestions: {}".format(" | ".join(suggestions)))
        new_token = input("Enter a new word => ")
        user_tokens.append(new_token)
main()
