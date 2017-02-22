#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import re
import sys
import argparse
import os.path

##
## @brief      Recreates an image with code/text as pixels
##
## @param      img       The image
## @param      text      The text
## @param      font      The font
## @param      fontSize  The font size
##
## @return     the altered image
##
def textOverlayInverse(img, text, font = "default", fontSize = 10):
	front = Image.new('RGBA', img.size)
	out = Image.new('RGBA', img.size, (255,255,255,0))
	draw = ImageDraw.Draw(front)
	if (font == "default"):
		font = ImageFont.load_default()
	else:
		font = ImageFont.truetype(font, fontSize)

	# determining the size of the font...
	sentence = "The quick brown fox jumps over the lazy dog"
	font_w, font_h = font.getsize(sentence)
	font_w = font_w / len(sentence) # to get the approximate average width of the text

	nRowChars = img.size[0] / font_w + 1

	y_text = 0
	a, img_height = img.size
	textTmp = text
	while y_text < img_height:
		draw.text((0, y_text), textTmp[1:nRowChars], font = font)
		textTmp = textTmp[nRowChars + 1:]
		if (len(textTmp) <= nRowChars):
			textTmp += text # repeat the characters if necessary
		y_text += font_h

	mask = ImageEnhance.Brightness(front).enhance(0)
	out.paste(img, (0,0), mask)
	return out

##
## @brief      Main Function
##
## @param      argv  The argv
##
## @return     
##
def main(argv):

	parser = argparse.ArgumentParser(description = "imageCoder 0.1 (February 2017) by Author: David Zimmermann")

	parser.add_argument("-i", "--imageFile", help = "input file for the background image", required = True)
	parser.add_argument("-o", "--imageOut", help = "filename for the output image", required = True)
	parser.add_argument("-t", "--textFile", help = "input file for the text/code", required = True)
	parser.add_argument("-f", "--font", help = "fontname or font path to a truetype-font", required = False, default = "default")
	parser.add_argument("-s", "--fontSize", help = "font size in pt", required = False, default = 10, type=int)
	parser.add_argument("-w", "--width", help = "width of the output image", required = False, default = 1024, type=int)
	parser.add_argument("-H", "--height", help = "height of the output image", required = False, default = 768, type=int)
	
	args = parser.parse_args()

	inFile = args.imageFile
	outFile = args.imageOut
	textFile = args.textFile
	font = args.font
	fontSize = args.fontSize
	img_width = args.width
	img_height = args.height
	
	if (not inFile[-4:] == ".png"):
		print("inFile has to be a .png-file")
		sys.exit(2)
	if (not os.path.isfile(inFile)):
		print("Could not find file '%s'." % inFile)
		sys.exit(2)
	if (not os.path.isfile(textFile)):
		print("Could not find file '%s'." % textFile)
		sys.exit(2)

	# load the text 
	text_file = open(textFile)
	text = text_file.read()
	text_file.close()
	# clean the text
	text = re.sub("\s+", " ", text)
	text = re.sub("\n+", " ", text)

	# load the image
	img = Image.open(inFile)
	img = img.resize((img_width, img_height), Image.ANTIALIAS)

	# overlay the text 
	out = textOverlayInverse(img, text, font = font, fontSize = fontSize)
	# save the text
	out.save(outFile)
	print("File saved to %s" % outFile)

if __name__ == "__main__":
	main(sys.argv[1:])
