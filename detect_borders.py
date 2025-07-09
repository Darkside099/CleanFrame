import os
import pandas as pd
import cv2
from border_utils import BorderDetector

input_dir = "input"
report_path = "border_report.csv"
results = []

for filename in os.listdir(input_dir):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    path = os.path.join(input_dir, filename)
    image = cv2.imread(path)

    if image is None:
        continue

    detector = BorderDetector(image)
    top, bottom, left, right, sides = detector.detect()

    results.append(
        {
            "filename": filename,
            "top_border_px": top,
            "bottom_border_px": bottom,
            "left_border_px": left,
            "right_border_px": right,
            "border_sides": ", ".join(sides),
        }
    )

pd.DataFrame(results).to_csv(report_path, index=False)
