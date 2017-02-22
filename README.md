# ImageCoder
imageCoder is inspired by Pete Corey's [blog article](http://www.east5th.co/blog/2017/02/13/build-your-own-code-poster-with-elixir/) and [commit.io](www.commits.io)'s service. 

Contrary to the article by Pete, this program uses python instead of elixir and is a lot faster. The speed advantage is mainly due to operating directly on png-images and a slightly different approach to parsing the text. While the former approach limits one color per character, imageCoder uses the colors of the image, thus it can have multiple colors per character.

The program takes a png-file as a background image, a string for the output image, and a text-file with text/code, furthermore, the user can directly change the font, font-size, and the width and height for the output image.

# Example

Without much further ado, here is a simple output image created by imageCoder using the python logo (taken from [Wikimedia](https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg) and converted to png) and the source-code for the merging function of pandas (as found [here](https://github.com/pandas-dev/pandas/blob/master/pandas/tools/merge.py)).

The command to recreate the picture below, is `./imageCoder.py -i python.png -o pythonCoder.png -t merge_pandas.py -f /usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-B.ttf -s 10` (the best results imho come with a mono-spaced font)

![PythonCoder.png](pythonCoder.png "PythonCoder.png")

If you want to increase the resolution of the image, I would suggest increasing both the size of the image to something above 10k and the font-size to roughly 20-40.

# Installation
To use imageCoder make sure you have the following dependencies installed

## Dependencies

Python 2.7.12 
Pillow 2.2.1

To install Pillow, use `sudo pip install Pillow`.


# Collaboration

Lastly, if you like this project, feel that it needs more functionality, find a mistake, or simply want to contribute, you are more than welcome to open an issue/fork the project or make a pull-request.
