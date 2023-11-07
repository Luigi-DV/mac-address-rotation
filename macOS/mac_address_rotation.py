import subprocess
import time
import getpass

while True:
    try:
        interval_seconds = int(input("Enter the time interval (in seconds) for running the commands (0 to exit): "))
        if interval_seconds == 0:
            break
        elif interval_seconds < 0:
            print("Please enter a positive interval.")
        else:
            sudo_password = getpass.getpass("Enter your sudo password: ")
            while True:
                # Turns off the default network interface
                command1 = ["networksetup", "-setairportpower", "en0", "off"]
                subprocess.run(["sudo", "-S", "-p", "", *command1], input=sudo_password, text=True, check=True)

                # Generates a new MAC and capture the result
                command2 = "openssl rand -hex 6 | sed 's/\\(..\\)/\\1:/g; s/.$//'"
                result = subprocess.run(command2, shell=True, check=True, capture_output=True, text=True)
                lladdr = result.stdout.strip()

                # Turns on the default network interface
                command3 = ["networksetup", "-setairportpower", "en0", "on"]
                subprocess.run(["sudo", "-S", "-p", "", *command3], input=sudo_password, text=True, check=True)

                # Update the lladdr in the fourth command
                command4 = [f"ifconfig en0 lladdr {lladdr}"]
                subprocess.run(["sudo", "-S", "-p", "", *command4], input=sudo_password, text=True, check=True)

                # Sleep for the specified interval
                time.sleep(interval_seconds)

    except KeyboardInterrupt:
        # Break the loop (e.g., Ctrl+C)
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")

print("Script terminated.")
