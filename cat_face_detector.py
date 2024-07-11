import cv2
import os
import glob

# delete any leftover images in result-images
files = glob.glob('result-images/haar/*')
for f in files:
    os.remove(f)

files = glob.glob('result-images/lbp/*')
for f in files:
    os.remove(f)

# cat recognizer (lbp - local binary patterns)
rec = 'lbpcascade_frontalcatface.xml'

# loads haar case algorithm for cat face recognition
alg = "haarcascade_frontalcatface_extended.xml"
# passing cat regonition algorithm to OpenCV
haar_cascade = cv2.CascadeClassifier(alg)

# loads lbp case algorithm for cat face recognition
alg2 = "lbpcascade_frontalcatface.xml"
# passing alternate cat recognition algorithm to OpenCV
lbp_cascade = cv2.CascadeClassifier(alg2)

file_name = 'cat-images\\cat-image-1.jpg'
img = cv2.imread(file_name, 0)
# gray version of image (makes it easier to process image)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# detects cat faces using haar algorithm
faces = haar_cascade.detectMultiScale(
    gray_img, scaleFactor=1.15, minNeighbors=1, minSize=(80,80)
)

# detects cat faces using lbp algorithm
faces2 = lbp_cascade.detectMultiScale(
    gray_img, scaleFactor=1.15, minNeighbors=1, minSize=(80,80)
)

# for each face detected (using haar algorithm)
face_count = 0
for x, y, w, h in faces:
    face_count+=1
    # crops the image so that only one face is selected
    cropped_image = img[y : y + h, x : x + w]
    # loads image path to the target_file_name variable
    target_file_name = 'result-images\\haar\\found-cat-' + str(face_count) + '.jpg'
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )

# for each face detected (using lbp algorithm)
face_count2 = 0
for x, y, w, h in faces2:
    face_count2+=1
    # crops the image so that only one face is selected
    cropped_image = img[y : y + h, x : x + w]
    # loads image path to the target_file_name variable
    target_file_name = 'result-images\\lbp\\found-cat-' + str(face_count2) + '.jpg'
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )        