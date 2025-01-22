# Automation Script for Printing Incoming Invoices

This program is designed for automatically downloading and printing PDF files from a specified list stored in JSON format. The script also logs which files have been successfully printed to prevent duplicate printing. It was created for a private client and is published with prior consent.

## Project Structure

- `task_scheduler.py`: A scheduler that repeatedly runs the main script `main.py` at predefined intervals. It ensures full automation of print tasks.
- `main.py`: The main script that processes the file list, downloads PDF files, and sends them for printing.
- `config.py`: Contains configuration variables such as URLs for file lists, the location of PDF files for printing, etc. It needs to be set according to the user’s requirements.
- `file_operations.py`: Contains functions for file handling.
- `printer.py`: Contains functions for sending files to the printer and logging printed files.
- `printed_files.json`: A JSON file that logs files that have already been printed. Serves as a log for the script.
- `order_list.json`: A JSON file containing a list of PDF files to be printed. In a real-world deployment, this file resides on a server.

## Usage

### Prerequisites

- Python 3.x
- `requests` library

### Setup

1. Clone this repository to your local machine (requires **Git**):
   ```bash
   git clone https://github.com/liborgit/davmo-print-script.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install requests
   ```

4. Edit the `config.py` file according to your requirements:
   - `MAIN_PY_PATH`: Specify the path to the `main.py` file. Important for using `task_scheduler.py`.
   - `INTERVAL`: Interval in seconds at which `main.py` will be rerun. Adjust as needed.
   - `LIST_URL`: The URL of the external JSON file containing the list of PDF files to print.
   - `BASE_URL`: The base URL of the external directory where the PDF files (orders) are stored for printing.
   - `DOWNLOAD_FOLDER`: Folder where PDF files will be downloaded before printing.
   - `LOG_FILE`: Name of the file logging printed files.

## Execution

For automatic monitoring of new files for downloading and printing, you need to run the `task_scheduler.py` script. This script ensures scheduled execution of the main script `main.py` at regular intervals defined in the configuration file `config.py`.

### Execution Steps:
1. Open a terminal or command prompt.
2. Navigate to the project’s source code directory `src/`.
3. Run the scheduler `task_scheduler.py`. This command will start the scheduler, which will periodically check for new files to download and print:
   ```bash
   python task_scheduler.py
   ```

### After Running the Scheduler:

The program will automatically execute the `main.py` script at regular intervals (e.g., every 30 minutes). During each run, the script will process and compare the file list, download new PDF files, and send them for printing. The scheduler will log runtime information to the console.

To stop the scheduler, you can safely terminate the program by pressing **Ctrl + C**.

### How It Works

- **File List Loading**: The script loads the list of PDF files from the URL defined in `config.py`.
- **Printed Files Check**: The script checks which files have already been printed and only prints new files.
- **Download and Print**: Each new file is downloaded and then sent to the printer.
- **Logging**: After successful printing, the file is logged in `printed_files.json` to prevent duplicate printing.

### Limitations

- The script is designed for Windows systems and uses the `os.startfile` function for sending files to the printer.
- For printing files, the system must have a default application installed that supports the print command (e.g., Adobe Reader for PDFs).
