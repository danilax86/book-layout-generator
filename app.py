import os, argparse

from PIL import Image, ImageFile
from dataclasses import dataclass

PAGES_PATH: str = 'pages'
OUTPUT_PATH: str = 'out'


def fatal(err_msg):
    print(err_msg)
    exit(1)


@dataclass
class Page:
    num: int
    file: ImageFile

    def __init__(self, num, file):
        self.num = num
        self.file = file


@dataclass
class PageBlock:
    left: Page
    right: Page
    filePath: str = ""

    def __init__(self, left, right, file_path=""):
        self.left = left
        self.right = right
        self.filePath = file_path


def get_png_files(dir_path):
    if not os.path.exists(dir_path):
        fatal('No such directory: ' + dir_path)

    png_files = [file for file in os.listdir(dir_path) if file.endswith('.png')]
    if len(png_files) == 0:
        fatal('No png files in directory: ' + dir_path)

    return sorted(png_files, key=lambda x: x)


def split_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    half_width = width // 2
    left_half = image.crop((0, 0, half_width, height))
    right_half = image.crop((half_width, 0, width, height))
    return left_half, right_half


def create_page_blocks(png_files, dir_path):
    page_blocks = []
    for i in range(len(png_files)):
        l, r = split_image(dir_path + '/' + png_files[i])
        page_blocks.append(PageBlock(Page(len(page_blocks) + i, l), Page(len(page_blocks) + i + 1, r), png_files[i]))
    return page_blocks


def book_layout(page_blocks):
    book_layout_blocks = []
    for i in range(len(page_blocks)):
        left = page_blocks[i].left
        right = page_blocks[-i - 1].right
        book_layout_blocks.append(PageBlock(left, right))
    return book_layout_blocks


def combine_images(left, right):
    combined = Image.new('L', (left.width + right.width, max(left.height, right.height)))
    combined.paste(left, (0, 0))
    combined.paste(right, (left.width, 0))
    return combined


def save_image(image, file_name):
    image.save(file_name)


def save_images_from_page_blocks(page_blocks, path):
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(len(page_blocks)):
        combined = combine_images(page_blocks[i].left.file, page_blocks[i].right.file)
        if i % 2 == 0:
            save_image(combined, path + '/' + str(len(page_blocks) - i - 1) + '.png')
        else:
            save_image(combined, path + '/' + str(i) + '.png')


def main():
    parser = argparse.ArgumentParser(description='Create book layout from images')
    parser.add_argument('-i', '--input', type=str, required=False, help='input folder with images')
    parser.add_argument('-o', '--output', type=str, required=False, help='output folder')
    args = parser.parse_args()

    pages_path = args.input
    output_path = args.output

    if pages_path is None:
        pages_path = PAGES_PATH
    if output_path is None:
        output_path = OUTPUT_PATH

    save_images_from_page_blocks(book_layout(create_page_blocks(get_png_files(pages_path), pages_path)), output_path)


if __name__ == '__main__':
    main()
