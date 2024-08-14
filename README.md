# Book Layout Generator

A Python script to generate a book layout from a set of PNG images.

## Installation

To use this project, you'll need to have Python and the Pillow library installed on your system.
You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use the script, add your pages to `pages` directory
or provide directory yourself with `-i` flag:

```bash
python app.py -i pages
```

## Options
The script supports the following options:

- `-i` or `--input`: Specify the directory containing PNG images
- `-o` or `--output`: Specify the output directory for the generated book layout

## Process

### Before
<img src="pages/0.png" width="200" />
<img src="pages/1.png" width="200" />
<img src="pages/2.png" width="200" />
<img src="pages/3.png" width="200" />
<img src="pages/4.png" width="200" />

### After
<img src="out/0.png" width="200" />
<img src="out/1.png" width="200" />
<img src="out/2.png" width="200" />
<img src="out/3.png" width="200" />
<img src="out/4.png" width="200" />

Print pages according their output numbers:
1. Print page 0, then flip a piece of paper and print page 1.
2. Take another piece of paper and print page 2, then flip and print page 3.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull
request.
