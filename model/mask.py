import cv2
import numpy as np
import os


def get_max_contour(contours):
    if len(contours) == 0:
        return
    max_c = contours[0]

    try:
        for contour in contours:
            if cv2.contourArea(contour) > cv2.contourArea(max_c):
                max_c = contour
    except:
        return max_c

    return max_c


def crop_img(gray, img, file):

    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[-1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contour = get_max_contour(
        cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
    )
    x, y, w, h = cv2.boundingRect(contour)
    padding = 3

    cropped = img[y - padding : y + h + padding, x - padding : x + w + padding]
    return cropped


def extract_brain(gray, img, buffer):
    # threshold
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[-1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contour = get_max_contour(
        cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
    )
    x, y, w, h = cv2.boundingRect(contour)
    padding = 40 + buffer
    # thresh = 255 - thresh
    sec = thresh[y - padding : y + h + padding, x - padding : x + w + padding]

    while padding > -10:
        try:

            contour_list = []
            th = img.copy()
            th = th[y - padding : y + h + padding, x - padding : x + w + padding]
            sec = thresh[y - padding : y + h + padding, x - padding : x + w + padding]
            contours = cv2.findContours(sec, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[
                -2
            ]
            # if len(contours) == 5:
            #     # padding -= 10
            #     # sec = thresh[y - padding : y + h + padding, x - padding : x + w + padding]
            #     break
            contour = get_max_contour(contours)
            x1, y1, w1, h1 = cv2.boundingRect(contour)
            # if abs(th.shape[0] - h) > 20 and abs(th.shape[1] - w) > 20:
            #     print(x, y, w, h)
            #     break

            if x1 != 0 and y1 != 0:
                while padding > -10:
                    th = img.copy()
                    th = th[
                        y - padding : y + h + padding, x - padding : x + w + padding
                    ]
                    sec = 255 - sec
                    sec = thresh[
                        y - padding : y + h + padding, x - padding : x + w + padding
                    ]
                    contours = cv2.findContours(
                        sec, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
                    )[-2]
                    contour_list.append(get_max_contour(contours))
                    padding -= 1
                contour = sorted(contour_list, key=cv2.contourArea, reverse=True)[-1]
                ret, markers = cv2.connectedComponents(sec)

                marker_area = [
                    np.sum(markers == m) for m in range(np.max(markers)) if m != 0
                ]
                cv2.drawContours(th, contour, -1, color=(0, 255, 0), thickness=1)

                largest_component = np.argmax(marker_area) + 1
                brain_mask = markers == largest_component
                brain_out = th.copy()
                brain_out[brain_mask == False] = (0, 0, 0)

                return brain_out, False

            padding -= 1

        except Exception as e:
            padding -= 1
            print(e)
            return gray, True


def rm_r_ds_store(path):
    os.system(f"find . -name '.DS_Store' -type f -delete")


def main():
    rm_r_ds_store(0)
    os.makedirs("cropped", exist_ok=True)
    files = []
    objects = []
    extracted = []
    os.chdir("brain_tumor_dataset")
    # os.chdir("archive3")

    for dir in os.listdir():
        os.makedirs(os.path.join("..", "cropped", dir), exist_ok=True)
        for file in os.listdir(dir):
            path = os.path.join(dir, file)
            if file.endswith(".jpg"):
                try:
                    img = cv2.imread(path)
                    img = cv2.resize(img, (128, 128))
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    crp_path = os.path.join("..", "cropped", dir, f"cropped_{file}")

                    cv2.imwrite(
                        crp_path,
                        crop_img(gray, img, path),
                    )
                    dim = list(cv2.imread(crp_path).shape)
                    if dim[0] < 80 or dim[1] < 80:
                        os.remove(crp_path)
                except Exception as e:
                    print(img.shape[1::-1])
                    print(e)


if __name__ == "__main__":
    main()
