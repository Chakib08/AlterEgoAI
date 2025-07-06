import os
import time
import uuid
import base64

def save(image_path: str, image_base64: str) -> str:
    if not isinstance(image_path, str):
        raise TypeError(f"Expected image_path to be str, but got {type(image_path).__name__}")

    # Split full path into dir, base filename, and extension
    directory = os.path.dirname(image_path)
    basename = os.path.basename(image_path)
    filename, ext = os.path.splitext(basename)

    # Generate unique filename
    img_uuid = f"_{int(time.time())}_{uuid.uuid4().hex[:6]}.png"
    output_filename = filename + img_uuid
    output_path = os.path.join(directory, output_filename)

    # Decode and save
    image_bytes = base64.b64decode(image_base64)
    with open(output_path, "wb") as f:
        f.write(image_bytes)

    return output_path
