from abc import ABC, abstractclassmethod

class Musician(ABC):
  """
  An abstract class to represent a musician

  Attributes:
    name (str): name of the musician
  
  Methods:
    get_instrument(): returns the musicians instrument
    play_solo(): returns the musicians solo
  """

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f'My name is {self.name} and I play {self.get_instrument()}'
  
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'
  
  @abstractclassmethod
  def get_instrument():
    pass

  @abstractclassmethod
  def play_solo():
    pass

class Band:
  """
  Represents a band

  Attributes:
    name (str): name of the band
    members (list): list of members of the band, each member should be of the Musician class
    instances (list): list of the number of instances of Band
  
  Methods:
    play_solos(): returns a list of the solo attribute for each member of the band
    to_list(): returns a list of the number of instances of Band
  """

  instances = []

  def __init__(self, name, members = None):
    self.name = name
    self.members = members or []
    self.instances.append(self)

  def __str__(self):
    return self.name
  
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'

  def play_solos(self):
    return [member.play_solo() for member in self.members]
  
  @classmethod
  def to_list(cls):
    return cls.instances
    
class Guitarist(Musician):
  """
  Represents a guitarist. Extends Musician class.

  Attributes:
    name (str): name of the guitarist
  
  Methods:
    get_instrument(): returns 'guitar'
    play_solo(): returns the guitarist solo
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'guitar'
  
  def play_solo(self):
    return 'face melting guitar solo'

class Bassist(Musician):
  """
  Represents a bassist. Extends Musician class.

  Attributes:
    name (str): name of the bassist
  
  Methods:
    get_instrument(): returns 'bass'
    play_solo(): returns the bassist solo
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'bass'
  
  def play_solo(self):
    return 'bom bom buh bom'

class Drummer(Musician):
  """
  Represents a drummer. Extends Musician class.

  Attributes:
    name (str): name of the drummer
  
  Methods:
    get_instrument(): returns 'drums'
    play_solo(): returns the drummer solo
  """

  def __init__(self, name):
    super().__init__(name)
  
  def get_instrument(self):
    return 'drums'
  
  def play_solo(self):
    return 'rattle boom crash'

class Keyboardist(Musician):
  
  def __init__(self, name):
    super().__init__(name)