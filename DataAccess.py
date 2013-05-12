"""Data access module
""" 
def dbGetUser(userID):
  """Retrive a user's profile from database
  
  Retrieve relevant information about a user from the database.
  Return a dictionary representing the user.
  
  Args:
    int userID: The userID of the user being retrieved.
    
  Return:
    UserInfo: A UserInfo object specifying relevant information about the user. Store enough 
              information to generate a user profile page.
  """


def dbCreateUser(user):
  """Add new user to database
  
  Insert a new user into the database.
  
  Args:
    UserInfo user: UserInfo object representing the user. Take all fields from this object.
  """
  	# Make an empty error dictionary
   	err = {}
   	
	email = user.email
  	pw = user.password
  	name = user.name
  	loc = user.location
  	dob = user.dob
  	image = user.imagePath
  	
  	#Create new UserInfo object to add to database
  	person = UserInfo(email, password, name, location, dob, image)
  	
  	db.session.add(person)
  	#db.session.add(user)
  	db.session.commit()
  	
  	if not err:
  		return (person, err)
  	else:
  		return (None, err)
		

def dbEditUser(user, attr):
  """Update user profile in database with attributes
  
  Change information stored about the user in the database to match relevant information
  passed in attr.
  
  Args:
    UserInfo user: The UserInfo object of the user being modified.
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
  #name = wine.wineName
  #varietal = wine.varietal
  #winery = wine.winery
  #type = wine.wineType
  #vintage = wine.vintage
  #region = wine.region
  #clusterID = wine.clusterID
  #cso = wine.cso
  #tags = wine.tags
  #description = wine.description
  #averageRating = wine.averageStarRating
  #image = wine.imagePath
  #barcode = wine.barcode
  #bitter = wine.bitter
  #sweet = wine.sweet
  #sour = wine.sour
  #salty = wine.salty
  #chemical = wine.chemical
  #pungent = wine.pungent
  #oxidized = wine.oxidized
  #microbio = wine.microbiological
  #floral = wine.floral
  #spicy = wine.spicy
  #fruity = wine.fruity
  #vegetative = wine.vegetative
  #nutty = wine.nutty
  #caramel = wine.carmelized
  #woody = wine.woody
  #earthy = wine.earthy
  #bottle = Wine(name, varietal, winery, type, vintage, region, clusterID, cso, tags, description,\
  #       		averageRating, image, barcode, bitter, sweet, sour, salty, chemical, pungent,\
  #       		oxidized, microbio, floral, spicy, fruity, vegetative, nutty, caramel, woody,\
  #       		earthy)
  #db.session.add(bottle)
  db.session.add(wine)
  db.session.commit()
  
  return ()
  
  
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
  
  Return a list of LocationInventory objects representing the wines in a user's inventory.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    
  Return:
    list: A list of LocationInventory objects detailing the user's entire inventory. 
  """
  
  
def dbGetLocation(user, locationID):
  """Retrieve a user's inventory location
  
  Retrieve an inventory location from the location map.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location.
    
  Return:
    LocationMap: The LocationMap object of the location.
  """
  

def dbGetWineUser(user, wineID, locationID):
  """Retrieve a user's wine from inventory
  
  Retrieve the specified wine from the user's location.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int wineID: The wineID of the wine.
    int locationID: The locationID of the wine's location.
    
  Return:
    LocationInventory: The LocationInventory object of the wine.
  """
  
  
def dbGetLocationHistory(user, locationID, wineID):
  """Retrieve a location history
  
  Retrieve a specific Location History.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    int locationID: The locationID of the location history.
    int wineID: The wineID of the location history.
    
  Return:
    LocationHistory: The LocationHistory object of the location history
  """
  
  
def dbSearchInventory(user, wine):
  """Search through inventories for matching wine.
  
  Find wines matching the specified properties.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    dict wine: A dict detailing properties of the wine to look for. Not all fields stored 
               in the database have to be present.
               
  Return:
    list: A list of LocationInventory objects of wines matching the search parameters.
  """
  
  
def dbAddWineUser(user, wine, count):
  """Add a wine to the user's inventory in database
  
  Insert the given wine into the specified inventory.
  Include the attributes in wine, which will include a new
  wineID.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory wine: A LocationInventory object representing a wine.
    int count: The number of this wine to add.
  """
  
  count++
    
def dbAddInventory(user, location):
  """Add a new inventory location to user's profile in database
  
  Insert a new inventory location into the user's Location Map.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationMap location: The LocationMap object of the location.
  """
  
  
def dbAddLocationHistory(user, history):
  """Add a new location history to the database.
  
  Insert a new location history into the database.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationHistory history: The LocationHistory object representing the new history.
  """
  
  
def dbDeleteWineUser(user, wine, count):
  """Delete a wine from user's inventory in database
  
  Delete count amounts of the wine from the user's locations.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory wine: The LocationInventory object of the wine.
  """
  
  
def dbDeleteInventory(user, location):
  """Delete a user's inventory location in database
  
  Delete an inventory location from user's Location Map.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory location: The LocationInventory object of the location.
  """
  

def dbEditInventory(user, location, changes):
  """Edit a user's inventory
  
  Edit the properties of an inventory location. For every property specified in 
  changes, replace the corresponding old property with the new one.
  
  Args:
    UserInfo user: The UserInfo object of the user who is deleting a location.
    LocationMap location: The LocationMap object of the location being modified.
    dict changes: A dictionary specifying properties and values of the form
                  {locationName:*, imagePath:*, etc}. Not all fields stored in the
                  database have to be present.
  """


def dbEditEntryUser(user, wine, changes):
  """Edit a wine in the user's inventory
  
  Edit the properties of a wine. For every property specified in
  changes, replace the corresponding old property with the new one.
  
  Args:
    UserInfo user: The UserInfo object of the user who is editing wines.
    LocationInventory wine: The LocationInventory object of the wine to be edited.
    dict changes: A dictionary specifying properties and values of the form
                  {li_locationID:*, li_wineID:*, etc}. Not all fields stored in the database
                  have to be present.
  """


def dbRateWineUser(user, wine, rating):
  """Store user's rating of wine in database
  
  Store the rating of the specified wine in the user's inventory.
  
  Args:
    UserInfo user: The UserInfo object of the user.
    LocationInventory wine: The LocationInventory object of the wine.
    int rating: The rating on a 1-5 scale.
  """
