# ImageCoder
imageCoder is inspired by Pete Corey's [blog article](http://www.east5th.co/blog/2017/02/13/build-your-own-code-poster-with-elixir/) and [commit.io](https://commits.io/)'s service. 

Contrary to the article by Pete, this program uses python instead of elixir and is a lot faster. The speed advantage is mainly due to operating directly on png-images and a slightly different approach to parsing the text. While the former approach limits one color per character, imageCoder overlays the text over the image and makes it transparent, thus the image can have multiple colors per character.

The program takes a png-file as a background image, a string for the name of the output image, and a text-file with text/code, furthermore, the user can directly change the font, font-size, and the width and height for the output image.

# Example

Without much further ado, here is a simple output image created by imageCoder using the python logo (taken from [Wikimedia](https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg) and converted to png using [ImageMagick](https://www.imagemagick.org/script/index.php) `convert -background none -density 1000 -resize 1000x python.svg python.png`) and the source-code for the merging function of pandas (as found [here](https://github.com/pandas-dev/pandas/blob/master/pandas/tools/merge.py)).

The command to recreate the picture below, is `./imageCoder.py -i python.png -o pythonCoder.png -t merge_pandas.py -f /usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-B.ttf -s 10 -H 2000 -w 2000` (the best results imho come with a mono-spaced font)

![PythonCoder.png](pythonCoder.png "PythonCoder.png")

If you want to increase the resolution of the image, I would suggest increasing both the size of the image to something above 10k and the font-size to roughly 20-40.

# Usage

To see the full usage, run `./imageCoder.py -h`, which currently shows you

``` 
usage: imageCoder.py [-h] -i IMAGEFILE -o IMAGEOUT -t TEXTFILE [-f FONT]
                     [-s FONTSIZE] [-w WIDTH] [-H HEIGHT]

imageCoder 0.1 (February 2017) by Author: David Zimmermann

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGEFILE, --imageFile IMAGEFILE
                        input file for the background image
  -o IMAGEOUT, --imageOut IMAGEOUT
                        filename for the output image
  -t TEXTFILE, --textFile TEXTFILE
                        input file for the text/code
  -f FONT, --font FONT  fontname or font path to a truetype-font
  -s FONTSIZE, --fontSize FONTSIZE
                        font size in pt
  -w WIDTH, --width WIDTH
                        width of the output image
  -H HEIGHT, --height HEIGHT
                        height of the output image

```

# Installation
To use imageCoder make sure you have the following dependencies installed

## Dependencies

- Python 2.7.12 
- Pillow 2.2.1

To install Pillow, use `sudo pip install Pillow`.

Then you can download the tool with

`git clone https://github.com/DavZim/imageCoder.git`

use wget and unzip
`wget https://github.com/DavZim/imageCoder/archive/master.zip && unzip master.zip && cd imageCoder-master`

or simply download, unzip, and navigate to the unzipped folder manually.

Make sure that the program is executable (`chmod +x imageCoder.py`) or use `python imageCoder.py -i ...` instead of `./imageCoder.py -i ...`. Et voila, you are ready to go.


# Collaboration

Lastly, if you like this project, feel that it needs more functionality, find a mistake, or simply want to contribute, you are more than welcome to open an issue, fork the project, or make a pull-request. Also any kind of feedback is always welcome.
