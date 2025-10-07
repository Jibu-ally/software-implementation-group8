def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def main():
    print("🌡  Welcome to the Digital Thermometer 🌡")
    celsius = float(input("Enter temperature in degrees Celsius: "))

    if celsius > 25:
        print("It's a hot day.")
    elif celsius < 7:
        print("It's a cold day.")
    else:
        print("The weather is moderate.")

    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"The equivalent temperature in Fahrenheit is: {fahrenheit:.2f}°F")


if __name__ == "_main_":
    main()
    