# Trello to Excel

This Python script allows you to export cards from a selected Trello list into an Excel file. It uses the Trello API to fetch data and pandas to handle the export.

## Features
- Fetches all lists from a specified Trello board.
- Allows the user to select a list.
- Exports cards (with name, description, due date, and labels) to an Excel file.

## Requirements
- Python 3.x
- A Trello account and API credentials (API key and token).

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/lelocrow/TrelloToExcel.git
cd TrelloToExcel
```

### 2. Install Dependencies
Make sure you have `requests` and `pandas` installed. You can install them using pip:
```bash
pip install requests pandas openpyxl
```

### 3. Get Your Trello API Credentials
- Visit the [Trello Developer API Keys](https://trello.com/app-key) page.
- Copy your **API Key** and generate a **Token**.

### 4. Configure the Script
- Open the script file in your editor.
- Replace the placeholders with your credentials and board ID:
  ```python
  api_key = 'YourApiKey'
  token = 'YourApiToken'
  board_id = 'YourBoardID'
  ```

## Usage

1. Run the script:
   ```bash
   python script_name.py
   ```

2. The script will display all available lists in the specified board.  
   Example:
   ```
   Lists available:
   1. To Do
   2. In Progress
   3. Done
   ```

3. Enter the number corresponding to the list you want to export.

4. The script will create an Excel file named `<list_name>_trello_list.xlsx` in the current directory.

## Example Output

| Card Name     | Description           | Due Date   | Labels     |
|---------------|-----------------------|------------|------------|
| Task 1        | First task details    | 2024-12-31 | High, Urgent |
| Task 2        | Second task details   | 2025-01-15 | Medium      |

## Notes
- Ensure your board and lists have public access or your API credentials have sufficient permissions.
- The Excel file will overwrite if a file with the same name already exists.

## Troubleshooting
- If you encounter an error while fetching lists or cards, check your API credentials and board ID.
- If the script crashes while exporting, ensure you have write permissions in the current directory.

## License
This project is licensed under the MIT License. Feel free to use and modify it.
