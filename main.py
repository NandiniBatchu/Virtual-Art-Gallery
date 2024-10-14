import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from tabulate import tabulate
from exception.UserNotFoundException import UserNotFoundException
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.artwork import Artwork


class MainModule:
    def __init__(self):
        self.service=VirtualArtGalleryImpl()
    def menu(self):
        print("*"*50)
        print("Welcome to Virtual Art Gallery")
        print("*"*50)
        while True:
            menu=[
                ["1.","Add artwork"],
                ["2.","Update artwork"],
                ["3.","Remove artwork"],
                ["4.","Get Artwork By ID"],
                ["5.","Search artworks"],
                ["6.","Add Artwork To Favorite"],
                ["7.","Remove Artwork From Favorite"],
                ["8","Get User Favorite Artworks"],
                ["9","Exit"]
            ]

            print(tabulate(menu,headers=["Option","Description"],tablefmt="grid"))

            choice=input("Enter your choice: ")

            if choice=="1":
                artworkId=self.service.get_next_artworkID()
                title=input("Enter artwork title: ")
                description=input("Enter artwork description: ")
                creationDate=input("Enter artwork creation date: ")
                medium=input("Enter artwork medium: ")
                imageUrl=input("Enter artwork image url: ")
                if artworkId is None:
                    print("-------Artwork ID cannot be null------")
                else:
                    artwork=Artwork(
                        artworkId=artworkId,
                        title=title,
                        description=description,
                        creationDate=creationDate,
                        medium=medium,
                        imageURL=imageUrl
                    )
                    self.service.addArtwork(artwork)

            elif choice=="2":
                try:
                    artworkId=int(input("Enter Artwork ID to update: "))
                    cursor = self.service.connection.cursor()
                    query="SELECT * FROM Artwork WHERE ArtworkID=?"
                    cursor.execute(query,(artworkId,))
                    if cursor.fetchone() is None:
                        raise ArtWorkNotFoundException(artworkId)
                
                    newTitle=input("Enter new artwork title: ")
                    newDescription=input("Enter new artwork description: ")
                    newCreationDate=input("Enter new artwork creation date: ")
                    newMedium=input("Enter new artwork medium: ")
                    newImageUrl=input("Enter new artwork image url: ")
                    artwork=Artwork(
                        artworkId=artworkId,
                        title=newTitle,
                        description=newDescription,
                        creationDate=newCreationDate,
                        medium=newMedium,
                        imageURL=newImageUrl
                    )
                    self.service.updateArtwork(artwork,artworkId)
                except ArtWorkNotFoundException as e:
                    print("Error:", e) 
                except Exception as e:
                    print("An unexpected error occurred:", e)
                

            elif choice=="3":
                try:
                    artworkId = int(input("Enter Artwork ID to remove: "))
                except Exception as e:
                    print("Invalid input for Artwork ID.",e)
                    continue
                self.service.removeArtwork(artworkId)

            elif choice=="4":
                try:
                    artworkId=int(input("Enter Artwork ID to get details: "))
                    self.service.getArtworkById(artworkId)
                except Exception as e:
                    print("Invalid input:",e)
                
                
            elif choice=="5":
                search_object=input("Enter Search Object: ")
                self.service.searchArtworks(search_object)

            elif choice=="6":
                try:
                    userID=int(input("Enter User ID: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Users WHERE UserID=?"
                    cursor.execute(query, (userID,))
                    if cursor.fetchone() is None:
                        raise UserNotFoundException(userID)  
                    artworkId=int(input("Enter Artwork ID to add to favourites: "))
                    self.service.addArtworkToFavorite(userID,artworkId)
                except UserNotFoundException as e:
                    print("Error:", e)  
                except Exception as e:
                    print("Invalid input:",e)
              

            elif choice=="7":
                try:
                    userID=int(input("Enter User ID: "))
                    cursor = self.service.connection.cursor()
                    query = "SELECT * FROM Users WHERE UserID=?"
                    cursor.execute(query, (userID,))
                    if cursor.fetchone() is None:
                        raise UserNotFoundException(userID)  # Raise exception if user is not found

                    artworkId=int(input("Enter Artwork ID to remove favourites: "))
                    self.service.removeArtworkFromFavorite(userID,artworkId)
                except UserNotFoundException as ue:
                    print("Error:",ue)  # Handle the exception here
                except Exception as e:
                    print('Invalid input:',e)
                

            elif choice=="8":
                try:
                    userID=int(input("Enter User ID: "))
                    self.service.getUserFavoriteArtworks(userID)
                except Exception as e:
                    print("Invalid input:",e)
                

            elif choice=="9":
                print("Thank you for using Virtual Art Gallery!")
                break
if __name__ == '__main__':
    MainModule().menu()












