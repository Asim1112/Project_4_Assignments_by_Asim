C: int = 299792458

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    calculate_energy: float = mass_in_kg * (C ** 2)

    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(calculate_energy) + " joules of energy!")


if __name__ == "__main__":
    main()
