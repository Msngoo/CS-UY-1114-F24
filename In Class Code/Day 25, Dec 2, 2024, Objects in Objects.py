from screenDay25 import Screen
from pixelDay25 import Pixel

def main():
    scr1 = Screen("Samsung", 75, 920000, "flat screen")
    scr2 = Screen("Apple", 16, 340000, "monitor")
    scr3 = Screen("Vizio", 55, 9345231, "curved")
    # print(scr1)
    # print(repr(scr1))

    pix1 = Pixel(255, 32, 0)
    pix2 = Pixel(255, 255, 255)
    pix3 = Pixel(0, 0, 0)
    print(pix1)

    scr1.add_pixel(pix1)
    scr1.add_pixel(pix2)
    scr1.add_pixel(pix3)
    print(scr1) #Output looks the same bc __str__() doesn't have mention of pixel

if __name__ == "__main__":
    main()


#Seasame St Analyzer
