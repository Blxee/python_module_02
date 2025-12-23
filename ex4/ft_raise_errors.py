def check_plant_health(plant_name: str,
                       water_level: int, sunlight_hours: int) -> str:
    """Checks the plant's health, raises appropriate errors"""

    if len(plant_name) == 0:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError("Sunlight hours "
                         + f"{sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Tests for the check_plant_health function"""

    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        value = check_plant_health("tomato", 5, 8)
        print(value)
    except ValueError as error:
        print("Error:", error)

    print("\nTesting empty plant name...")
    try:
        value = check_plant_health("", 5, 8)
        print(value)
    except ValueError as error:
        print("Error:", error)

    print("\nTesting bad water level...")
    try:
        value = check_plant_health("tomato", 15, 8)
        print(value)
    except ValueError as error:
        print("Error:", error)

    print("\nTesting bad sunlight hours...")
    try:
        value = check_plant_health("tomato", 5, 0)
        print(value)
    except ValueError as error:
        print("Error:", error)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
