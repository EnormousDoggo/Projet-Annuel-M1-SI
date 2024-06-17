from io import BytesIO
from PIL import ImageGrab
import time

def capture():
    image = ImageGrab.grab()
    imageIO = BytesIO()
    image.save(imageIO, format='PNG')
    imageIO.seek(0)  # Rewind the file pointer to the beginning
    saveTime = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
    savePath = f"{saveTime}-Screenshot.png"
    files = {'file': (savePath, imageIO, 'image/png')}
    return files
