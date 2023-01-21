import itertools

words = "Hello Dylan you're the best friend I've ever had and I'm incredibly grateful for your presence in my life."

simple_words = "Hi bye Hello"

def shortest_word(find_shortest_word: str):
    individual_words = find_shortest_word.split()
    return min((i for i in find_shortest_word.split()), key=len)

print(shortest_word(simple_words))