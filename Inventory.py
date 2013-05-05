"""Inventory system processing module
"""

def getWine(user, wineID):
  """Retrieve wine from user's inventory
  
  Call the DataAccess layer to retrive information about the wine.
  Wine object epresenting properties of the wine that the IO layer uses to
  list the wine.
  
  Args:
    User user: The User object of the user.
    int wineID: The wineID of the wine being requested.
    
  Return:
    Wine: Wine object of the wine.
          Includes the information that will be displayed on the Inventory web page.
  """


def searchInventory(user, wine):
  """Search through inventories for matching wine.
  
  Call the DataAccess layer to find a wine matching the specified properties.
  
  Args:
    User user: The User object of the user.
    dict wine: A dict detailing properties of the wine to look for, in the form
               {wineName:*, winery:*, etc}. Not all fields stored in the database
               have to be present. The qualities field is another dict that stores
               the qualities of the wine.
               
  Return:
    list: A list of Wine objects of wines matching the search parameters.
  """
  
def addWineUser(user, wine, count, location = -1):
  """Add wine to user's inventory
  
  Call the DataAccess layer to insert the given wine into the specified inventory.
  If the wine doesn't exist already, generate a new wineID for it. If it does exist,
  increment its quantity. Update the Location History.
  
  Args:
    User user: The User object of the user who is adding the wine.
    dict wine: A dictionary representing a wine of the form {wineName:*, winery:*,...}
               Not all the fields stored in the database have to be present. For the 
               averageQualities key, the value is another dictionary specifying the 
               traits and float values.
    int count: The quantity of this wine to add.
    Location location: The Location object defining which inventory to insert in. If unspecified,
                       just store in user's total inventory.
  """
  
  
def moveWine(user, wine, location1, location2, count, copy = False):
  """Move a wine from one location to another
  
  Call the DataAccess layer to insert wines into location2. If copy is True, don't
  delete the wine from location1. Otherwise decrement the count of this wine in
  location1.
  Update the Location History.
  
  Args:
    User user: The User object of the user who is moving wines.
    Wine wine: The Wine object of the wine being moved.
    Location location1: The Location object of where the wine is currently stored.
    Location location2: The Location object of where the wine is moved to.
    int count: The number of wines to move. If more than the actual quantity, move all.
    bool copy: True if a copy of the wine is being stored in location 2, not the wine itself.
  """

def addInventory(user, locationName):
  """Add inventory location to user's location map
  
  Call the DataAccess layer to create a new inventory location in the user's Location
  Map. Update the Location History.
  
  Args:
    User user: The User object of the user who is adding the inventory.
    string locationName: The name of the new location.
  """
  
  
def deleteWineUser(user, wine, count):
  """Delete wine from user's inventory
  
  Call the DataAccess layer to find a specified wine in the user's inventories and delete it.
  Update the Location History.
  
  Args:
    User user: The User object of the user who is deleting wine.
    Wine wine: The Wine object of the wine being deleted.
    int count: The number of this wine to delete. If more than actually exist, delete all.
  """
  
  
def deleteInventory(user, location):
  """Delete user's inventory location
  
  Call the DataAccess layer to delete the location from the user's Location Map.
  Update the Location History.
  
  Args:
    User user: The User object of the user who is deleting a location.
    Location location: The Location object of the location being deleted.
  """


def editInventory(user, location, changes):
  """Edit a user's inventory
  
  Call the DataAccess layer to edit the properties of an inventory location. For every
  property specified in changes, replace the corresponding old property with the new one.
  
  Args:
    User user: The User object of the user who is deleting a location.
    Location location: The Location object of the location being modified.
    dict changes: A dictionary specifying properties and values of the form
                  {locationName:*, imagePath:*, etc}. Not all fields stored in the
                  database have to be present.
  """
  
  
def editEntryUser(user, wine, changes):
  """Edit a wine in the user's inventory
  
  Call the DataAccess layer to edit the properties of a wine. For every property specified in
  changes, replace the corresponding old property with the new one.
  
  Args:
    User user: The User object of the user who is editing wines.
    Wine wine: The Wine object of the wine to be edited.
    dict changes: A dictionary specifying properties and values of the form
                  {locationID:*, qualities:*, etc}. Not all fields stored in the database
                  have to be present. The qualities field contains another dict representing
                  wine properties.
  """
  
def importInventory(user, file):
  """Import a new inventory using an XML file
  
  Call the DataAccess layer to create a new inventory and give it the properties detailed
  in the XML file.
  
  Args:
    User user: The User object of the user who is importing an inventory.
    XML file: The XML file. Specifies the properties of the
              inventory and the wines stored in it.  There should be enough information
              to fully generate an inventory.
  """
  
  
def exportInventory(user, location):
  """Export an XML representation of an inventory
  
  Call the DataAccess layer to retrieve information about an inventory. Generate an XML file 
  representation of the data. Retrieve all the properties of the inventory location and wines
  contained in it.
  
  Args:
    User user: The User object of the user who is requesting an XML.
    Location location: The location of the inventory location.
  
  Return:
    The XML representation of the inventory.
    OPTIONS TO CONSIDER: A link to a created XML, A string containing all the info
  """
  
  
def viewStats(user, location):
  """Retrieve statistics about an inventory
  
  Call the DataAccess layer to retrieve necessary information about an inventory. Construct
  a dictionary detailing the information and return it.
  
  Args:
    User user: The User object of the user requesting stats.
    Location location: The Location object of the location being analyzed.
    
  Return:
    dict: A dictionary detailing information specified as required in Globals
  """
  
  
def sortInventory(user, location, key, descend = True):
  """Sort inventory by a specified key
  
  Call the DataAccess layer to retrieve the wines stored in the inventory. Use key to determine
  how to sort them. If key is numeric, check descend to see what order to sort in. Create a list
  of Wine objects in sorted order and return it.
  
  Args:
    User user: The User object of the user.
    Location location: The Location object of the inventory location.
    string key: Determines what property to sort by ("dryness", "sweetness", etc).
    bool descend: If key is a numeric property, check this to determine sort order.
    
  Return:
    list: A list of Wine objects in sorted order.
  """
 
 
def viewArchive(user, location):
  """Retrieve the archive of a user's inventory
  
  Call the DataAccess layer to retrieve details about the inventory's archive. Return the 
  necesary information as a dict.
  
  Args:
    User user: The User object of the user.
    Location location: The Location object of the inventory location.
    
  Return:
    dict: A dict representing the archive of the form {added:[*], removed:[*], etc}. Include
          timestamps for each element (have each element be a tuple including the time?).
  """
  
  
def rateWineUser(user, wine, rating):
  """Store user's rating of wine in database
  
  Call the DataAccess layer to store the wine's rating in the user's inventory.
  
  Args:
    User user: The User object of the user.
    Wine wine: The Wine object of the wine to be rated.
    int rating: The rating on a 1-5 scale.
  """
