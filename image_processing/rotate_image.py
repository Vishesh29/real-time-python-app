from PIL import Image
import sys

def process_image(input_image_path, output_image_path):
    """
    Processes the input image by rotating it 90 degrees counter-clockwise and saves the result to the output path.

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

        # Rotate the image to 90 degrees counter-clockwise
        rotate_img = img.rotate(90)

        # Save the processed image
        rotate_img.save(output_image_path, 'PNG')
        print(f"Processed image saved as: {output_image_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_image> <output_image>")
    else:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]
        process_image(input_image_path, output_image_path)
