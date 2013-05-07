"""Inventory system processing module
"""

def getWine(user, locationID, wineID):
  """Retrieve wine from user's inventory
  
  Call the DataAccess layer to retrive information about the wine.
  Returns LocationInventory object representing properties of the wine 
  that the IO layer uses to list the wine.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the wine being requested.
    int wineID: The wineID of the wine being requested.
    
  Return:
    LocationInventory: LocationInventory object of the wine.
                       Includes the information that will be displayed on the Inventory web page.
  """


def getLocation(user, locationID):
  """Retrieve a location from the user's location map
  
  Call the DataAccess layer to retrieve a location.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location.
    
  Return:
    LocationMap: LocationMap object of the location.
  """
  
  
def getLocationHistory(user, locationID, wineID):
  """Retrieve a location history 
  
  Call the DataAccess layer to retrieve a location history.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location history.
    int wineID: The wineID of the location history.
    
  Return:
    LocationHistory: LocationHistory object of the location history.
  """
  

def addLocationHistory(user, locationID, wineID, eventTag):
  """Add a Location History to the database.
  
  Call the DataAccess layer to insert a new Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location.
    int wineID: The wineID of the wine.
    string eventTag: Message detailing the history.
  """


def searchInventory(user, wine):
  """Search through inventories for matching wine.
  
  Call the DataAccess layer to find a wine matching the specified properties.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory wine: A partially filled LocationInventory object detailing properties of the wine 
                            to look for. Not all fields stored in the database have to be present as 
                            instance variables, some of which might be None.
               
  Return:
    list: A list of LocationInventory objects of wines matching the search parameters.
  """
  
  
def addWineUser(user, wine, count, location):
  """Add wine to user's inventory
  
  Call the DataAccess layer to insert the given wine into the specified inventory.
  If the wine doesn't exist already, generate a new wineID for it and assign its location. 
  If it does exist, increment its quantity. Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is adding the wine.
    LocationInventory wine: A partially filled LocationInventory object representing the wine.
                            Not all the fields stored in the database have to be present,
                            such as li_locationID and li_wineID.
    int count: The quantity of this wine to add.
    LocationMap location: The LocationMap object defining which inventory to insert in.
  """
  
  
def moveWine(user, wine, location, count, copy = False):
  """Move a wine from one location to another
  
  Call the DataAccess layer to insert wines into location2. If copy is True, don't
  delete the wine from location1. Otherwise decrement the count of this wine in
  location1.
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is moving wines.
    LocationInventory wine: The LocationInventory object of the wine being moved.
    LocationMap location: The LocationMap object defining where to move the wine.
    int count: The number of wines to move. If more than the actual quantity, move all.
    bool copy: True if a copy of the wine is being stored in location, not the wine itself.
  """


def addInventory(user, location):
  """Add inventory location to user's location map
  
  Call the DataAccess layer to create a new inventory location in the user's Location
  Map. Assign everything other than locationName and imagePath, which are already made. 
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is adding the inventory.
    LocationMap location: Partially filled LocationMap object that only defines locationName and
                          maybe imagePath.
  """
  
  
def deleteWineUser(user, wine, count):
  """Delete wine from user's inventory
  
  Call the DataAccess layer to find a specified wine in the user's inventories and delete it.
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting wine.
    LocationInventory wine: The LocationInventory object of the wine being deleted.
    int count: The number of this wine to delete. If more than actually exist, delete all.
  """
  
  
def deleteInventory(user, location):
  """Delete user's inventory location
  
  Call the DataAccess layer to delete the location from the user's Location Map.
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting a location.
    LocationMap location: The LocationMap object of the location being deleted.
  """


def editInventory(user, location, changes):
  """Edit a user's inventory
  
  Call the DataAccess layer to edit the properties of an inventory location. For every
  property specified in changes, replace the corresponding old property with the new one.
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting a location.
    LocationMap location: The LocationMap object of the location being modified.
    dict changes: A dictionary specifying properties and values of the form
                  {locationName:*, imagePath:*, etc}. Not all fields stored in the
                  database have to be present.
  """
  
  
def editEntryUser(user, wine, changes):
  """Edit a wine in the user's inventory
  
  Call the DataAccess layer to edit the properties of a wine. For every property specified in
  changes, replace the corresponding old property with the new one. 
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user who is editing wines.
    LocationInventory wine: The LocationInventory object of the wine to be edited.
    dict changes: A dictionary specifying properties and values of the form
                  {li_locationID:*, quantity:*, etc}. Not all fields stored in the database
                  have to be present.
  """
  
  
def importInventory(user, file):
  """Import a new inventory using an XML file
  
  Call the DataAccess layer to create a new inventory and give it the properties detailed
  in the XML file.
  
  Args:
    UserInfo user: The UserInfo object of the user who is importing an inventory.
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
    UserInfo user: The UserInfo object of the user who is requesting an XML.
    LocationMap location: The LocationMap object of the inventory location.
  
  Return:
    The XML representation of the inventory.
    OPTIONS TO CONSIDER: A link to a created XML, A string containing all the info
  """
  
  
def viewStats(user, location):
  """Retrieve statistics about an inventory
  
  Call the DataAccess layer to retrieve necessary information about an inventory. Construct
  a dictionary detailing the information and return it.
  
  Args:
    UserInfo user: The UserInfo object of the user requesting stats.
    LocationMap location: The LocationMap object of the location being analyzed.
    
  Return:
    dict: A dictionary detailing information specified as required in Globals
  """
  
  
def sortInventory(user, location, key, descend = True):
  """Sort inventory by a specified key
  
  Call the DataAccess layer to retrieve the wines stored in the inventory. Use key to determine
  how to sort them. If key is numeric, check descend to see what order to sort in. Create a list
  of Wine objects in sorted order and return it.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationMap location: The LocationMap object of the inventory location.
    string key: Determines what property to sort by ("dryness", "sweetness", etc).
    bool descend: If key is a numeric property, check this to determine sort order.
    
  Return:
    list: A list of LocationInventory objects in sorted order.
  """
 
 
def viewArchive(user, location):
  """Retrieve the archive of a user's inventory
  
  Call the DataAccess layer to retrieve details about the inventory's archive. Return the 
  necesary information as a dict.
  
  Args:
    UserInfo user: The User object of the user.
    LocationMap location: The LocationMap object of the inventory location.
    
  Return:
    list: A list of LocationHistory objects.
  """
  
  
def rateWineUser(user, wine, rating):
  """Store user's rating of wine in database
  
  Call the DataAccess layer to store the wine's rating in the user's inventory.
  Update the Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory wine: The LocationInventory object of the wine to be rated.
    int rating: The rating on a 1-5 scale.
  """
