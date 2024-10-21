# Tomarket App Airdrop Clicker Bot

This Python script automates mouse clicking for the Tomarket App Airdrop on Telegram. It identifies specific color regions on the screen and clicks on them automatically. This is particularly useful for automating repetitive clicking tasks in the airdrop process.

## Preview

![DemoTomarketBot](https://github.com/user-attachments/assets/89115baf-0c99-4351-86c3-15ad1e8f5471)

## Features

- **Automated Mouse Clicking**: The program will automatically click on a target color that you specify.
- **Customizable Region**: You can adjust the region of the screen that the program monitors for clicks.
- **Start/Stop Control**: Use keyboard keys to start (`s`) and stop (`p`) the clicking.
- **Screen Compatibility**: Default region set for 1080p resolution, but you can modify the region coordinates to fit different screen sizes.

## Prerequisites

Before running this program, ensure you have the following libraries installed:

- `opencv-python`
- `numpy`
- `pyautogui`
- `pynput`

You can install them using pip:

```bash
pip install opencv-python numpy pyautogui pynput
```

## How to Use

1. **Clone the repository** or download the Python script:

   ```bash
   git clone https://github.com/ammar2350/Tomarket-App-Clicker.git
   ```

2. **Edit the region settings** (if necessary):

   The default screen region is set for a 1080p resolution. If your screen has a different resolution, update the `region` variable inside the script:

   ```python
   region = (720, 155, 475, 620)
   ```

   Adjust the `region` values according to your screen size:
   - `(x, y, width, height)` corresponds to the top-left corner of the region and the size of the region to be monitored for clicks.

3. **Run the program**:

   Execute the Python script:

   ```bash
   python Tomarket-App.py
   ```

4. **Start and Stop Clicking**:

   - Press the `s` key to start auto-clicking.
   - Press the `p` key to stop auto-clicking.
   - Press the `q` key to quit the program.

## Customization

- **Color Detection**: You can change the `hex_color` variable to target a different color for clicking:

  ```python
  hex_color = "#fe3e6c"  # Replace with your desired hex color
  ```

- **Threshold and Contour Area**: Adjust the `threshold`, `min_area`, and `max_area` variables to fine-tune the color detection sensitivity and the size of areas to click on.
