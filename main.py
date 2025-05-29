import random
import click
from PIL import Image, ImageEnhance


# Crisp 2000s-era 480p
MAX_RES = 480


@click.command("ms-teams-image-simulator")
@click.argument("input", type=click.File('rb'))
@click.argument("output", type=click.File('wb'))
def main(input, output):
    img = Image.open(input)
    width, height = img.size
    ratio = height / MAX_RES
    width = min(width, round(width / ratio))
    height = min(height, round(height / ratio))
    print(width, height)
    img = img.resize((width, height))
    if random.randint(1, 10) == 1:
        # Darken image by 100%
        img = ImageEnhance.Brightness(img).enhance(0)
    # 10% quality for the best possible compression
    img.save(output, quality=10)


if __name__ == "__main__":
    main()
