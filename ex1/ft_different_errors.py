def garden_operations(s: str) -> None:
    num = int(s)
    num = 2 / num
    if (num == 2):
        open("missing.txt", "r")
    elif (num == 1):
        plant_heights = {"tree": 500, "rose": 25}
        _ = plant_heights['missing_plant']

def test_error_types() -> None:
    print("\nTesting ValueError...")
    try:
        garden_operations("abc")
    except ValueError as e:
        print("Caught ValueError:", e)

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("0")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("1")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    print("\nTesting KeyError...")
    try:
        garden_operations("2")
    except KeyError as e:
        print("Caught KeyError:", e)

    print("\nTesting multiple errors together...")
    try:
        garden_operations("abc")
        garden_operations("0")
        garden_operations("1")
        garden_operations("2")
    except:
        print("Caught an error, but program continues!")

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
