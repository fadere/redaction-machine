🕵️‍♂️ The Redaction Machine
An automated, OCR-powered tool to scan images for sensitive keywords and physically overwrite them with solid black rectangles.

📌 Overview
This script is designed for use in Google Colab or Jupyter Notebooks. It allows users to upload multiple images, specify a list of "naughty words," and receive processed versions where those words are permanently masked.

Key Features
Batch Processing: Upload multiple images at once.

Permanent Masking: Draws solid black rectangles over text (not just a highlight).

OCR-Driven: Automatically locates text coordinates using the Tesseract engine.

Auto-Download: Automatically triggers a browser download for each redacted file.

🚀 How to Use
Open in Colab: Copy the script into a new cell in Google Colab.

Run the Setup: The first block of the script will automatically install the tesseract-ocr engine and the pytesseract library.

Upload Images: A "Choose Files" button will appear. Select all the images you wish to process.

Enter Keywords: When prompted, type the words you want to hide (e.g., Confidential, Password, $5,000).

Note: The script is case-insensitive.

Review & Download: The script will display a preview of each redacted image and automatically trigger a download of the new file (prefixed with redacted_).

🛠 Technical Requirements
The script relies on the following stack:

Language: Python 3.x

OCR Engine: Tesseract OCR

Image Processing: OpenCV (cv2)

Visualization: Matplotlib

Python Dependencies
Bash
pip install pytesseract opencv-python-headless matplotlib
⚠️ Important Limitations
[!WARNING]

OCR Accuracy: While Tesseract is powerful, it is not 100% perfect. Highly stylized fonts, low-resolution images, or handwriting may result in missed words. Always manually verify highly sensitive documents.

Whole Words Only: Currently, the script looks for exact matches. Redacting "Tax" may not automatically redact "Taxes."

Standard Text: The script works best on horizontal, machine-printed text.

📄 License
This project is open-source. Feel free to modify the masking logic or the coordinate padding to suit your specific security needs.
