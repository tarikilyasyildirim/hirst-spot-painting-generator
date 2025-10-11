# Hirst Spot Painting Generator 🎨

A Python program that creates artwork inspired by Damien Hirst's famous spot paintings using the Turtle graphics library and color extraction from images.

## About This Project

This project was created as part of my ML/AI learning journey, inspired by the "100 Days of Code: The Complete Python Pro Bootcamp" course by Angela Yu on Udemy. It demonstrates the use of Python's Turtle graphics module combined with the colorgram library to extract colors from images and generate algorithmic art.

## Features

- Extracts colors from any source image using the `colorgram` library
- Generates a 10x10 grid of colored dots (100 dots total)
- Filters out very light colors to maintain visual contrast
- Creates a Damien Hirst-style spot painting automatically

## Prerequisites

Before running this project, make sure you have Python 3.x installed on your system.

## Usage

1. Place an image file named `picture.jpg` in the same directory as the script. This image will be used to extract the color palette.

2. Run the program:
```bash
python main.py
```

3. A window will open displaying your generated spot painting!

4. Close the window when you're done admiring your artwork.

## How It Works

1. **Color Extraction**: The program uses `colorgram` to extract 20 dominant colors from the source image
2. **Color Filtering**: Light colors (RGB values > 220) are filtered out to ensure vibrant results
3. **Grid Generation**: Using Turtle graphics, the program creates a 10x10 grid of dots
4. **Random Color Application**: Each dot is assigned a random color from the extracted palette

## Customization

You can customize the artwork by modifying these parameters in the code:

- **Grid size**: Change the range in the loops (currently 10x10)
- **Dot size**: Modify the `tom.dot(20, ...)` parameter
- **Spacing**: Adjust the `tom.forward(60)` value
- **Number of colors**: Change the extraction count in `colorgram.extract("picture.jpg", 20)`
- **Color filter threshold**: Modify the RGB values in the color filtering condition

## Learning Outcomes

Through this project, I learned:
- Working with the Turtle graphics library
- Extracting and manipulating color data from images
- Creating algorithmic art with Python
- Understanding RGB color values
- Implementing nested loops for grid patterns

## Acknowledgments

- **Angela Yu** - For the excellent Udemy course "100 Days of Code: The Complete Python Pro Bootcamp"
- **Damien Hirst** - For the artistic inspiration
- The Python community for the amazing libraries

## License
This project is free to use, modify, and distribute. Feel free to use it however you'd like!


---*Part of my ML/AI learning journey* 🚀
