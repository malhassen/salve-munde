class Pokemon:
    def main(self):
        pokemon = self.get_type()
        print(f"{self.return_starter(pokemon)} is {pokemon.type} type")

    def get_type(self):
        pokemon =  Pokemon()
        pokemon.type = input("Fire, Water, or Grass?  ").strip().lower()
        return pokemon
    

    def return_starter(self, pokemon):
        while True:
              if pokemon.type == "fire":
                    return "Charmander"
              elif pokemon.type == "water":
                    return "Squirtle"
              elif pokemon.type == "grass":
                    return "Bulbasaur"
              else:
                print("Invalid type. Starters can only be Fire, Water, or Grass")
                pokemon.type = input("Fire, Water, or Grass? ").strip().lower()
                

            

if __name__ == "__main__":
    p = Pokemon()
    p.main()
