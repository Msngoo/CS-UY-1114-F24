class Pixel:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'({self.red}, {self.green}, {self.blue})'

if __name__ == "__main__":
    main()