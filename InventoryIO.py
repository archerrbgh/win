"""Inventory system IO module
"""

#Exceptions thrown below this layer are not caught here, they are allowed
# to raise up to the ajax layer

import re
import datetime


def inputGetWine(user, locationID, wineID):
  """Preprocess retrieval of wine from user's inventory
  
  Call the Model layer to retrive information about the wine.
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


def inputGetLocation(user, locationID):
  """Preprocess retrieval of a location from the user's location map
  
  Call the Model layer to retrieve a location.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location.
    
  Return:
    LocationMap: LocationMap object of the location.
  """


def inputGetLocationHistory(user, locationID, wineID):
  """Preprocess retrieval of a location history 
  
  Call the Model layer to retrieve a location history.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location history.
    int wineID: The wineID of the location history.
    
  Return:
    LocationHistory: LocationHistory object of the location history.
  """


def inputGetInventory(user):
  """Preprocess retrieval of user's inventory
  
  Return a list of LocationInventory objects representing the wines in a user's inventory.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    
  Return:
    list: A list of LocationInventory objects detailing the user's entire inventory.
  """
  validateUser(user)
  getInventory(user)
  getInventory(user) 
  
  
def inputSearchInventory(user, wine):
  """Preprocess searching through inventories for matching wine.
  
  Return a list of LocationInventory objects showing wines that fit the search parameters.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    dict wine: A dict detailing properties of the wine to look for. Not all fields stored 
               in the database have to be present.
               
  Return:
    list: A list of LocationInventory objects of wines matching the search parameters.
  """
  
  
def inputAddWineUser(user, wine, count, location):
  """Preprocess addition of wine to user's inventory
  
  Create a LocationInventory object using the wine dict and pass it to the Model layer.
  
  Args:
    UserInfo user: The UserInfo object of the user who is adding the wine.
    dict wine: A dict representing the wine with format similar to the class' instance variables.
               Not all the fields stored in the database have to be present,
               such as li_locationID and li_wineID.
    int count: The quantity of this wine to add.
    LocationMap location: The LocationMap object defining which inventory to insert in.
  """
  validateUser(user)
  validateWine(wine)
  addWineUser(user,wine)
  
  
def inputMoveWine(user, wine, location, count, copy = False):
  """Preprocess moving a wine from one location to another
  
  Args:
    UserInfo user: The UserInfo object of the user who is moving wines.
    LocationInventory wine: The LocationInventory object of the wine being moved.
    LocationMap location: The LocationMap object defining where to move the wine.
    int count: The number of wines to move. If more than the actual quantity, move all.
    bool copy: True if a copy of the wine is being stored in location, not the wine itself.
  """
  
  
def inputAddInventory(user, location):
  """Preprocess addition of storage location to user's inventory
  
  Create a LocationMap object using the location dict and pass it to the Model layer.
  
  Args:
    UserInfo user: The UserInfo object of the user who is adding the inventory.
    dict location: dict that only defines locationName and maybe imagePath.
  """
  validateUser(user)
  validateStorage(storage)
  addStorage(user,storage)
    
    
def inputDeleteWineUser(user, wine, count):
  """Preprocess deletion of wine from user's inventory
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting wine.
    LocationInventory wine: The LocationInventory object of the wine being deleted.
    int count: The number of this wine to delete. If more than actually exist, delete all.
  """
  validateUser(user)
  validateWine(wine)
  deleteUserWine(user,wine)
   
   
def inputDeleteInventory(user, location):
  """Preprocess deletion of user's inventory location
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting a location.
    LocationMap location: The LocationMap object of the location being deleted.
  """
  validateUser(user)
  validateStorage(storage)
  deleteStorage(user,storage)


def inputEditInventory(user, location, changes):
  """Preprocess editing a user's inventory
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting a location.
    LocationMap location: The LocationMap object of the location being modified.
    dict changes: A dictionary specifying properties and values of the form
                  {locationName:*, imagePath:*, etc}. Not all fields stored in the
                  database have to be present.
  """
  
  
def inputEditEntryUser(user, wine, changes):
  """Preprocess editing a wine in the user's inventory
  
  Args:
    UserInfo user: The UserInfo object of the user who is editing wines.
    LocationInventory wine: The LocationInventory object of the wine to be edited.
    dict changes: A dictionary specifying properties and values of the form
                  {li_locationID:*, quantity:*, etc}. Not all fields stored in the database
                  have to be present.
  """
  
  
def inputImportInventory(user, xfile):
  """Preprocess importing a new inventory using an XML file
  
  Args:
    UserInfo user: The UserInfo object of the user who is importing an inventory.
    XML xfile: The XML file. Specifies the properties of the
               inventory and the wines stored in it.  There should be enough information
               to fully generate an inventory.
  """
  
  
def inputExportInventory(user, location):
  """Preprocess exporting an XML representation of an inventory
  
  Args:
    UserInfo user: The UserInfo object of the user who is requesting an XML.
    LocationMap location: The LocationMap object of the inventory location.
  
  Return:
    The XML representation of the inventory.
    OPTIONS TO CONSIDER: A link to a created XML, A string containing all the info
  """
  
  
def inputViewStats(user, location):
  """Preprocess retrieval of statistics about an inventory
  
  Args:
    UserInfo user: The UserInfo object of the user requesting stats.
    LocationMap location: The LocationMap object of the location being analyzed.
    
  Return:
    dict: A dictionary detailing information specified as required in Globals
  """
  
  
def inputSortInventory(user, location, key, descend = True):
  """Preprocess sorting inventory by a specified key
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationMap location: The LocationMap object of the inventory location.
    string key: Determines what property to sort by ("dryness", "sweetness", etc).
    bool descend: If key is a numeric property, check this to determine sort order.
    
  Return:
    list: A list of LocationInventory objects in sorted order.
  """


def inputViewArchive(user, location):
  """Preprocess retrieval of the archive of a user's inventory
  
  Args:
    UserInfo user: The User object of the user.
    LocationMap location: The LocationMap object of the inventory location.
    
  Return:
    list: A list of LocationHistory objects.
  """
  
  
def inputRateWineUser(user, wine, rating):
  """Preprocess storing user's rating of wine in database
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory wine: The LocationInventory object of the wine to be rated.
    int rating: The rating on a 1-5 scale.
  """


def validateWine(wine):
  """ Check for invalid attributes and for null values in non null rows
  raise the relevant exceptions for any error
  """
  # Check the object's attributes for null values #
  if wine.li_locationID == None:
    raise Exception("NullException")

  if wine.li_wineID == None:
    raise Exception("NullException")

  if wine.quantity == None:
    raise Exception("NullException")

  if wine.isWishlist == None:
    raise Exception("NullException")
    
  # Check the object's attributes for proper type #

  if not isinstance(wine.li_locationID, (int,long)):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.li_wineID, (int,long)):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.quantity, (int,long)):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.personalStarRating, (int,long)):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.isWishlist, bool):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.bitter, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.sweet, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.sour, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.salty, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.chemical, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.pungent, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.oxidized, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.microbiological, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.floral, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.spicy, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.fruity, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.vegetative, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.nutty, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.carmelized, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.woody, float):
    raise Exception("ImproperTypeException")

  if not isinstance(wine.earthy, float):
    raise Exception("ImproperTypeException")

  # Check the object's attributes for proper range #

  if wine.li_locationID < 0:
    raise Exception("InvalidRangeException")

  if wine.li_wineID < 0:
    raise Exception("InvalidRangeException")

  if wine.quantity < 0:
    raise Exception("InvalidRangeException")

  if wine.personalStarRating < 0 or wine.personalStarRating > 5:
    raise Exception("InvalidRangeException")

  if wine.bitter < 0:
    raise Exception("InvalidRangeException")

  if wine.sweet < 0:
    raise Exception("InvalidRangeException")

  if wine.sour < 0:
    raise Exception("InvalidRangeException")

  if wine.salty < 0:
    raise Exception("InvalidRangeException")

  if wine.chemical < 0:
    raise Exception("InvalidRangeException")

  if wine.pungent < 0:
    raise Exception("InvalidRangeException")

  if wine.oxidized < 0:
    raise Exception("InvalidRangeException")

  if wine.microbiological < 0:
    raise Exception("InvalidRangeException")

  if wine.floral < 0:
    raise Exception("InvalidRangeException")

  if wine.spicy < 0:
    raise Exception("InvalidRangeException")

  if wine.fruity < 0:
    raise Exception("InvalidRangeException")

  if wine.vegetative < 0:
    raise Exception("InvalidRangeException")

  if wine.nutty < 0:
    raise Exception("InvalidRangeException")

  if wine.caramelized < 0:
    raise Exception("InvalidRangeException")

  if wine.woody < 0:
    raise Exception("InvalidRangeException")

  if wine.earthy < 0:
    raise Exception("InvalidRangeException")


def validateUser(user):
  """ Check for invalid attributes and for null values in non null rows
  raise the relevant exceptions for any error
  """
  # Check the object's attributes for null values #
  if user.userID == None:
    raise Exception("NullException")
  if user.emailAddress == None:
    raise Exception("NullException")
  if user.password == None:
    raise Exception("NullException")

    
  # Check the object's attributes for proper type #
  if not isinstance(user.userID , (int,long)):
    raise Exception("ImproperTypeException")
  
  # regex match to check for valid email
  if not re.match(r"[^@]+@[^@]+\.[^@]+", user.emailAddress):
    raise Exception("ImproperTypeException")
  
  if not isinstance(user.password, basestring):
    raise Exception("ImproperTypeException")

  # Note: What will happen here if user.name ==  None?
  if not isinstance(user.name, basestring):
    raise Exception("ImproperTypeException")

  if not isinstance(user.location, basestring):
    raise Exception("ImproperTypeException")

  # Check if dateOfBirth is a valid date
  try:
    datetime.datetime.strptime(user.dateOfBirth, '%Y-%m-%d')
  except ValueError:
    raise Exception("ImproperTypeException")

  if not isinstance(user.imagePath, basestring):
    raise Exception("ImproperTypeException")


  # Check the object's attributes for proper range #

  if user.userID < 0:
    raise Exception("InvalidRangeException")
  
  if len(user.emailAddress) > 255:
    raise Exception("InvalidRangeException")

  if len(user.password) > 255:
    raise Exception("InvalidRangeException")

  # Passwords must be 6 characters or more
  if len(user.password) < 6:
    raise Exception("InvalidRangeException")

  if len(user.name) > 255:
    raise Exception("InvalidRangeException")

  if len(user.location) > 255:
    raise Exception("InvalidRangeException")
  
  # Check for date of birth range. No Methuselahs allowed
  if int(user.dateOfBirth[:4]) < 1910:
    raise Exception("InvalidRangeException")

  if len(user.imagePath) > 255:
    raise Exception("InvalidRangeException")

def validateStorage(storage):
  """ Check for invalid attributes and for null values in non null rows
  raise the relevant exceptions for any error
  """
  # Check the object's attributes for null values #
  if storage.locationID == None:
    raise Exception("NullException")

  if storage.lm_userID == None:
    raise Exception("NullException")

  if storage.locationName == None:
    raise Exception("NullException")

  if storage.timeCreated == None:
    raise Exception("NullException")

  # Check the object's attributes for proper type #
  if not isinstance(storage.locationID, (int,long)):
    raise Exception("ImproperTypeException")

  if not isinstance(storage.lm_userID, (int,long)):
    raise Exception("ImproperTypeException")

  if not isinstance(storage.locationName, basestring):
    raise Exception("ImproperTypeException")

  # Check timeCreated to make sure it's a valid timestamp
  try:
    datetime.datetime.strptime(storage.timeCreated, "%d-%m-%Y %I:%M:%S")
  except ValueError:
    raise Exception("ImproperTypeException")

  if not isinstance(storage.imagePath, basestring):
    raise Exception("ImproperTypeException")

  # Check the object's attributes for proper range #

  if storage.locationID < 0:
    raise Exception("InvalidRangeException")

  if storage.lm_userID < 0:
    raise Exception("InvalidRangeException")

  if len(storage.locationName) > 255:
    raise Exception("InvalidRangeException")

  if len(storage.imagePath) > 255:
    raise Exception("InvalidRangeException")
  
#Exceptions - null, invalid type input, out of range
