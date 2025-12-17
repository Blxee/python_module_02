def check_temperature(temp_str: str) -> None:
    """Checks whether a temperatue is valid and gives feedback"""
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except:
        print(f"Error: '{temp_str}' is not a valid number")

def test_temperature_input() -> None:
    """Tests the check_temperature fucntion"""
    temps = [25, "abc", 100, -50]

    for temp in temps:
        print("Testing temperature: ", temp)
        check_temperature(temp)

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()
