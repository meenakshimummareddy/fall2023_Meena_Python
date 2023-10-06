from PIL import Image
import pytesseract

# Load an image
image = Image.open("image.jpg")

# Perform OCR to extract text
text = pytesseract.image_to_string(image)

# Print extracted text
print(text)
