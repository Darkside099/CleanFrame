import cv2
import numpy as np


class BorderDetector:
    def __init__(self, image):
        self.image = image
        self.h, self.w = image.shape[:2]

    def _edge_similarity(self, line, ref, threshold=5):
        diff = np.abs(line.astype(np.int16) - ref.astype(np.int16))
        return np.mean(diff) < threshold

    def _border_size(self, axis):
        arr = self.image if axis == 0 else self.image.transpose(1, 0, 2)
        ref = arr[0]
        size = 0
        for line in arr:
            if self._edge_similarity(line, ref):
                size += 1
            else:
                break
        return size

    def _reverse_border_size(self, axis):
        arr = self.image if axis == 0 else self.image.transpose(1, 0, 2)
        ref = arr[-1]
        size = 0
        for line in reversed(arr):
            if self._edge_similarity(line, ref):
                size += 1
            else:
                break
        return size

    def detect(self):
        top = self._border_size(0)
        bottom = self._reverse_border_size(0)
        left = self._border_size(1)
        right = self._reverse_border_size(1)
        sides = [
            s
            for s, v in zip(
                ["top", "bottom", "left", "right"], [top, bottom, left, right]
            )
            if v
        ]
        return top, bottom, left, right, sides

    def crop(self, top, bottom, left, right):
        return self.image[top : self.h - bottom, left : self.w - right]
