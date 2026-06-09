import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Try to import pillow_heif for HEIC/HEIF support (common for iPhone images)
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF_SUPPORT = True
except ImportError:
    HEIF_SUPPORT = False

def remove_metadata(input_path, output_path):
    """
    Removes metadata from an image while preserving its visual quality.
    Supports JPG, PNG, HEIC (iPhone), WEBP, and other common formats.
    """
    try:
        with Image.open(input_path) as img:
            actual_format = img.format
            
            # Create a new image object containing only pixel data
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(list(img.getdata()))
            
            if actual_format in ['JPEG', 'JPG']:
                try:
                    clean_img.save(output_path, format=actual_format, quality='keep', subsampling='keep')
                except ValueError:
                    clean_img.save(output_path, format='JPEG', quality=95)
            elif actual_format == 'PNG':
                clean_img.save(output_path, format='PNG', optimize=True)
            elif actual_format in ['HEIF', 'HEIC']:
                # Save iPhone HEIC files safely. Fallback to JPEG if direct HEIF write fails
                try:
                    clean_img.save(output_path, format=actual_format, quality=95)
                except Exception:
                    base_path, _ = os.path.splitext(output_path)
                    output_path = base_path + ".jpg"
                    clean_img.save(output_path, format='JPEG', quality=95)
            elif actual_format == 'WEBP':
                clean_img.save(output_path, format='WEBP', quality=95)
            else:
                # Catch-all fallback for other formats: convert safely to JPEG
                base_path, _ = os.path.splitext(output_path)
                output_path = base_path + ".jpg"
                clean_img.save(output_path, format='JPEG', quality=95)
                
        print(f"Successfully stripped metadata: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def get_user_selection():
    """
    Opens a GUI dialog immediately allowing the user to select one or multiple files.
    """
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    print("Opening file selection window... Please look at your screen/taskbar.")
    
    # Expanded file types to include iPhone HEIC/HEIF and all standard formats
    file_types = [
        ("All Supported Images", "*.jpg *.jpeg *.png *.heic *.heif *.webp *.tiff *.bmp"),
        ("JPEG Images", "*.jpg *.jpeg"),
        ("PNG Images", "*.png"),
        ("iPhone Images (HEIC/HEIF)", "*.heic *.heif"),
        ("WebP Images", "*.webp"),
        ("All Files", "*.*")
    ]
    
    file_paths = filedialog.askopenfilenames(
        title="Select Image File(s) to Clean",
        filetypes=file_types
    )
    
    return list(file_paths) if file_paths else None

def process_images(file_list, output_dir="clean_images"):
    if not file_list:
        print("No files were selected. Exiting.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if not HEIF_SUPPORT:
        print("\n[WARNING]: 'pillow-heif' is not installed. iPhone (.heic/.heif) files may fail to load.")
        print("To fix this, run: pip install pillow-heif\n")
        
    print(f"Processing {len(file_list)} selected file(s)...")
    
    for source_path in file_list:
        filename = os.path.basename(source_path)
        remove_metadata(source_path, os.path.join(output_dir, filename))
        
    print(f"\nAll done! Cleaned images saved to the folder: '{os.path.abspath(output_dir)}'")

if __name__ == "__main__":
    selected_files = get_user_selection()
    process_images(selected_files, output_dir="clean_images")