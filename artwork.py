class Artwork:
    def __init__(self,artworkId,title,description,creationDate,medium,imageURL):
        self.artworkId = artworkId
        self.title = title
        self.description = description
        self.creationDate = creationDate
        self.medium = medium
        self.imageURL = imageURL

    #Setters

    def set_artworkId(self,artworkId):
        self.artworkId = artworkId
    def set_title(self,title):
        self.title = title
    def set_description(self,description):
        self.description = description
    def set_creationDate(self,creationDate):
        self.creationDate = creationDate
    def set_medium(self,medium):
        self.medium = medium
    def set_imageURL(self,imageURL):
        self.imageURL = imageURL

    #Getters

    def get_artworkId(self):
        return self.artworkId
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_creationDate(self):
        return self.creationDate
    def get_medium(self):
        return self.medium
    def get_imageURL(self):
        return self.imageURL
    