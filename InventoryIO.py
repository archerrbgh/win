"""Inventory system IO module
"""

#Exceptions thrown below this layer are not caught here, they are allowed
# to raise up to the ajax layer

import Inventory


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
  # Check for invalid attributes and for null values in non null rows
  # raise the relevant exceptions for any error

def validateUser(user):
  # Check for invalid attributes and for null values in non null rows
  # raise the relevant exceptions for any error

def validateStorage(storage):
  # Check for invalid attributes and for null values in non null rows
  # raise the relevant exceptions for any error


#Exceptions - null, invalid input
