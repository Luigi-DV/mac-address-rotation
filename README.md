# Python | MAC Address Rotation

This Python script is designed to rotate the MAC address of the default network interface on your macOS system. It uses various system commands to achieve this.

## Prerequisites

- You need to have Python installed on your macOS system.
- You need to have administrative privileges to run `sudo` commands.
- This script assumes that you have already configured your system to allow running specific `sudo` commands without a password prompt. Be cautious when configuring `sudo` without password prompts, as it can pose a security risk. Only grant these permissions to specific commands that you absolutely trust and need to run without interaction.

## Usage

1. Open a terminal window.

2. Run the script by executing the following command:

   ```shell
   python mac_address_rotation.py
   ```

3. The script will prompt you to enter the time interval (in seconds) for running the commands. Enter the desired interval, or enter `0` to exit the script.

4. You will be prompted to enter your `sudo` password. Enter your password to allow the script to run `sudo` commands.

5. The script will execute the following steps in an infinite loop:

   - Turn off the default network interface.
   - Generate a new MAC address.
   - Turn on the default network interface.
   - Update the MAC address with the generated one.

6. The script will repeat these steps at the specified interval. To manually exit the script, you can press `Ctrl+C`.

## Script Details

- The script uses the `subprocess` module to run system commands.
- It first turns off the default network interface.
- It generates a new MAC address using the `openssl` and `sed` commands.
- It turns on the default network interface.
- It updates the MAC address with the generated one.
- The script repeats these steps based on the specified time interval.

## Troubleshooting

If you encounter any issues with `sudo` password prompts or command execution, please review your system's `sudo` configuration and ensure that the necessary permissions are granted for the commands used in the script.
