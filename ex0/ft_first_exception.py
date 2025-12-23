def check_temperature(temp_str: str):
    """Checks whether a temperatue is valid and gives feedback"""
    temp = 0
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return

    try:
        if temp < 0:
            raise ValueError(f"Error: {temp}°C is "
                             + "too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(f"Error: {temp}°C is "
                             + "too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
    except ValueError as error:
        print(error)


def test_temperature_input() -> None:
    """Tests the check_temperature fucntion"""
    print("=== Garden Temperature Checker ===\n")

    temps = [25, "abc", 100, -50]

    for temp in temps:
        print("Testing temperature: ", temp)
        check_temperature(temp)
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
