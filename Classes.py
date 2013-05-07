"""All classes used by System. Identical to database table counterparts.
   Check Database Schema for additional details.
"""

class UserInfo:
  def __init__(self, 
               userID = None, 
               emailAddress = None, 
               password = None, 
               name = None,
               location = None,
               dateOfBirth = None,
               imagePath = None):

    self.userID = userID
    self.emailAddress = emailAddress
    self.password = password
    self.name = name
    self.location = location
    self.dateOfBirth = dateOfBirth
    self.imagePath = imagePath


class LocationMap:
  def __init__(self,
               locationID = None,
               lm_userID = None,
               locationName = None,
               timeCreated = None,
               imagePath = None):

    self.locationID = locationID
    self.lm_userID = lm_userID
    self.locationName = locationName
    self.timeCreated = timeCreated
    self.imagePath = imagePath


class LocationHistory:
  def __init__(self,
               lh_locationID = None,
               lh_wineID = None,
               timestamp = None,
               eventTag = None):
  
    self.lh_locationID = lh_locationID
    self.lh_wineID = lh_wineID
    self.timestamp = timestamp
    self.eventTag = eventTag


class LocationInventory:
  """A wine in the user's inventory
  """
  def __init__(self,
               li_locationID = None,
               li_wineID = None,
               quantity = None,
               personalStarRating = None,
               isWishlist = None,
               bitter = None,
               sweet = None,
               sour = None,
               salty = None,
               chemical = None,
               pungent = None,
               oxidized = None,
               microbiological = None,
               floral = None,
               spicy = None,
               fruity = None,
               vegetative = None,
               nutty = None,
               caramelized = None,
               woody = None,
               earthy = None):

    self.li_locationID = li_locationID
    self.li_wineID = li_wineID
    self.quantity = quantity
    self.personalStarRating = personalStarRating
    self.isWishlist = isWishlist
    self.bitter = bitter
    self.sweet = sweet
    self.sour = sour
    self.salty = salty
    self.chemical = chemical
    self.pungent = pungent
    self.oxidized = oxidized
    self.microbiological = microbiological
    self.floral = floral
    self.spicy = spicy
    self.fruity = fruity
    self.vegetative = vegetative
    self.nutty = nutty
    self.caramelized = caramelized
    self.woody = woody
    self.earthy = earthy


class Wine:
  """A wine in the global inventory
  """
  def __init__(self,
               wineID = None,
               wineName = None,
               varietal_blend = None,
               winery = None,
               wineType = None,
               vintage = None,
               region = None,
               clusterID = None,
               CSO = None,
               tags = None,
               description = None,
               averageStarRating = None,
               imagePath = None,
               barcode = None,
               bitter = None,
               sweet = None,
               sour = None,
               salty = None,
               chemical = None,
               pungent = None,
               oxidized = None,
               microbiological = None,
               floral = None,
               spicy = None,
               fruity = None,
               vegetative = None,
               nutty = None,
               caramelized = None,
               woody = None,
               earthy = None):

    self.wineID = wineID
    self.wineName = wineName
    self.varietal_blend = varietal_blend
    self.winery = winery
    self.wineType = wineType
    self.vintage = vintage
    self.region = region
    self.clusterID = clusterID
    self.CSO = CSO
    self.tags = tags
    self.description = description
    self.averageStarRating = averageStarRating
    self.imagePath = imagePath
    self.barcode = barcode
    self.bitter = bitter
    self.sweet = sweet
    self.sour = sour
    self.salty = salty
    self.chemical = chemical
    self.pungent = pungent
    self.oxidized = oxidized
    self.microbiological = microbiological
    self.floral = floral
    self.spicy = spicy
    self.fruity = fruity
    self.vegetative = vegetative
    self.nutty = nutty
    self.caramelized = caramelized
    self.woody = woody
    self.earthy = earthy


class Recommender:
  def __init__(self,
               recommenderID = None,
               r_userID = None,
               channelName = None,
               timeCreated = None,
               seedBitter = None,
               seedSweet = None,
               seedSour = None,
               seedSalty = None,
               seedChemical = None,
               seedPungent = None,
               seedOxidized = None,
               seedMicrobiological = None,
               seedFloral = None,
               seedSpicy = None,
               seedFruity = None,
               seedVegetative = None,
               seedNutty = None,
               seedCaramelized = None,
               seedWoody = None,
               seedEarthy = None):

    self.recommenderID = recommenderID
    self.r_userID = r_userID
    self.channelName = channelName
    self.timeCreated = timeCreated
    self.seedBitter = seedBitter
    self.seedSweet = seedSweet
    self.seedSour = seedSour
    self.seedSalty = seedSalty
    self.seedChemical = seedChemical
    self.seedPungent = seedPungent
    self.seedOxidized = seedOxidized
    self.seedMicrobiological = seedMicrobiological
    self.seedFloral = seedFloral
    self.seedSpicy = seedSpicy
    self.seedFruity = seedFruity
    self.seedVegetative = seedVegetative
    self.seedNutty = seedNutty
    self.seedCaramelized = seedCaramelized
    self.seedWoody = seedWoody
    self.seedEarthy = seedEarthy


class RecommenderHistory:
  def __init__(self,
               rh_recommenderID = None,
               rh_wineID = None,
               timestamp = None,
               isSeedBottle = None):

    self.rh_recommenderID = rh_recommenderID
    self.rh_wineID = rh_wineID
    self.timestamp = timestamp
    self.isSeedBottle = isSeedBottle
