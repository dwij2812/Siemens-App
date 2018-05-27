import PIL.Image
import PIL
class Resize:
    def rsize(self,image):
        try:
            im = PIL.Image.open(image)
        except:
            im =image
        x,y=im.size
        while x<500 or y<500:
            x*=2
            y*=2
        im=im.resize((int(x),int(y)), PIL.Image.BICUBIC)
        return im #returning resized image object
