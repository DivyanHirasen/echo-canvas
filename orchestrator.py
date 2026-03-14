from generate_quote import generate_quote
from utils import read_template, save_quote

if __name__ == "__main__":
    template = read_template("templates/quote/stoic.txt")
    quote = generate_quote(template)
    entry = save_quote(quote)

    print(f"Saved quote [{entry['id']}]")
    print("---------")
    print(quote)
