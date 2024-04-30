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
image_path = 'C:/Users/Brian/Desktop/ocr/1.png'
extracted_text = extract_text(image_path)
translated_text = translate_text(extracted_text, target_language='en')

print("Extracted Text:", extracted_text)
print("Translated Text:", translated_text)
