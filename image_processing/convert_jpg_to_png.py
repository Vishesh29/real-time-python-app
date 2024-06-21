from PIL import Image
import sys
import os

def convert_images(src_dir, dest_dir):
    """
    Converts images from JPG to PNG format.

    Parameters:
    src_dir (str): Path to the source directory containing JPG images.
    dest_dir (str): Path to the destination directory where PNG images will be saved.
    """
    try:
        # Create the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)

        # Loop through all files in the source directory
        for filename in os.listdir(src_dir):
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                # Open the image file
                img_path = os.path.join(src_dir, filename)
                img = Image.open(img_path)

                # Create the output filename with the same base name and PNG extension
                output_filename = os.path.splitext(filename)[0] + ".png"
                output_path = os.path.join(dest_dir, output_filename)

                # Save the image as PNG
                img.save(output_path, "PNG")

                print(f"Converted {filename} to {output_filename}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the directory paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_jpg_to_png.py <src_dir> <dest_dir>")
    else:
        src_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        convert_images(src_dir, dest_dir)