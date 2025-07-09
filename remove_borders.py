import os
import cv2
from border_utils import BorderDetector

def process_images(input_dir='input', output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    valid_exts = ('.png', '.jpg', '.jpeg')

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(valid_exts):
            continue

        input_path = os.path.join(input_dir, filename)
        image = cv2.imread(input_path)

        if image is None:
            continue

        detector = BorderDetector(image)
        top, bottom, left, right, _ = detector.detect()
        height, width = image.shape[:2]

        if top + bottom < height and left + right < width:
            cropped = detector.crop(top, bottom, left, right)
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, cropped)

if __name__ == '__main__':
    process_images()
