class User:
    def __init__(self, userId,userName,password,email,firstName,lastName,dateOfBirth,profilePicture,favouriteArtworks):
        self.userId = userId
        self.userName = userName
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.profilePicture = profilePicture
        self.favouriteArtworks = favouriteArtworks

    #Setters

    def set_userId(self,userId):
        self.userId = userId
    def set_username(self,userName):
        self.userName = userName
    def set_password(self,password):
        self.password = password
    def set_email(self,email):
        self.email = email
    def set_firstName(self,firstName):
        self.firstName = firstName
    def set_lastName(self,lastName):
        self.lastName = lastName
    def set_dateOfBirth(self,dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def set_profilePicture(self,profilePicture):
        self.profilePicture = profilePicture
    def set_favouriteArtworks(self,favouriteArtworks):
        self.favouriteArtworks = favouriteArtworks

    #Getters

    def get_userId(self):
        return self.userId
    def get_username(self):
        return self.userName
    def get_password(self):
        return self.password
    def get_email(self):
        return self.email
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_dateOfBirth(self):
        return self.dateOfBirth
    def get_profilePicture(self):
        return self.profilePicture
    def get_favouriteArtworks(self):
        return self.favouriteArtworks
