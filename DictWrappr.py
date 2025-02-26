
# Constants for log file configuration
LOG_FILE = "failed_reads.log"  # Name of the log file
MAX_LOG_LINES = 200            # Maximum number of lines the log file should contain

class DictWrapper:
    """
    A wrapper class for a dictionary that provides attribute-style access
    and logs failed key accesses.
    """
    def __init__(self, dic):
        """
        Initialize the DictWrapper with the provided dictionary and
        prepare the log file.

        Args:
            dic (dict): The dictionary to wrap.
        """
        self._dic = dic
        self._initialize_log()

    def __getattr__(self, key):
        """
        Retrieve the value associated with 'key'. If the key does not exist,
        return an empty string and log the failed access.

        Args:
            key (str): The key to look up in the dictionary.

        Returns:
            The value associated with 'key' if it exists; otherwise, an empty string.
        """
        value = self._dic.get(key, "")
        if value == "":
            self._log_failure(key)
        return value

    
    def _initialize_log(self):
        """
        Initialize the log file by clearing its contents at the start of a new run.
        """
        """Attempts to open the log file, handling permission errors."""
        try:
            with open(LOG_FILE, "w") as log_file:
                x=1
        except PermissionError:
            print(f"Permission denied: Cannot write to '{log_file}'.")
            
# =============================================================================
#    
#         with open(LOG_FILE, "w") as log_file:
#             pass  # Create or clear the log file
# 
# =============================================================================
    def _log_failure(self, key):
        """
        Log the details of a failed key access attempt, including the timestamp,
        key name, filename, and line number.

        Args:
            key (str): The key that was not found in the dictionary.
        """
        frame = inspect.currentframe().f_back.f_back  # Get the caller's frame
        dt = datetime.now().strftime("%a %H:%M")
        base_filename = os.path.basename(frame.f_code.co_filename)
        line_number = frame.f_lineno
        log_entry = f"-->> {key} <<-  LINE:{line_number} {base_filename} {dt}\n"
        # for full file path instead use
        # log_entry = f"{dt}: -->> {key} <<--\n     LINE:{frame.f_lineno} {frame.f_code.co_filename}\n" 
        with open(LOG_FILE, "a") as log_file:
            log_file.write(log_entry)
            log_file.flush()  # Forces the OS to write the data immediately
        self._truncate_log()

    def _truncate_log(self):
        """
        Ensure the log file does not exceed MAX_LOG_LINES by retaining only the
        most recent entries.
        """
        with open(LOG_FILE, "r") as log_file:
            lines = log_file.readlines()
        if len(lines) > MAX_LOG_LINES:
            with open(LOG_FILE, "w") as log_file:
                log_file.writelines(lines[-MAX_LOG_LINES:])
                log_file.flush()  # Forces the OS to write the data immediately

def glog(pause=True):
    """
    Display the number of entries in the log file and its contents if there are any.
    Optionally pause for user input after displaying the log.

    Args:
        pause (bool): If True, wait for user input after displaying the log.
    """
    if not os.path.exists(LOG_FILE):
        return  # Log file does not exist
    with open(LOG_FILE, "r") as log_file:
        lines = log_file.readlines()
    line_count = len(lines)
    if line_count == 0:
        return  # No failures logged
    else:
        l.p(f'ERROR: {line_count}) Failed Reads DictWrapper ')
        print('.............................................................')
        print(f'..({line_count}) Failed Reads DictWrapper..eg: ~g = DictWrapper(dic)~')
        print('.............................................................')
        # Display the number of log entries and their contents
        for line in lines:
            print(f'\n{line}') # Process each log entry as needed
        print('.............................................................\n')
        if pause:
            print(f"......ERROR: {line_count} use ~g.field~ ~glog(1)~ or ~glog(0)~..........")  
            print('................. No quotes on field name! ..................\n')
# # Example usage:
# data = {'existing_key': 'value'}
# g = DictWrapper(data)
