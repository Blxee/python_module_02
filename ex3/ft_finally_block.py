class Plant:
    def __init__(self, name: str) -> None:
        self.name = name

    def water(self):
        print("Watering", self.name)

class PlantError(Exception):
    def __init__(self, value) -> None:
        message = f"Cannot water {value} - invalid plant!"
        super().__init__(message)

def water_plants(plant_list: list) -> None:
    print("Opening watering system")

    success = True
    try:
        for plant in plant_list:
            if type(plant) is not Plant:
                raise PlantError(plant)
            plant.water()
    except PlantError as e:
        print("Error:", e)
        success = False
    finally:
        print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!")

def test_watering_system() -> None:
    print("Testing normal watering...")
    plant_list = [Plant("tomato"), Plant("lettuce"), Plant("carrots")]
    water_plants(plant_list)

    print("\nTesting with error...")
    plant_list = [Plant("tomato"), None]    
    water_plants(plant_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
