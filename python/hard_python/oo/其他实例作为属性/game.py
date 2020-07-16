import dog

house = dog.DogHouse('9527')
pd = dog.PetDog('小可爱', 0.2, 1, 988, house)
print(pd.price)
pd.bark()