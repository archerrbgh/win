"""Inventory system processing module
"""

import DataAccess
import Globals
import InventoryIO
import Wine


def getWine(userID, wineID):
  """Retrieve wine from user's inventory
  
  Call the DataAccess layer to retrive information about the wine.
  Return a dict representing properties of the wine that the IO layer uses to
  list the wine.
  
  Args:
    int userID: The userID of the user.
    int wineID: The wineID of the wine being requested.
    
  Return:
    dict: Dict representing the wine in the form {wineName:*, personalStarRating:*, etc}
          Include the information that will be displayed on the Inventory web page.
  """


def searchInventory(userID, wine):
  """Search through inventories for matching wine.
  
  Call the DataAccess layer to find a wine matching the specified properties.
  
  Args:
    int userID: The userID of the user.
    dict wine: A dict detailing properties of the wine to look for, in the form
               {wineName:*, winery:*, etc}. Not all fields stored in the database
               have to be present. The qualities field is another dict that stores
               the qualities of the wine.
               
  Return:
    list: A list of wineIDs of wines matching the search parameters.
  """
  
def addWineUser(userID, wine, count, locationID = -1):
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
    int count: The quantity of this wine to add.
    int locationID: The locationID defining which inventory to insert in. If unspecified,
                    just store in user's total inventory.
  """
  
  
def moveWine(userID, wineID, locationID1, locationID2, count, copy = False):
  """Move a wine from one location to another
  
  Call the DataAccess layer to insert wines into location2. If copy is True, don't
  delete the wine from location1. Otherwise decrement the count of this wine in
  location1.
  Update the Location History.
  
  Args:
    int userID: The userID of the user who is moving wines.
    int wineID: The wineID of the wine being moved.
    int locationID1: The locationID of where the wine is currently stored.
    int locationID2: The locationID of where the wine is moved to.
    int count: The number of wines to move. If more than the actual quantity, move all.
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
  
  
def deleteWineUser(userID, wineID, count):
  """Delete wine from user's inventory
  
  Call the DataAccess layer to find a specified wine in the user's inventories and delete it.
  Update the Location History.
  
  Args:
    int userID: The userID of the user who is deleting wine.
    int wineID: The wineID of the wine being deleted.
    int count: The number of this wine to delete. If more than actually exist, delete all.
  """
  
  
def deleteInventory(userID, locationID):
  """Delete user's inventory location
  
  Call the DataAccess layer to delete the location from the user's Location Map.
  Update the Location History.
  
  Args:
    int userID: The userID of the user who is deleting a location.
    int locationID: The locationID of the location being deleted.
  """


def editInventory(userID, locationID, changes):
  """Edit a user's inventory
  
  Call the DataAccess layer to edit the properties of an inventory location. For every
  property specified in changes, replace the corresponding old property with the new one.
  
  Args:
    int userID: The userID of the user who is deleting a location.
    int locationID: The locationID of the location being modified.
    dict changes: A dictionary specifying properties and values of the form
                  {locationName:*, imagePath:*, etc}. Not all fields stored in the
                  database have to be present.
  """
  
  
def editEntryUser(userID, wineID, changes):
  """Edit a wine in the user's inventory
  
  Call the DataAccess layer to edit the properties of a wine. For every property specified in
  changes, replace the corresponding old property with the new one.
  
  Args:
    int userID: The userID of the user who is editing wines.
    int wineID: The wineID of the wine to be edited.
    dict changes: A dictionary specifying properties and values of the form
                  {locationID:*, qualities:*, etc}. Not all fields stored in the database
                  have to be present. The qualities field contains another dict representing
                  wine properties.
  """
  
def importInventory(userID, xml):
  """Import a new inventory using an XML file
  
  Call the DataAccess layer to create a new inventory and give it the properties detailed
  in the XML file.
  
  Args:
    int userID: The userID of the user who is importing an inventory.
    dict xml: A dictionary representation of the XML file. Specifies the properties of the
              inventory and the wines stored in it. Its format is 
              {locationName:*, creationTimestamp:*, etc). There should be enough information
              to fully generate an inventory.
  """
  
  
def exportInventory(userID, locationID):
  """Export an XML representation of an inventory
  
  Call the DataAccess layer to retrieve information about an inventory. Generate an XML file 
  representation of the data. Retrieve all the properties of the inventory location and wines
  contained in it.
  
  Args:
    int userID: The userID of the user who is requesting an XML.
    int locationID: The locationID of the inventory location.
  
  Return:
    The XML representation of the inventory.
    OPTIONS TO CONSIDER: A link to a created XML, A string containing all the info
  """
  
  
def viewStats(userID, locationID):
  """Retrieve statistics about an inventory
  
  Call the DataAccess layer to retrieve necessary information about an inventory. Construct
  a dictionary detailing the information and return it.
  
  Args:
    int userID: The userID of the user requesting stats.
    int locationID: The locationID of the location being analyzed.
    
  Return:
    dict: A dictionary detailing information specified as required in Globals
  """
  
  
def sortInventory(userID, locationID, key, descend = True):
  """Sort inventory by a specified key
  
  Call the DataAccess layer to retrieve the wines stored in the inventory. Use key to determine
  how to sort them. If key is numeric, check descend to see what order to sort in. Create a list
  of wineIDs in sorted order and return it.
  
  Args:
    int userID: The userID of the user.
    int locationID: The locationID of the inventory location.
    string key: Determines what property to sort by ("dryness", "sweetness", etc).
    bool descend: If key is a numeric property, check this to determine sort order.
  """
 
 
def viewArchive(userID, locationID):
  """Retrieve the archive of a user's inventory
  
  Call the DataAccess layer to retrieve details about the inventory's archive. Return the 
  necesary information as a dict.
  
  Args:
    int userID: The userID of the user.
    int locationID: The locationID of the inventory location.
    
  Return:
    dict: A dict representing the archive of the form {added:[*], removed:[*], etc}. Include
          timestamps for each element (have each element be a tuple including the time?).
  """
