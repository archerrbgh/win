"""Data access module
"""


def dbGetUser(username):
  """Retrive a user's profile from database
  """


def dbCreateUser(username, password):
  """Add new user to database
  """
  

def dbUpdateUser(attributes):
  """Update user profile in database with attributes
  """
  
  
def dbGetWinesByAttr(attributes):
  """Retrieve wines from database with qualities similar
  to attributes
  """
 

def dbGetWinesByName(name):
  """Retrieve wines from database with the given name
  """
 

def dbAddWineGlobal(wine)
  """Add a new wine to the global database
  """
  
  
def dbRandomWines():
  """Retrieve a random set of wines from database
  """
  

def dbGetInventory(user):
  """Retrieve a user's inventory from database
  """
  
  
def dbAddUserWine(user, wine):
  """Add a wine to the user's inventory in database
  """
  
  
def dbAddUserStorage(user, storage):
  """Add a new storage location to user's profile
  in database
  """
  
  
def dbDeleteUserWine(user, wine):
  """Delete a wine from user's inventory in database
  """
  
  
def dbDeleteUserStorage(user, storage):
  """Delete a user's storage location in database
  """
  
  
def dbAddToStorage(user, storage, wine):
  """Add wine to a user's storage location in database
  """
