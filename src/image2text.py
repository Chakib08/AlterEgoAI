import base64

def encode(image_path: str):
    """
    Convert an image to a Base64 text string.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        str: Base64 encoded text representing the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        encoded_text = encoded_bytes.decode('utf-8')  # Convert bytes to string
    return encoded_text

def decode(encoded_text: str, output_path: str):
    """
    Convert a Base64 text string back to an image file.

    Args:
        encoded_text (str): Base64 encoded text.
        output_path (str): Path where the output image will be saved.
    """
    image_data = base64.b64decode(encoded_text)
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)
