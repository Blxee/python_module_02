class GardenError(Exception):
    """Error for garden problems"""

    pass


class PlantError(GardenError):
    """Error for plant problems"""

    pass


class WaterError(GardenError):
    """Error for water problems"""

    pass


class SunlightError(GardenError):
    """Error for water problems"""

    pass


class Plant:
    """Basic blueprint for a plant"""

    def __init__(self,
                 name: str,
                 water_level: int,
                 sunlight_hours: int) -> None:
        """Constructor for the plant"""
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def water(self, amount: int):
        """Water this plant"""
        self.water_level += amount
        print("Watering", self.name)

    @staticmethod
    def check_health(plant) -> str:
        """Checks the plant's health, raises appropriate errors"""
        name, water, sun = plant.name, plant.water_level, plant.sunlight_hours

        if len(name) == 0:
            raise PlantError("Plant name cannot be empty!")

        if water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")
        elif water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")

        if sun < 2:
            raise SunlightError(f"Sunlight hours {sun} is too low (min 2)")
        elif sun > 12:
            raise SunlightError(f"Sunlight hours {sun} is too high (max 12)")

        return f"{name}: healthy (water: {water}, sun: {sun})"


class GardenManager:
    """Class to manage garden of different plants"""
    amount_per_water: int = 4

    def __init__(self) -> None:
        self.plant_list = []
        self.water_in_tank = 10

    def add_plant(self, plant: Plant) -> None:
        """Add a new plant to be managed"""
        try:
            Plant.check_health(plant)
            self.plant_list.append(plant)
            print(f"Added {plant.name} successfully")
        except GardenError as error:
            print("Error adding plant:", error)

    def water_plants(self, show=True) -> None:
        """Water all the plants"""
        if show:
            print("Opening watering system")

        try:
            for plant in self.plant_list:
                if type(plant) is not Plant:
                    raise PlantError(plant)

                if self.water_in_tank < self.amount_per_water:
                    raise GardenError("Not enough water in tank")

                plant.water(self.amount_per_water)
                self.water_in_tank -= self.amount_per_water

        except PlantError as e:
            print("Error:", e)

        except GardenError as error:
            print("Caught GardenError:", error)

        finally:
            if show:
                print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Checks the plant's health, raises appropriate errors"""

        for plant in self.plant_list:
            try:
                print(Plant.check_health(plant))
            except GardenError as error:
                print(f"Error checking {plant.name}:", error)


def test_garden_management():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("\nAdding plants to garden...")

    tomato = Plant("tomato", 1, 8)
    lettuce = Plant("lettuce", 10, 8)
    invalid_plant = Plant("", 7, 9)

    manager.add_plant(tomato)
    manager.add_plant(lettuce)
    manager.add_plant(invalid_plant)

    print("\nWatering plants...")
    manager.plant_list[1].water_level += 1
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.water_plants(False)
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
