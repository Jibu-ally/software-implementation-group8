# Digital Thermometer

# Ask the user for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Determine temperature condition
if celsius <= 0:
    condition = "Freezing "
elif celsius < 10:
    condition = "Too Cold "
elif celsius < 20:
    condition = "Cold "
elif celsius < 30:
    condition = "Warm "
elif celsius < 40:
    condition = "Hot "
else:
    condition = "Very Hot "

# Display results
print(f"\nTemperature: {celsius}°C = {fahrenheit:.1f}°F")
print(f"Condition: {condition}")
