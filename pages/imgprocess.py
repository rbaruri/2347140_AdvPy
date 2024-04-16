import streamlit as st
from PIL import Image

st.title('Image Processing')

st.image('image1.jpg', caption='Image 1', use_column_width=True)
st.image('image2.jpg', caption='Image 2', use_column_width=True)
st.image('image3.jpg', caption='Image 3', use_column_width=True)
st.image('image4.jpg', caption='Image 4', use_column_width=True)


st.write('Choose the Image Processing Technique to be applied')
option = st.radio('', ('Image Resizing', 'Grayscale Conversion', 'Image Cropping', 'Image Rotation'))

image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')
image3 = Image.open('image3.jpg')
image4 = Image.open('image4.jpg')

if option == 'Image Resizing':
    st.write('Here are the resized images')

    
    image1_res = image1.resize((300,300))
    st.image(image1_res, caption='Resized Image', use_column_width=True)
    
    image2_res = image2.resize((300,300))
    st.image(image2_res, caption='Resized Image', use_column_width=True)
    
    image3_res = image3.resize((300,300))
    st.image(image3_res, caption='Resized Image', use_column_width=True)
    
    image4_res = image4.resize((300,300))
    st.image(image4_res, caption='Resized Image', use_column_width=True)
   
elif option == 'Grayscale Conversion':
    
    st.write('Here are the grayscale images')

    image1_gray = image1.convert('L')
    st.image(image1_gray, caption='Grayscale Image', use_column_width=True)
    
    image2_gray = image2.convert('L')
    st.image(image2_gray, caption='Grayscale Image', use_column_width=True)
    
    image3_gray = image3.convert('L')
    st.image(image3_gray, caption='Grayscale Image', use_column_width=True)
    
    image4_gray = image4.convert('L')
    st.image(image4_gray, caption='Grayscale Image', use_column_width=True)
    
    
elif option == 'Image Cropping':
    st.write('Here are the cropped images')
    
    box = (100,100,400,400)
    image1_crop = image1.crop(box)
    st.image(image1_crop)
    
    image2_crop = image2.crop(box)
    st.image(image2_crop)
    
    image3_crop = image3.crop(box)
    st.image(image3_crop)
    
    image4_crop = image4.crop(box)
    st.image(image4_crop)
        
elif option == 'Image Rotation':
    st.write('Here are the rotated images')
    
    image1_rot = image1.rotate(90)
    st.image(image1_rot)
    
    image2_rot = image2.rotate(90)
    st.image(image2_rot)
    
    image3_rot = image3.rotate(90)
    st.image(image3_rot)
    
    image4_rot = image4.rotate(90)
    st.image(image4_rot)
    
    


