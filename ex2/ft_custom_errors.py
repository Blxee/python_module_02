class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class  WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def yeet_garden():
    raise GardenError("The garden is no more o7")


def yeet_plant():
    raise PlantError("The tomato plant is wilting!")


def yeet_water():
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        yeet_plant()
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        yeet_water()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        yeet_plant()
    except GardenError as e:
        print(f"Caught a garden error:", e)

    try:
        yeet_water()
    except GardenError as e:
        print(f"Caught a garden error:", e)

    print("\nAll custom error types work correctly!")
