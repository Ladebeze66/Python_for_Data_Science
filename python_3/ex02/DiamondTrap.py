from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Your docstring for Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        # Corriger l'attribut initial 'hairs' -> 'hair'
        if 'hairs' in self.__dict__:
            self.__dict__['hair'] = self.__dict__.pop('hairs')

    @property
    def eyes(self):
        """Your docstring for Method"""
        return self.__dict__.get('eyes', 'brown')

    @eyes.setter
    def eyes(self, value):
        """Your docstring for Method"""
        self.__dict__['eyes'] = value

    @property
    def hairs(self):
        """Your docstring for Method"""
        # Retourne 'hair' ou 'hairs' selon ce qui existe
        return self.__dict__.get('hairs', self.__dict__.get('hair', 'dark'))

    @hairs.setter
    def hairs(self, value):
        """Your docstring for Method"""
        # Supprimer 'hair' et créer 'hairs'
        if 'hair' in self.__dict__:
            del self.__dict__['hair']
        self.__dict__['hairs'] = value

    def get_eyes(self):
        """Your docstring for Method"""
        return self.eyes

    def set_eyes(self, value):
        """Your docstring for Method"""
        self.eyes = value

    def get_hairs(self):
        """Your docstring for Method"""
        return self.hairs

    def set_hairs(self, value):
        """Your docstring for Method"""
        self.hairs = value
