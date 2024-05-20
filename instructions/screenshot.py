from PIL import ImageGrab
import time

def capture():
    im = ImageGrab.grab()
    savetime = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
    savepath = f"/tmp/{savetime}-Screenshot.png"
    
    im.save(savepath)

capture()



