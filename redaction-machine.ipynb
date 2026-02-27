# --- STEP 1: INSTALL & SETUP ---
!apt-get update -qq
!apt-get install -y tesseract-ocr -qq
!pip install pytesseract opencv-python-headless -q

import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt
from google.colab import files
import os

def run_multi_redaction_machine():
    # 1. Prompt for multiple File Uploads
    print("--- 🚀 STEP 1: UPLOAD IMAGES (Select one or many) ---")
    uploaded = files.upload()
    
    if not uploaded:
        print("No files uploaded. Exiting.")
        return

    # 2. Get Redaction Terms (Applied to ALL images)
    print("\n--- ✍️ STEP 2: DEFINE TARGETS ---")
    terms_input = input("Enter words to redact (separated by commas): ")
    redact_list = [term.strip().lower() for term in terms_input.split(",")]

    # 3. Loop through EVERY uploaded file
    for file_name in uploaded.keys():
        print(f"\n--- ⚙️ PROCESSING: {file_name} ---")
        
        img = cv2.imread(file_name)
        if img is None:
            print(f"Skipping {file_name}: Not a valid image.")
            continue
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        d = pytesseract.image_to_data(gray, output_type=Output.DICT)

        redaction_count = 0
        for i in range(len(d['text'])):
            word = d['text'][i].strip().lower()
            if word and word in redact_list:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                # Draw solid black rectangle
                cv2.rectangle(img, (x-2, y-2), (x + w + 2, y + h + 2), (0, 0, 0), -1)
                redaction_count += 1

        # 4. Save and Show Results for this specific file
        output_name = f"redacted_{file_name}"
        cv2.imwrite(output_name, img)
        
        print(f"Redacted {redaction_count} instances in {file_name}.")
        
        # Display preview
        plt.figure(figsize=(8,8))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(f"Result: {output_name}")
        plt.axis('off')
        plt.show()

        # 5. Download the specific result
        files.download(output_name)

    print("\n--- ✅ ALL FILES PROCESSED ---")

# Run the machine
run_multi_redaction_machine()
