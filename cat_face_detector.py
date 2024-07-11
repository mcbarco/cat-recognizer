import cv2
import os
import glob

# delete any leftover images in result-images
files = ['result-images/haar/*', 'result-images/lbp/*']
for folder in files:
    f = glob.glob(folder)
    for im in f:
        os.remove(im)        

# saves algorithm paths
algs = ["haarcascade_frontalcatface_extended.xml", "lbpcascade_frontalcatface.xml"]

# passing cat regonition algorithm to OpenCV
haar_cascade = cv2.CascadeClassifier(algs[0])

# passing alternate cat recognition algorithm to OpenCV
lbp_cascade = cv2.CascadeClassifier(algs[1])

# declares which cat image you wish to search in (change as needed)
file_name = 'cat-images\\cats-image-6.jpg'
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

cat_faces = [faces, faces2]
# for each face detected 
num = 0
for face in cat_faces:
    face_count = 0
    for x, y, w, h in face:
        face_count+=1
        # crops the image so that only one face is selected
        cropped_image = img[y : y + h, x : x + w]
        
        # determines which cat detector is being used (haar or lbp)
        rec_type = 'haar'
        if (num == 1):
            rec_type = 'lbp'

        # loads image path to the target_file_name variable
        target_file_name = 'result-images\\' + rec_type + '\\found-cat-' + str(face_count) + '.jpg'
        cv2.imwrite(
            target_file_name,
            cropped_image,
        )
    num+=1