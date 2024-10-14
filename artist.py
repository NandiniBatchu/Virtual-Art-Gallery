class Artist:
    def __init__(self, artistId, name,biography,birthDate,nationality,website,contactInformation):
        self.artistId = artistId
        self.name = name
        self.biography = biography
        self.birthDate = birthDate
        self.nationality = nationality
        self.website = website
        self.contactInformation = contactInformation

    #Setters

    def set_artistId(self,artistId):
        self.artistId = artistId
    def set_name(self,name):
        self.name = name
    def set_biography(self,biography):
        self.biography = biography
    def set_birthDate(self,birthDate):
        self.birthDate = birthDate
    def set_nationality(self,nationality):
        self.nationality = nationality
    def set_website(self,website):
        self.website = website
    def set_contactInformation(self,contactInformation):
        self.contactInformation = contactInformation

    #Getters

    def get_artistId(self):
        return self.artistId
    def get_name(self):
        return self.name
    def get_biography(self):
        return self.biography
    def get_birthDate(self):
        return self.birthDate
    def get_nationality(self):
        return self.nationality
    def get_website(self):
        return self.website
    def get_contactInformation(self):
        return self.contactInformation
