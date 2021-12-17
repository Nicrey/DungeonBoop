


class Project:

    def __init__(self, name):
        self.name = name
        self.drawings = []
        from src.Util.file_manager import FILES
        self.drawings.append(Drawing('base', FILES.load_project(name=name)))



    def get_pixels(self):
        if self.drawings:
            return self.drawings[0].pixels

        return None


class Drawing:

    def __init__(self, name, pixels):
        self.name = name
        self.pixels = pixels
