import customtkinter as ctk
from models import CalorieModel, FoodItem
from interfaces import CalTrackrUI
from strategies import LimitBasedColorStrategy


def main():
    # Set appearance
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # 1. Initialize Data Model with pre-loaded data from Screenshot 1
    # (Total 2040 kcal to demonstrate the Red Bar from Screenshot 2)
    model = CalorieModel(limit=2000)


    # 2. Initialize Strategy
    color_strategy = LimitBasedColorStrategy()

    # 3. Initialize UI with dependencies
    app = CalTrackrUI(model, color_strategy)

    # 4. Run Loop
    app.mainloop()


if __name__ == "__main__":
    main()