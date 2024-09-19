from collections import defaultdict
import random

def build_char_model(text, n=1):
    model = defaultdict(lambda: defaultdict(int))
    for i in range(len(text) - n):
        current_state = text[i:i+n]
        next_char = text[i+n]
        model[current_state][next_char] += 1
    return model

def generate_text_char(model, start, length=100):
    current_state = start
    result = start
    for _ in range(length):
        next_chars = list(model[current_state].keys())
        if not next_chars:
            break
        next_char = random.choices(next_chars, weights=model[current_state].values())[0]
        result += next_char
        current_state = current_state[1:] + next_char
    return result

def build_word_model(text, n=1):
    words = text.split()
    model = defaultdict(lambda: defaultdict(int))
    for i in range(len(words) - n):
        current_state = tuple(words[i:i+n])
        next_word = words[i+n]
        model[current_state][next_word] += 1
    return model

def generate_text_word(model, start, length=100):
    current_state = tuple(start.split())
    result = start
    for _ in range(length):
        next_words = list(model[current_state].keys())
        if not next_words:
            break
        next_word = random.choices(next_words, weights=model[current_state].values())[0]
        result += ' ' + next_word
        current_state = tuple(list(current_state[1:]) + [next_word])
    return result
