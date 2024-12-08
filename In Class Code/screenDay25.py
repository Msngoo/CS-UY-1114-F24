class Screen:
    def __init__(self, manu, size, num_pixel, tech_type):
        self.manufacturer = manu
        self.dimension = size
        self.num_pixels = num_pixel
        self.type = tech_type
        self.pixel_list = []

    def add_pixel(self, pix):
        self.pixel_list.append(pix)
    
    def __str__(self):
        return f"{self.manufacturer}: {self.type} - {self.num_pixels} {self.dimension}"
    
    def __repr__(self):
        return f'Screen("{self.manufacturer}", {self.dimension}, {self.num_pixels}, "{self.type}")'

if __name__ == "__main__":
    main()