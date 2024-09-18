from Alumno import Alumno

def main():
    Jesus = Alumno("Cruz Mendoza", "Jesus")
    print(Jesus)

    Jesus.saludar()
    Jesus.adios()
    
    rodrigo = Alumno("Rodrigo", "")
    rodrigo.saludar()
    rodrigo.adios()

if __name__ == "__main__":
    main()