# Simple Keylogger

## Description

This is a Python-based keylogger that captures and logs keystrokes to a file. It's designed to capture user input for purposes such as debugging, monitoring, or security analysis.

**Key Features**

* **Keystroke Logging:** Records all keys pressed by the user.
* **Timestamped Output:** Logs each keystroke with a corresponding date and time.
* **Configurable Output:** Keystrokes are saved to a text file (default: `keylog.txt`).
* **Threaded Operation:** Uses a separate thread for writing to the log file to minimize performance impact.
* **Error Handling:** Includes basic error handling for file operations.

**Important Note:**

* This keylogger is intended for ethical and legal use only.  
* Ensure you have explicit permission before using it on any system.  
* Unauthorized use of keyloggers is illegal and unethical.

## How to Use

1.  **Prerequisites**
    * Python 3.x
    * `pynput` library:

        ```bash
        pip install pynput
        ```

2.  **Installation**
    * Clone this repository or download the `key_log.py` script.

3.  **Configuration**
    * The following parameters can be configured within the `if __name__ == "__main__":` block of the `key_log.py` script:
        * `log_file_path`:  The name of the file where keystrokes will be logged (default: `keylog.txt`).
        * `report_interval_seconds`:  The frequency (in seconds) at which the keylogger writes the captured keystrokes to the log file (default: 60 seconds).

4.  **Running the Keylogger**
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the `key_log.py` file.
    * Execute the script:

        ```bash
        python key_log.py
        ```
    * The keylogger will start recording keystrokes.  
    * To stop the keylogger, press Ctrl+C in the terminal.

## Code Description

The keylogger is implemented using the following components:

* `Keylogger` Class
    * `__init__(self, log_file="keylog.txt", report_interval=60)`:  Initializes the Keylogger object with the log file path and report interval.
    * `on_press(self, key)`:  Called when a key is pressed.  Captures the key and timestamp.
    * `append_log(self, log_entry)`:  Appends the keystroke to the log data buffer.
    * `write_log(self)`:  Writes the buffered log data to the log file.
    * `report(self)`:  A function that runs in a separate thread to periodically write log data to the file.
    * `start(self)`:  Starts the keylogger and the reporting thread.

## Disclaimer

This keylogger should be used responsibly and only on systems with proper authorization. The developers assume no liability for misuse.
