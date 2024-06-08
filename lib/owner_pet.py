class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(pet_type, str):
            raise TypeError("pet_type must be a string")
        if owner is not None and not isinstance(owner, Owner):
            raise TypeError("owner must be an instance of the Owner class")

        self.__name = name
        if pet_type.lower() in Pet.PET_TYPES:
            self.pet_type = pet_type.lower()
        else:
            raise ValueError(f"pet_type must be one of {Pet.PET_TYPES}")
        self.owner = owner
        Pet.all_instances(self)

    @classmethod
    def all_instances(cls, instance):
        cls.all.append(instance)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name

    def __repr__(self):
        owner_info = f", owned by {self.owner.name}" if self.owner else ""
        return f"{self.pet_type.capitalize()} named {self.name}{owner_info}"


class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner: {self.name}"
