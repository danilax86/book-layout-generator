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
![0.png](pages/0.png)
![1.png](pages/1.png)
![2.png](pages/2.png)
![3.png](pages/3.png)
![4.png](pages/4.png)

### After
![0.png](out/0.png)
![1.png](out/1.png)
![2.png](out/2.png)
![3.png](out/3.png)
![4.png](out/4.png)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull
request.
