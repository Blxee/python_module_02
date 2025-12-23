def garden_operations(s: str) -> None:
    """Try different errors according to the argument"""
    match s:
        case "value":
            _ = int("abc")
        case "zero":
            _ = 5 / 0
        case "file":
            _ = open("missing.txt", "r")
        case "key":
            plant_heights = {"tree": 500, "rose": 25}
            _ = plant_heights['missing_plant']


def test_error_types() -> None:
    """Test error types duh ;-;"""

    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print("Caught ValueError:", e)

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print("Caught KeyError:", e)

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
        garden_operations("file")
        garden_operations("key")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
