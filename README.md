
# OCR Text Translator 🐍

the script will translate any given image by ocr getting text from the image and translate the texts
view https://tesseract-ocr.github.io for more info about languaes support.
here is sample Demo.☕

![Screenshot 2024-04-30 190811](https://github.com/brianlangay4/Image-transalate-OCR-/assets/67788456/2d922feb-c7d9-4476-837e-b0ff00591643)


```

This Python script utilizes Optical Character Recognition (OCR) to extract text from images and then translates the extracted text to a desired language using the Google Translate API.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- pytesseract: Python wrapper for Google's Tesseract-OCR Engine. You can install it using pip:
  ```
  pip install pytesseract
  ```

- Pillow (PIL Fork): Python Imaging Library to work with images. You can install it using pip:
  ```
  pip install Pillow
  ```

- deep_translator: Python library for translating text using various translation services. You can install it using pip:
  ```
  pip install deep_translator
  ```

- Tesseract-OCR: OCR engine for text recognition. You can download and install it from the following link: https://github.com/tesseract-ocr/tesseract

## Usage

1. Clone the repository or download the script.

2. Ensure the required libraries are installed (see Prerequisites).

3. Provide the path to the image file you want to extract text from by modifying the `image_path` variable in the script.

4. Run the script. It will extract text from the provided image using OCR and then translate the extracted text to the desired language.

## Example

```python
import pytesseract
from PIL import Image
from deep_translator import GoogleTranslator

# Step 1: Extract text from image using OCR (Tesseract)
def extract_text(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image)
    
    return text

# Step 2: Translate extracted text to desired language
def translate_text(text, target_language='en'):
    # Translate the text using Deep Translator
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
    
    return translated_text

# Step 3: Example usage
image_path = 'path_to_your_image.png'
extracted_text = extract_text(image_path)
translated_text = translate_text(extracted_text, target_language='en')

print("Extracted Text:", extracted_text)
print("Translated Text:", translated_text)
```

Replace `'path_to_your_image.png'` with the actual path to your image file.

## Acknowledgments

- This script utilizes pytesseract for OCR and deep_translator for translation.

- Special thanks to the developers of Tesseract-OCR and Google Translate API.

## License
fell free to use its free. ☕
```

Make sure to replace `'path_to_your_image.png'` with the actual path to your image file before running the script.
```
## Debuging 💥

incase of unsual smooth running 
1.install tesseract-ocr on your machine

link to official tesseract-ocr https://tesseract-ocr.github.io/tessdoc/Downloads.html

2.open cmd and step to tesseract-ocr directory

3.excute python/python3 /path to pythonScript.py

4.make sure the image path is in full path directory formart because your accessing the python script outside (full path)









