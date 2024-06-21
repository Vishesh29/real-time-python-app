from PIL import Image, ImageFilter
import sys

def process_image(input_image_path, output_image_path):
    """
    Processes the input image by applying a smooth filter and saves the result to the output path.

    Parameters:
    input_image_path (str): Path to the input image file.
    output_image_path (str): Path to save the processed image file.
    """
    try:
        # Open the input image
        img = Image.open(input_image_path)

        # Print image details
        print(f"Format: {img.format}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")

        # Apply a smooth filter to the image
        smooth_img = img.filter(ImageFilter.SMOOTH)

        # Save the processed image
        smooth_img.save(output_image_path, 'PNG')
        print(f"Processed image saved as: {output_image_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python smooth_image.py <input_image> <output_image>")
    else:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]
        process_image(input_image_path, output_image_path)
