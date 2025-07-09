# 📸 Image Border Detection and Removal

Automatically detect and remove uniform borders (e.g., white/black frames) from images in a batch. This project includes:

- Border size detection with a CSV report
- Automated cropping and saving of cleaned images

---

## 🗂️ Project Structure

```
your_project/
├── input/    
│   └── example_input.jpg
├── output/
│   └── example_output.jpg
├── border_utils.py
├── detect_borders.py
├── remove_borders.py
├── border_report.csv
└── README.md
```

---

## 🖼️ Example Input vs Output

### Input Image (with border)
![Input](https://github.com/Darkside099/CleanFrame/blob/396893f2217fa05f165ca1a06e3a1d00ab2b7f26/input/IMG_1.jpg)

### Output Image (cropped)
![Output](https://github.com/Darkside099/CleanFrame/blob/7b8c2e09b513407a261593de8212253a6b281dc5/output/IMG_1.jpg).

---

## 📄 Sample CSV Output

| Filename    | Top (px) | Bottom (px) | Left (px) | Right (px) | Border Sides             |
| ----------- | -------- | ----------- | --------- | ---------- | ------------------------ |
| IMG\_1.jpg  | 237      | 237         | 194       | 194        | top, bottom, left, right |
| IMG\_10.jpg | 49       | 48          | 36        | 37         | top, bottom, left, right |
| IMG\_2.jpg  | 39       | 38          | 29        | 63         | top, bottom, left, right |
| IMG\_3.jpg  | 456      | 650         | 402       | 555        | top, bottom, left, right |
| IMG\_4.jpg  | 59       | 2165        | 936       | 772        | top, bottom, left, right |
| IMG\_5.jpg  | 15       | 1271        | 403       | 556        | top, bottom, left, right |
| IMG\_6.jpg  | 36       | 3248        | 1003      | 1037       | top, bottom, left, right |
| IMG\_7.jpg  | 220      | 118         | 225       | 264        | top, bottom, left, right |
| IMG\_8.jpg  | 65       | 64          | 48        | 49         | top, bottom, left, right |
| IMG\_9.jpg  | 185      | 201         | 185       | 400        | top, bottom, left, right |

---

## 🚀 How to Use

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. 🖼️ Add Your Images

Place all your input images in the `input/` folder.

Supported formats: `.jpg`, `.jpeg`, `.png`

---

## ✅ Task 1: Detect Borders

Generate a CSV report with border sizes and positions.

```bash
python detect_borders.py
```

Output:  
- `border_report.csv` (lists top/bottom/left/right border size and detected sides for each image)

---

## ✂️ Task 2: Remove Borders

Crop the borders and save clean images into the `output/` folder.

```bash
python remove_borders.py
```

Output:  
- Cropped images saved with the same filenames into `output/`

---

## ⚙️ Customization

You can tweak threshold values or add support for non-white borders in `border_utils.py` if needed.

---

## 🧠 Technologies Used

- Python 3
- OpenCV (cv2)
- NumPy
- Pandas

---

## 📌 Example Use Case

Useful for:

- Cleaning scanned documents or datasets
- Preprocessing image data for machine learning
- Removing framing effects in screenshots or photos

---
