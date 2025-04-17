def main():
    print("Welcome to the Planetary Weight Calculator!\n")
    
  
    earth_weight = float(input("Enter a weight on Earth: "))
    
  
    planet = input("Enter a planet: ")

    
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

   
    if planet in gravity_factors:
        planetary_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"\nThe equivalent weight on {planet}: {planetary_weight}")
    else:
        print("\nSorry, that planet is not recognized.")

if __name__ == "__main__":
    main()
