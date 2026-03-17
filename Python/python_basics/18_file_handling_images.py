"""
18_file_handling_images.py

Manipulating Image Files:
- Python Standard Library works well for file I/O operations (copying, moving).
- For actual image manipulation (resizing, filters), the 'Pillow' library is standard.

NOTE: This script requires Pillow to be installed.
Command: pip install Pillow
"""

try:
    from PIL import Image, ImageFilter
    pillow_installed = True
except ImportError:
    pillow_installed = False
    print("Pillow library not found. Please install using: pip install Pillow")

# 1. Basic Binary Copy (Works without extra libraries)
# Useful for moving/copying image files without changing content
def copy_image(source_path, dest_path):
    try:
        with open(source_path, 'rb') as source_file: # 'rb' = Read Binary
            with open(dest_path, 'wb') as dest_file: # 'wb' = Write Binary
                dest_file.write(source_file.read())
        print(f"Image copied from {source_path} to {dest_path}")
    except FileNotFoundError:
        print(f"Source file {source_path} not found for copy demo.")

# 2. Image Manipulation with Pillow
def manipulate_image():
    if not pillow_installed:
        return

    # Create a simple new image from scratch for demonstration
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save('test_image.png')
    print("\nCreated 'test_image.png' (100x100 Red Square)")

    # Open existing image
    try:
        with Image.open('test_image.png') as im:
            print(f"Original Size: {im.size}")
            
            # Resize
            im_resized = im.resize((50, 50))
            im_resized.save('test_image_small.png')
            print("Saved resized image as 'test_image_small.png'")

            # Convert to Grayscale
            im_gray = im.convert("L")
            im_gray.save('test_image_gray.png')
            print("Saved grayscale image as 'test_image_gray.png'")
            
            # Apply Blur Filter
            im_blur = im.filter(ImageFilter.BLUR)
            im_blur.save('test_image_blur.png')
            print("Saved blurred image as 'test_image_blur.png'")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    # Create dummy image for the copy test
    with open("dummy_logo.jpg", "wb") as f:
        f.write(b'\xFF\xD8\xFF\xE0' + b'\x00' * 10) # Fake JPEG header
    
    copy_image("dummy_logo.jpg", "copy_logo.jpg")
    
    if pillow_installed:
        manipulate_image()
    else:
        print("\nSkipping Pillow examples since usage is constrained without the library.")
