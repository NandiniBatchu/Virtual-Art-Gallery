from typing import List

from dao.IvirtualArtGallery import IVirtualArtGallery
from entity.artwork import Artwork
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException
from util.DBConnection import DBConnection
from tabulate import tabulate


class VirtualArtGalleryImpl(IVirtualArtGallery):
    connection=None
    def __init__(self):
        self.connection=DBConnection.getConnection()

    def get_next_artworkID(self):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT Max(ArtworkID) FROM Artwork")
            max_id = cursor.fetchone()[0]
            return (max_id + 1) if max_id is not None else 1
        except Exception as e:
            print(e)
            return 1
        finally:
            cursor.close()

    def addArtwork(self, artwork):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Artwork (ArtworkID,Title,Description,CreationDate,Medium,ImageURL) VALUES (?,?,?,?,?,?)"
            cursor.execute(query,(self.get_next_artworkID(),artwork.get_title(),artwork.get_description(),artwork.get_creationDate(),artwork.get_medium(),artwork.get_imageURL()))
            self.connection.commit()
            print("------Artwork added------")
            return True
        except Exception as e:
            print("------Error in adding Artwork------",e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateArtwork(self, artwork,artworkId):
        cursor = self.connection.cursor()
        try:
           
            query='UPDATE Artwork SET Title=?, Description=?, CreationDate=?, Medium=? , ImageURL=? WHERE ArtworkID=?'
            cursor.execute(query,(artwork.get_title(),artwork.get_description(),artwork.get_creationDate(), artwork.get_medium(), artwork.get_imageURL(),artwork.get_artworkId()))
            self.connection.commit()
            print("------Artwork updated------")
            return True
     
        
        except Exception as e:
            print("------Error in updating Artwork------",e)
            return False
        finally:
            cursor.close()

    def removeArtwork(self, artworkId):
        cursor = self.connection.cursor()
        try:
            query = "SELECT Count(*) FROM Artwork WHERE ArtworkID=?"
            cursor.execute(query,(artworkId,))
            count = cursor.fetchone()[0]
            if count == 0:
                raise ArtWorkNotFoundException(artworkId)
            
            # Remove any references in User_Favorite_Artwork table
            delete_favorites_query = "DELETE FROM User_Favorite_Artwork WHERE ArtworkID=?"
            cursor.execute(delete_favorites_query, (artworkId,))

            # Remove any references in Artwork_Gallery table
            delete_gallery_query = "DELETE FROM Artwork_Gallery WHERE ArtworkID=?"
            cursor.execute(delete_gallery_query, (artworkId,))

       
            query='DELETE FROM Artwork WHERE ArtworkID=?'
            cursor.execute(query,(artworkId,))
            self.connection.commit()
            print("------Artwork removed------")
            return True
        
        
        except ArtWorkNotFoundException as e:
            print(e)  
            return False 
     
        except Exception as e:
            print("------Error in removing Artwork------",e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def getArtworkById(self, artworkId: int) -> Artwork:
        try:
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Artwork WHERE ArtworkID=?'
            cursor.execute(query, (artworkId,))
            artwork = cursor.fetchone()
            if artwork is None: 
                raise ArtWorkNotFoundException(artworkId)
            else:
                artwork_details = [
                    ['ArtworkID', artwork[0]],
                    ['Title', artwork[1]],
                    ['Description', artwork[2]],
                    ['CreationDate', artwork[3]],
                    ['Medium', artwork[4]],
                    ['ImageURL', artwork[5]],
                ]
                print("Artwork details")
                print(tabulate(artwork_details, tablefmt="grid"))
                return artwork
        except ArtWorkNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error in getting the details:",e)
        finally:
            cursor.close()


    def searchArtworks(self, search_object) -> None:
        cursor = self.connection.cursor()
        try:
            query = 'SELECT * FROM Artwork WHERE Title LIKE ? OR Medium LIKE ? OR Description LIKE ?'
            cursor.execute(query, (f'%{search_object}%', f'%{search_object}%', f'%{search_object}%'))
            artwork_data = cursor.fetchall()
            if artwork_data:
                for artwork in artwork_data:
                    artwork_details = [
                        ['Artwork ID', artwork[0]],  # Assuming ArtworkID is the first column
                        ['Title', artwork[1]],       # Title is the second column
                        ['Description', artwork[2]], # Description is the third column
                        ['CreationDate', artwork[3]], # CreationDate is the fourth column
                        ['Medium', artwork[4]],      # Medium is the fifth column
                        ['ImageURL', artwork[5]]     # ImageURL is the sixth column
                    ]
                    print(tabulate(artwork_details, tablefmt="grid"))
            else:
                print("No artwork found matching the search term")
        except Exception as e:
            print("Error in searching artworks:",e)
            self.connection.rollback()
        finally:
            cursor.close()

    def addArtworkToFavorite(self, userId, artworkId) -> bool:
        cursor = self.connection.cursor()
        try:
            
            query = "SELECT * FROM Artwork WHERE ArtworkID=?"
            cursor.execute(query, (artworkId,))
            if cursor.fetchone() is None:
                raise ArtWorkNotFoundException(artworkId)

            query = 'INSERT INTO User_Favorite_Artwork(UserID,ArtworkID) VALUES (?,?)'
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            print("Added to favorites")
            return True
        
        
        except ArtWorkNotFoundException as e:
            print(e)
            return False
        
        finally:
            cursor.close()

    def removeArtworkFromFavorite(self, userId, artworkId) -> bool:
        cursor = self.connection.cursor()
        try:
            
            query = "SELECT * FROM Artwork WHERE ArtworkID=?"
            cursor.execute(query, (artworkId,))
            if cursor.fetchone() is None:
                raise ArtWorkNotFoundException(artworkId)

            query = "DELETE FROM User_Favorite_Artwork WHERE UserID=? AND ArtworkID=?"
            cursor.execute(query, (userId, artworkId))
            self.connection.commit()
            print("Removed from favorites")
            return True
        
       
        except ArtWorkNotFoundException as e:
            print(e)
            return False

        finally:
            cursor.close()

    def getUserFavoriteArtworks(self, userId):
        cursor = self.connection.cursor()
        try:
            query = 'SELECT a.* FROM Artwork a JOIN User_Favorite_Artwork u on a.ArtworkID=u.ArtworkID WHERE UserID=?'
            cursor.execute(query, (userId,))
            artwork_data = cursor.fetchall()
            if artwork_data:
                for artwork in artwork_data:
                    artwork_details = [
                        ['Artwork ID', artwork[0]],
                        ['Title', artwork[1]],
                        ['Description', artwork[2]],
                        ['CreationDate', artwork[3]],
                        ['Medium', artwork[4]],
                        ['ImageURL', artwork[5]]
                    ]
                    print(tabulate(artwork_details, tablefmt="grid"))
            else:
                raise UserNotFoundException(userId)
        except Exception as e:
            print(e)
        finally:
            cursor.close()









