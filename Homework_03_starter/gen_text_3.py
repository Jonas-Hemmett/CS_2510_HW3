"""
CS 2990 / 2510
Alice In Wonderland as second-order Markov process
"""
from collections import defaultdict
import random
import string
import textwrap


CORPUS = 'alice.txt'
SEED = ('alice', 'was', 'beginning')


class SecondOrderMarkov:
    def __init__(self):
        self.transitions = defaultdict(list)

    def train(self, corpus_):
        words = corpus_.split()
        # Sliding window...
        for i in range(len(words) - 3):
            state = (words[i], words[i + 1], words[i + 2])  # Three of words as the state
            next_word = words[i + 3]
            self.transitions[state].append(next_word)

    def generate(self, length=20):
        # Start with a random word pair from the corpus
        # state = random.choice(list(self.transitions.keys()))
        state = SEED
        generated_text = list(state)

        for _ in range(length - 3):
            next_word = random.choice(self.transitions[state])
            generated_text.append(next_word)
            state = (state[1], state[2], next_word)
        print(len(self.transitions))

        return ' '.join(generated_text)

def get_tidied_corpus(file_path):
    # Create a translation table excluding hyphens from punctuation
    punctuation = string.punctuation.replace('-', '')
    translator = str.maketrans('', '', punctuation)

    cleaned_lines = []
    try:
        with open(file_path, 'r') as fh:
            for line in fh:
                if not line.startswith('#'):
                    line = line.strip()
                    # Remove punctuation except for hyphens
                    line = line.translate(translator)
                    # Convert to lowercase and split into words
                    words = line.lower().split()
                    # Join the words back together and store
                    cleaned_lines.append(' '.join(words))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""

    return ' '.join(cleaned_lines)


def print_wrapped_text(text, width):
    wrapped_lines = textwrap.wrap(text, width=width)
    for line in wrapped_lines:
        print(line)


if __name__ == '__main__':
    corpus = get_tidied_corpus(CORPUS)
    markov_chain = SecondOrderMarkov()
    markov_chain.train(corpus)
    result = markov_chain.generate(200)
    print_wrapped_text(result, 70)
