"""Inventory system processing module
"""

import DataAccess
import InventoryIO


def getInventory(user):
  """Retrieve user's inventory
  """
  
  
def addWineUser(userID, wine, locationID = -1):
  """Add wine to user's inventory
  
  Call the DataAccess layer to insert the given wine into the specified inventory.
  If the wine doesn't exist already, generate a new wineID for it. If it does exist,
  increment its quantity. Update the Location History.
  
  Args:
    int userID: The userID of the user who is adding the wine.
    dict wine: A dictionary representing a wine of the form {wineName:*, winery:*,...}
               Not all the fields stored in the database have to be present. For the 
               averageQualities key, the value is another dictionary specifying the 
               traits and float values.
    int locationID: The locationID defining which inventory to insert in. If unspecified,
                    just store in user's total inventory.
  """
  
  
def moveWine(userID, wineID, locationID1, locationID2, copy = False):
  """Move a wine from one location to another
  
  Call the DataAccess layer to insert the wine into location2. If copy is True, don't
  delete the wine from location1, and give the inserted wine a new wineID. 
  Update the Location History.
  
  Args:
    int userID: The userID of the user who is moving wines.
    int wineID: The wineID of the wine being moved.
    int locationID1: The locationID of where the wine is currently stored.
    int locationID2: The locationID of where the wine is moved to.
    bool copy: True if a copy of the wine is being stored in location 2, not the wine itself.
  """

def addInventory(userID, locationName):
  """Add inventory location to user's location map
  
  Call the DataAccess layer to create a new inventory location in the user's Location
  Map. Update the Location History.
  
  Args:
    int userID: The userID of the user who is adding the inventory.
    string locationName: The name of the new location.
  """
  
  
def deleteWineUser(userID, wineID):
  """Delete wine from user's inventory
  
  Call the DataAccess layer to find a specified wine in the user's inventories and delete it.
  Update the Location History.
  
  Args:
    int userID: The userID of the user who is deleting wine.
    int wineID: The wineID of the wine being deleted.
  """
  
  
def deleteInventory(userID, locationID):
  """Delete user's inventory location
  
  Call the DataAccess layer to delete the location from the user's Location Map.
  Update the Location History.
  
  Args:
    int userID: The userID of the user who is deleting a location.
    int locationID: The locationID of the location being deleted.
  """
