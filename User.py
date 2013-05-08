"""User account module
"""


def createUser(user):
  """Process new user info before adding to database
  
  Check if username and password aren't already taken. If not, create
  a new user.
  
  Args:
    dict user: Dict representing the UserInfo object of the potential new user
    
  Return:
    UserInfo: The newly created user object
  """


def login(username, password):
  """Login user if information is valid
  
  Args:
    string username: The potential username
    string password: The potential password
    
  Return:
    UserInfo: UserInfo object of the logged in user
  """
  

def logout():
  """Logout user
  
  Args:
    UserInfo user: UserInfo object of the user being logged out.
  """
  

def editUser(user):
  """Call DataAccess layer to update user profile in database with attributes
  
  Change information stored about the user in the database to match relevant information
  passed in attr.
  
  Args:
    UserInfo user: The UserInfo object of the user being modified.
    dict attr: A dict specifying user attributes, of the form {email:*, DOB:*, etc}. Not every
               field stored in the database has to be present.
  """
