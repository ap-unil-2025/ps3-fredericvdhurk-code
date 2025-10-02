def celsius_to_fahrenheit(celsius_temp):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    return (celsius_temp * 9/5) + 32 

    
    pass

def fahrenheit_to_celsius(fahrenheit_temp):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    return (fahrenheit_temp - 32) * 5/9

    
    pass

def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
# enter temperature value and unit
    try:
        temp_value = float(input("Enter the temperature value: "))
        temp_unit = input("Enter the current unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        
# return converted values
        if temp_unit == "C":
            temp_converted = round(celsius_to_fahrenheit(temp_value), 2)
            print(f"{temp_value:.2f}°C is {temp_converted:.2f}°F")
        elif temp_unit == "F":
            temp_converted = round(fahrenheit_to_celsius(temp_value), 2)
            print(f"{temp_value:.2f}°F is {temp_converted:.2f}°C")
            
# invalid unit case
        else:
            print("Invalid unit input. Please enter 'C' or 'F'.")

# invalid value case
    except ValueError:
        print("Invalid input value. Please enter a numeric value for temperature.")

        
    pass

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    # Run interactive converter
    temperature_converter()