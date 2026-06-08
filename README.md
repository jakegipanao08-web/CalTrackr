# CalTrackr 📊

A simple and elegant calorie tracking application built with Python and CustomTkinter. Monitor your daily calorie intake with an intuitive GUI and real-time progress visualization.

## Features ✨

- **Daily Calorie Tracking**: Add and manage food items with their calorie values
- **Real-time Progress Bar**: Visual representation of calorie consumption with dynamic color coding
- **Customizable Daily Limit**: Set and adjust your daily calorie goal
- **Food List Management**: View all consumed items with easy-to-use delete functionality
- **Dynamic Color Coding**: Progress bar and text color change based on consumption levels
- **Clean UI**: Modern, minimalist interface built with CustomTkinter
- **Reset Functionality**: Clear all items and start fresh each day

## Tech Stack 🛠️

- **Language**: Python 3.x
- **GUI Framework**: CustomTkinter
- **Architecture**: Model-View-Controller (MVC) pattern
- **Design Pattern**: Strategy pattern for flexible color management

## Project Structure 📁

```
CalTrackr/
├── main.py           # Application entry point
├── models.py         # Data models (CalorieModel, FoodItem)
├── interfaces.py     # UI implementation (CalTrackrUI)
├── strategies.py     # Color strategy implementation
├── test_app.py       # Unit tests
└── README.md         # This file
```

## Installation 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jakegipanao08-web/CalTrackr.git
   cd CalTrackr
   ```

2. **Install dependencies**:
   ```bash
   pip install customtkinter
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage 📱

### Adding Food Items
1. Enter the food name in the "Food Name" field
2. (Optional) Enter the calorie count in the "Calories" field
3. Click "Add Food" to add to your daily tracker

### Managing Daily Limit
- The default daily limit is 2000 kcal
- Click on the limit value to edit and set your personal goal
- Press Enter or click away to save changes

### Viewing Progress
- The progress bar shows visual representation of calorie consumption
- Colors change dynamically:
  - **Green**: Under limit
  - **Yellow**: Approaching limit
  - **Red**: Over limit
- Remaining calories are displayed in real-time

### Deleting Items
- Click the "✕" button next to any food item to remove it

### Reset
- Click the "Reset" button to clear all items and start fresh

## Code Components 🏗️

### models.py
Contains the core data models:
- **FoodItem**: Dataclass representing a single food item with name and calories
- **CalorieModel**: Main model managing calorie tracking with methods for:
  - Adding/removing food items
  - Calculating total consumed and remaining calories
  - Resetting the tracker
  - Updating daily limit

### interfaces.py
Contains the UI implementation:
- **CalTrackrUI**: Main GUI class extending CustomTkinter
  - Header with title and close button
  - Stats section showing consumed/remaining calories and progress bar
  - Input section for adding new food items
  - Scrollable food list
  - Footer with reset button

### strategies.py
Implements the Strategy pattern:
- **LimitBasedColorStrategy**: Determines progress bar and text colors based on consumption ratio

### main.py
Application entry point that:
- Initializes the data model
- Sets up the color strategy
- Creates and runs the UI

## Testing 🧪

Run the included tests:
```bash
python test_app.py
```

## Color Coding System 🎨

The application uses dynamic color coding to provide visual feedback:
- **Progress Bar**: Changes color based on percentage of limit consumed
- **Remaining Calories**: Turns red when negative (over limit)

## Architecture 🏛️

This project follows design principles:
- **MVC Pattern**: Separation of concerns between data, presentation, and logic
- **Strategy Pattern**: Flexible color strategy implementation
- **Single Responsibility**: Each module handles one aspect of functionality

## Future Enhancements 💡

- Data persistence (save to database)
- Meal history tracking
- Nutrition breakdown (protein, carbs, fats)
- Barcode scanning for food lookup
- Dark mode theme option
- Export daily/weekly reports

## License 📄

This project is open source and available for personal and educational use.

## Author 👤

**jakegipanao08-web**

---

**Happy Tracking!** 🎯 Keep your calorie intake in check with CalTrackr.
