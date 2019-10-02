
class Image:
    """A User Class For Storing User Information"""

    def __init__(self, image_name, image):
        self.image_name = image_name
        self.image = image

    def __repr__(self):
        return "Image('{}', '{}')".format(self.image_name, self.image)