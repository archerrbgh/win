"""User login preprocessing module
"""


def inputCreateUser(user):
  """Preprocess new user info
  
  Args:
    dict user: Dict representing all fields of a UserInfo object
    
  Return:
    UserInfo: The newly created user object
  """


def inputLogin(username, password):
  """Preprocess login information
  
  Args:
    string username: The potential username
    string password: The potential password
    
  Return:
    UserInfo: UserInfo object of the logged in user
  """
  

def inputLogout(user):
  """Preprocess logout
  
  Args:
    UserInfo user: UserInfo object of the user being logged out.
  """
  
  
def inputEditUser(user, attr):
  """Preprocess updating user profile
  
  Args:
    UserInfo user: The UserInfo object of the user being modified.
    dict attr: A dict specifying user attributes, of the form {email:*, DOB:*, etc}. Not every
               field stored in the database has to be present.
  """
