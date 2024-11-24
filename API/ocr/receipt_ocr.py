import pytesseract
import cv2
import numpy as np

from ocr_types import Image

def segment_receipt_fragment(receipt_img: Image) -> list[Image]:
    """
    Segment part of a receipt image into images with one item each.
    
    Args:
        receipt_img (Image): An image of a section of a receipt (either Products section or Prices section)
    
    Returns:
        list[Image]: List of images of individual items found in the section
    """
    gray = cv2.cvtColor(receipt_img, cv2.COLOR_BGR2GRAY)

    # preprocessing
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    div = np.float32(gray)/np.float32(close)
    res = np.uint8(cv2.normalize(div, div, 0, 255, cv2.NORM_MINMAX))
    img_thr = cv2.threshold(res, 128, 255, cv2.THRESH_BINARY_INV)[1]
    
    # count white pixels to find spaces between rows
    sum_x = np.count_nonzero(img_thr, axis=1)
    thr_x = 0.05 * receipt_img.shape[1]
    dips = np.where(sum_x < thr_x)[0]

    mean_dip_height = np.mean([dips[i+1] - dips[i] for i in np.arange(dips.shape[0] - 1)])
    segments_list = []

    for i in np.arange(dips.shape[0] - 1):
        # skip if very short segment (noise)
        if dips[i+1] - dips[i] < mean_dip_height:
            continue
        
        border_y1 = dips[i]-3 if dips[i]-3 > 0 else dips[i]-1 
        border_y2 = dips[i+1]+2 if dips[i+1]+2 < receipt_img.shape[0] else dips[i+1]-1 

        segment = receipt_img[border_y1:border_y2, :]
        segment = cv2.resize(segment, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

        segments_list.append(segment)

    return segments_list