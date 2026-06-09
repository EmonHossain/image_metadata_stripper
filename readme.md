# Image Metadata Stripper

A lightweight Python utility designed to protect your digital privacy by stripping EXIF data, GPS tags, and location tracking from your photos before you share them online. 

It features a simple, native graphical file picker that allows you to select single or multiple images simultaneously, rendering them safe for public or private distribution.

---

## 🚀 Features

* **Deep Privacy Cleaning:** Instead of just editing the tags, the script copies only the raw pixel data to a completely fresh image file, leaving all hidden EXIF data, camera models, and GPS locations behind.
* **Batch Processing:** Select and process multiple images at the same time using your operating system's native file dialog.
* **Format Preservation:** Keeps your original formats (JPEG, PNG, WebP) intact whenever possible.
* **Modern iPhone Support:** Native handling for iOS HEIC/HEIF files, with an automated fallback mechanism.
* **Non-Destructive:** Your original images remain completely untouched. Cleaned versions are securely saved to an isolated `clean_images/` directory.

---

## 🛠️ Requirements & Installation (Make sure you have python installed first)

The script relies on `Pillow` for image manipulation and `tkinter` (which comes pre-installed with most Python distributions) for the file selection interface.

### 1. Clone or Download the Script
Save the code into a file named `Image_Metadata_Stripper.py`.

### 2. Install Dependencies
Open your terminal or command prompt and run the following command to install the required image processing libraries:

```bash
pip install Pillow pillow-heif
```

### 2. How to run
Open your terminal or command prompt and run the following command to run the pyhton script locally

```bash
python Image_Metadata_Stripper.py
```

that's it! you are good to go...!