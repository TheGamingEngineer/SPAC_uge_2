import os

log=input("Enter log-file as .txt:")

## prøver at åbne  filen. 
try:
    log_history=open(log,"r")
except FileNotFoundError as e:
    print(f"File not found: {e}. Either the filename has been given erroneously, path to file has not been provided when needed, or file simply does not exist!")
except PermissionError as e:
    print(f"Permission denied: {e}. Please change permissions of the file and try again.")
except IsADirectoryError as e:
    print(f"Expected a file but found a directory: {e}. This script only handles text-files.")
except OSError as e:
    print(f"OS error: {e}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}.")

## udtrækker logfilens navn for at indikere sorteringsfilerne
log_name=log.split(".")[0]

## laver en ny warnings logfil
if os.path.exists(log_name + "_warnings.txt"):
    os.remove(log_name + "_warnings.txt")
log_warnings=open(log_name + "_warnings.txt","a")

## laver en ny errors logfil
if os.path.exists(log_name + "_errors.txt"):
    os.remove(log_name + "_errors.txt")
log_errors=open(log_name + "_errors.txt","a")

## laver en ny success logfil
if os.path.exists(log_name + "_successes.txt"):
    os.remove(log_name + "_successes.txt")
log_success=open(log_name + "_successes.txt","a")

## laver en ny logfil med andre meddelelser. 
if os.path.exists(log_name + "_info-logs.txt"):
    os.remove(log_name + "_info-logs.txt")
log_info=open(log_name + "_info-logs.txt","a")

## gennemgår logfilen og sortere baserert på meddelelsestypen 
for line in log_history:
    if "WARNING" in line:
        log_warnings.write(line)
    elif "ERROR" in line:
        log_errors.write(line)
    elif "SUCCESS" in line:
        log_success.write(line)
    else:
        log_info.write(line)
        
#### lukker alle åbne filer. 
log_history.close()
log_warnings.close()
print(log_name + "_warnings.txt successfully created!")
log_errors.close()
print(log_name + "_errors.txt successfully created!")
log_success.close()
print(log_name + "_successes.txt successfully created!")
log_info.close()
print(log_name + "_info-logs.txt successfully created!")

print("Job is done.")        