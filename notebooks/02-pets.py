from typingisfun.pets import Pet


cat = Pet(name="Cameron", nickname="Cam", weight=7, species="cat", favorite_foods=["fish", "mice", "lasagna"])
cat.weight
cat.favorite_foods


dog_dict = {
    "name": "Priscilla",
    "weight": 25,
    "species": "dog",
    "favorite_foods": ["steak"],
}
dog = Pet(**dog_dict)
dog.name

lizard = Pet(name="Rocky", nickname="The Rock", species="frog")
