## Spam Message Script using Python

This Python script allows users to send a predefined message multiple times through their keyboard using a hotkey. The script utilizes the `keyboard` module to simulate key presses and automates message sending. 

### Requirements
- Python 3.x
- `keyboard` module

### Installation

1. Install the `keyboard` module using pip:
   ```
   pip install keyboard
   ```

2. Save the script to a `.py` file.

### Features
- Input a message and the number of times it will be sent.
- The script listens for the hotkey `Shift + .` to start sending the message.
- Pressing the `Esc` key stops the script and allows the user to input a new message and repetition count.
- If the "1" key is pressed while sending the message, the script stops the current message sending process.

### Usage

1. Run the script in a Python environment.
2. You will be prompted to enter the message and the number of times to send it.
3. Press `Shift + .` to start the automatic message sending.
4. The message will be sent according to the number entered, and pressing `Esc` stops the execution.
5. After stopping, you can input a new message and repetition count.

### Code Overview

- **`spm()` function:** Automates the message sending process, allowing it to be sent a specified number of times.
- **Hotkey functionality:** The `Shift + .` combination triggers the message sending, and pressing `Esc` halts the script, allowing for new input.

### Note

- **Caution:** Ensure responsible use of this script, as sending multiple messages in quick succession could violate rules on certain platforms.
