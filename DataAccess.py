"""Data access module
"""


def dbGetUser(userID):
  """Retrive a user's profile from database
  
  Retrieve relevant information about a user from the database.
  Return a dictionary representing the user.
  
  Args:
    int userID: The userID of the user being retrieved.
    
  Return:
    User: A User object specifying relevant information about the user}. Store enough 
          information to generate a user profile page.
  
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
  

def dbUpdateUser(user, attr):
  """Update user profile in database with attributes
  
  Change information stored about the user in the database to match relevant information
  passed in attr.
  
  Args:
    Object user: The User object of the user being modified.
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

def dbGetInventory(user):
  """Retrieve a user's inventory from database
  
  Return a list of wineIDs representing the wines in a user's inventory.
  
  Args:
    User user: The User object of the user.
    
  Return:
    list: A list of Location objects detailing the user's entire inventory. 
  """
  
  
def dbAddWineUser(user, wine, count, location = -1):
  """Add a wine to the user's inventory in database
  
  Insert the given wine into the specified inventory.
  Include the attributes in wine, which will include a new
  wineID. If location is unspecified, store the wine in the user's
  global inventory.
  
  Args:
    User user: The User object of the user.
    Wine wine: A Wine object representing a wine.
    int count: The number of this wine to add.
    Location location: If specified, the location of the inventory to
                       insert the wine into.
  """
  
  
def dbAddInventory(user, location):
  """Add a new inventory location to user's profile in database
  
  Insert a new inventory location into the user's Location Map.
  
  Args:
    User user: The User object of the user.
    Location location: The Location object of the location.
  """
  
  
def dbDeleteWineUser(user, wine, count):
  """Delete a wine from user's inventory in database
  
  Delete count amounts of the wine from the user's locations.
  
  Args:
    User user: The User object of the user.
    Wine wine: The Wine object of the wine.
  """
  
  
def dbDeleteInventory(user, location):
  """Delete a user's inventory location in database
  
  Delete an inventory location from user's Location Map.
  
  Args:
    User user: The User object of the user.
    Location location: The Location object of the location.
  """
  
  
def dbRateWineUser(user, wine, rating):
  """Store user's rating of wine in database
  
  Store the rating of the specified wine in the user's inventory.
  
  Args:
    User user: The User object of the user.
    Wine wine: The wine object of the wine.
    int rating: The rating on a 1-5 scale.
  
  """
