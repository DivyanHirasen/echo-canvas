from generate_quote import generate_quote
from utils import read_template, save_quote
from image_processing_utils import add_quote_to_image

if __name__ == "__main__":
    #template = read_template("templates/quote/stoic.txt")
    #quote = generate_quote(template)
    #entry = save_quote(quote)

    quote = "In the stillness of existence, remember: what you cherish lies within; the tempest outside is mere illusion, immutable to your essence."

    #print(f"Saved quote [{entry['id']}]")
    print("---------")
    print(quote)

    image_path = "generated_image.jpg"
    output_path = f"outputs/{"5"}_quote.jpg"
    add_quote_to_image(image_path, quote, output_path=output_path)
