"""Inventory system IO module
"""

#Exceptions thrown below this layer are not caught here, they are allowed
# to raise up to the ajax layer

import Inventory
import re


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
  # Check the object's attributes for null values
  for attr in wine.__dict__.iteritems():
    if attr == None:
      raise Exception("NullException")

  # Check the object's attributes for proper type

  # Check the object's attributes for proper range
  

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

  # TODO: check if dateOfBirth is a valid date

  if not isinstance(user.imagePath, basestring):
    raise Exception("ImproperTypeException")


  # Check the object's attributes for proper range

  # TODO: Check for password length
  # TODO: Check for date of birth range

def validateStorage(storage):
  """ Check for invalid attributes and for null values in non null rows
  raise the relevant exceptions for any error
  """
  # Check the object's attributes for null values
  for attr in storage.__dict__.iteritems():
    if attr == None:
      raise Exception("NullException")
  # Check the object's attributes for proper type

  # Check the object's attributes for proper range


#Exceptions - null, invalid type input, out of range
