"""Inventory system IO module
"""

#Exceptions thrown below this layer are not caught here, they are allowed
# to raise up to the ajax layer

import Inventory
import re
import datetime

def inputGetInventory(user):
  """Preprocess retrieval of user's inventory
  """
  validateUser(user)
  getInventory(user)
  getInventory(user) 
  
def inputAddWineUser(user, wine):
  """Preprocess addition of wine to user's inventory
  """
  validateUser(user)
  validateWine(wine)
  addWineUser(user,wine)
  
def inputAddStorage(user, storage):
  """Preprocess addition of storage location to
  user's inventory
  """
  validateUser(user)
  validateStorage(storage)
  addStorage(user,storage)
    
def inputDeleteUserWine(user, wine):
  """Preprocess deletion of wine from user's inventory
  """
  validateUser(user)
  validateWine(wine)
  deleteUserWine(user,wine)
   
def inputDeleteStorage(user, storage):
  """Preprocess deletion of user's storage location
  """
  validateUser(user)
  validateStorage(storage)
  deleteStorage(user,storage)
  
def inputAddToStorage(user, storage, wine):
  """Preprocess addition of wine to user's storage
  location
  """
  validateUser(user)
  validateStorage(storage)
  validateWine(wine)
  addToStorage(user,storage,wine)

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
