from model import verify

try:
    image_path1 = 'picture/5.jpg'
    image_path2 = 'picture/4.jpg'
    verify(image_path1, image_path2)
except Exception as error:
    print('Error {}'.format(error))