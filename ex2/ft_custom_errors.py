class GardenError(Exception):
    """Error for garden problems"""
    def __init__(self, message: str) -> None:
        """Constructor for GardenError"""
        super().__init__(message)


class PlantError(GardenError):
    """Error for plant problems"""
    def __init__(self, message: str) -> None:
        """Constructor for PlantError"""
        super().__init__(message)


class WaterError(GardenError):
    """Error for water problems"""
    def __init__(self, message: str) -> None:
        """Constructor for WaterError"""
        super().__init__(message)


def test_plant_error():
    """Raise a plant error"""
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


def test_water_error():
    """Raise a water error"""
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


def test_garden_errors():
    """Raise a water error"""
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print("Caught a garden error:", error)


def test_custom_errors():
    test_plant_error()
    test_water_error()
    test_garden_errors()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    test_custom_errors()

    print("\nAll custom error types work correctly!")
