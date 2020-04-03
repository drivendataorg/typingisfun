from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class SpeciesEnum(Enum):
    DOG = "dog"
    CAT = "cat"
    LIZARD = "lizard"


class FoodEnum(Enum):
    FISH = "fish"
    MICE = "mice"
    STEAK = "steak"
    LASAGNA = "lasagna"
    WORMS = "worms"


class Pet(BaseModel):
    name : str
    weight : float
    species : SpeciesEnum
    favorite_foods : List[FoodEnum]
    nickname : Optional[str]


dog = Pet(name="Priscilla", weight=25, species="dog", favorite_foods=["steak"])
cat = Pet(name="Cameron", nickname="Cam", weight=7, species="cat", favorite_foods=["fish", "mice", "lasagna"])
lizard = Pet(name="Rocky", nickname="The Rock", species="frog")
