from abc import ABC, abstractmethod

class Musician(ABC):
    """
    Abstract class defining a musician.

    Attributes:
      name (str): The musician's name.

    Methods:
      get_instrument(): Returns the instrument played by the musician.
      play_solo(): Returns a solo performed by the musician.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

class Band:
    """
    Class representing a musical band.

    Attributes:
      name (str): The name of the band.
      members (list): A list of band members, each being an instance of the Musician class.
      instances (list): A list of Band instances.

    Methods:
      play_solos(): Returns a list of solos, each performed by a band member.
      to_list(): Returns a list of all Band instances.
    """

    instances = []

    def __init__(self, name, members=None):
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
    Class representing a bassist, extending the Musician class.

    Attributes:
      name (str): The bassist's name.

    Methods:
      get_instrument(): Returns 'bass'.
      play_solo(): Returns the solo performance by the bassist.
    """

    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):
    """
    Class representing a drummer, extending the Musician class.

    Attributes:
      name (str): The drummer's name.

    Methods:
      get_instrument(): Returns 'drums'.
      play_solo(): Returns the solo performance by the drummer.
    """

    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'

class Keyboardist(Musician):
    """
    Represents a keyboardist. Extends Musician class.

    Attributes:
      name (str): name of the keyboardist

    Methods:
      get_instrument(): returns 'keyboard'
      play_solo(): returns the keyboardist solo
    """

    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return 'keyboard'

    def play_solo(self):
        return 'keyboard solo'
