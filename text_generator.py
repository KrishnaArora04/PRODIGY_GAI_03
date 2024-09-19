from markov_model import build_char_model, generate_text_char, build_word_model, generate_text_word

def read_text(file_path):
    """Read the content of the file."""
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def main():
    text = read_text('/Users/krishnaarora/Desktop/PRO/3/sample.txt')

    char_model = build_char_model(text, n=3)
    word_model = build_word_model(text, n=2)

    # Generate text
    start_char = text[:3] 
    generated_char_text = generate_text_char(char_model, start=start_char, length=200)
    generated_word_text = generate_text_word(word_model, start="Once upon", length=100)

    print("Generated Text (Characters):")
    print(generated_char_text)

    print("\nGenerated Text (Words):")
    print(generated_word_text)

if __name__ == "__main__":
    main()
