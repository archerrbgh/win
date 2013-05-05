"""Data access module
"""


def dbGetUser(userID):
  """Retrive a user's profile from database
  
  Retrieve relevant information about a user from the database.
  Return a dictionary representing the user.
  
  Args:
    int userID: The userID of the user being retrieved.
    
  Return:
    dict: A dictionary specifying relevant information about the user, in the form
          {name:*, email:*, etc}. Store enough information to generate a user
          profile page.
  
  """


def dbCreateUser(username, password, attr = 0):
  """Add new user to database
  
  Insert a new user into the database with the given password, and optionally specify
  additional details from attr. Create a new userID for the user.
  
  Args:
    string username: The name of the user being created.
    string password: The user's password.
    dict attr: An optional attribute dict of the form {email:*, DOB:*, etc}. If this is
               included, then store the relevant information in the database for the user.
  """
  

def dbUpdateUser(userID, attr):
  """Update user profile in database with attributes
  
  Change information stored about the user in the database to match relevant information
  passed in attr.
  
  Args:
    int userID: The userID of the user being modified.
    dict attr: A dict specifying user attributes, of the form {email:*, DOB:*, etc}. Not every
               field stored in the database has to be present.
  """
  
  
# RECOMMENDATION SYSTEM
  
def dbGetWinesByAttr(attributes):
  """Retrieve wines from database with qualities similar
  to attributes
  """
 

def dbGetWinesByName(name):
  """Retrieve wines from database with the given name
  """
 

def dbAddWineGlobal(wine):
  """Add a new wine to the global database
  """
  
  
def dbDeleteWineGlobal(wine):
  """Delete wine from the global database
  """


def dbRateWineGlobal(wine, rating):
  """Update the global rating of a wine in database
  """
  
  
def dbRandomWines():
  """Retrieve a random set of wines from database
  """
  
  
# INVENTORY SYSTEM

def dbGetInventory(userID):
  """Retrieve a user's inventory from database
  
  Return a list of wineIDs representing the wines in a user's inventory.
  
  Args:
    int userID: The userID of the user.
    
  Return:
    list: A list of wineIDs. Contains the wineID of every wine in the user's
          inventory.
  """
  
  
def dbAddWineUser(userID, wine, count, locationID = -1):
  """Add a wine to the user's inventory in database
  
  Insert the given wine into the specified inventory.
  Include the attributes in wine, which will include a new
  wineID. If locationID is unspecified, store the wine in the user's
  global inventory.
  
  Args:
    int userID: The userID of the user.
    dict wine: A dict specifying wine attributes, of the form 
              {wineID:*, wineName:*, etc}.
    int count: The number of this wine to add.
    int locationID: If specified, the locationID of the inventory to
                    insert the wine into.
  """
  
  
def dbAddInventory(user, storage):
  """Add a new storage location to user's profile
  in database
  """
  
  
def dbDeleteWineUser(user, wine):
  """Delete a wine from user's inventory in database
  """
  
  
def dbDeleteStorage(user, storage):
  """Delete a user's storage location in database
  """
  
  
def dbAddToStorage(user, storage, wine):
  """Add wine to a user's storage location in database
  """
  
  
def dbRateWineUser(user, wine, rating):
  """Store user's rating of wine in database
  """
