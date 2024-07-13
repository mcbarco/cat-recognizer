# :cat: Cat Recognizer

This project is a Python program that uses OpenCV (Open Source Computer Vision) to detect cats in images. 

## About The Project

OpenCV is a library used mainly for computer vision. While researching facial recognition software, and how to build it, I discovered something even more fun! Cat recognition software. For a cat lover, this was an amazing discovery.

I began by following a facial recognition tutorial to understand the basics of how OpenCV's resources work. Then, I modified it to work with Haar Cascades' and LBP Cascades' cat recognition tool. 

## Results

The following image is a cat image that I used to test the program. 

<img src="cat-images\cats-image-6.jpg" alt="cats-image-su.and.ran" width="500">

The following table shows what each of the cat recognition tools generated from the cat image.

| Haar Cascades                     | LBP Cascades                      |
|-----------------------------------|-----------------------------------|
| ![found-cat-1-haar](result-images\haar\found-cat-1.jpg)| ![found-cat-1-lbp](result-images\lbp\found-cat-1.jpg)|
|                | ![found-cat-2-lbp](result-images\lbp\found-cat-2.jpg)|

## Testing Process

I tested this with a variety of different cat photos (taken by myself, [@su.and.ran](https://www.instagram.com/su.and.ran/) and [@nabesentochiro](https://www.instagram.com/nabesentochiro/?hl=en) on Instagram). Some of the photos had one cat, while others had multiple. 

Using Haar Cascades' cat recognition tool, I got varying results. While it always recognized the cat in the photo, it also falsely recognized other non-cat portions of the photo as well. 

After more research, I found an alternative tool: LBP Cascades. I implemented the same program with LBP Cascades. The following tables provide information on how these tools performed with the six sample cat photos. 

| Image                 | True Number of Cats | Haar Recognized | LBP Recognized |
|-----------------------|---------------------|-----------------|----------------|
| cat-image-1           | 1                   | 3               | 1              |
| cat-image-2           | 1                   | 7               | 2              |
| cat-image-3           | 1                   | 7               | 17             |
| cat-image-4           | 1                   | 1               | 0              |
| cat-image-5           | 3                   | 3               | 3              |
| cat-image-6           | 2                   | 1               | 2              |

The results are fairly unclear, likely due to the varied quality of images (see cat-image-3 and cat-image-4). 

But in the main experimentation phase, while using Haar Cascade's cat regnition tool, I was often disappointed by it not recognizing multiple cats in certain images. LBP's tool certainly helped with that, but also had it's own fallbacks. 

## Reflection

Overall, I really enjoyed experimenting with this software. I love cats, and taking photos of cats. So it was great to see that my hobby could be combined with my area of study.