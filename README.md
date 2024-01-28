# ExpertiseCar
-The ExpertiseCar application is a simple PyQt5-based GUI program that interacts with an SQLite database ('ExpertiseCar.db') and it helps to manage the expertise companies for cars. 
The application allows users to view data from three tables: "Cars_info," "Damages_info," and "Equipments." and provides information on the past of any car available in the market.

## Requirements
- Python 3.x
- PyQt5
- SQLite

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ExpertiseCarApp.git
   cd ExpertiseCarApp
Install the required dependencies: "pip install PyQt5"

## Usage
Run the application using the following command: "python GUI.py".
The main window will display information from the "Cars_info," "Damages_info," and "Equipments" tables.

## Database
The application connects to an SQLite database ('ExpertiseCar.db') containing the necessary tables. If you need to modify the database schema or add new functionalities, refer to the main.py file and the corresponding UI module.


## Customization
-UI modification If you want to make changes to the UI, refer to the Ui_MainWindow class in the UI module.

-Database Interaction: To handle additional database operations or modify existing ones, check the main.py file for database connection and cursor usage.

## Contributing
-Feel free to contribute by opening issues or submitting pull requests.

## License
-This project is licensed under the MIT License.
