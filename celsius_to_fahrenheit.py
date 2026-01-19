import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    if len(sys.argv) > 1:
        celsius = float(sys.argv[1])
    else:
        celsius = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(celsius))

if __name__=="__main__":
   main()


