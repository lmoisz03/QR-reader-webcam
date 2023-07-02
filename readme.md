# QR Code Reader

A simple Python script to detect and decode QR codes using a webcam.

## Prerequisites

- Python 3.x
- OpenCV
- colorama

## How to Use

1. Clone this repository or copy the script to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required packages using pip:

```bash
pip install opencv-python colorama
```

4. Run the script

```bash
python main.py
```

## Usage

The QR Code Reader will access the default webcam (0) by default. If you want to use an IP webcam, you can set the URL to the video stream. For example:

```python
# For a default webcam
self.url = 0

# For an IP webcam (replace '100.x.x.x' with the actual IP address)
self.url = 'https://100.x.x.x/video'
```

# Output

The script will display a blue "Starting QR Code Reader..." message when it starts. After loading the frames, it will display a cyan "Loading frames..." message. When a QR code is detected, it will print a green message containing the detected link.

The QR Code Reader can be closed by pressing 'q' in the OpenCV window, and a yellow "QR Code Reader is closed." message will be displayed.

Note: Make sure you have a functioning webcam or IP camera stream to detect QR codes.

Enjoy scanning QR codes with the QR Code Reader!
