def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: ").strip())
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")