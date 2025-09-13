# OpenCV Study Repository

This is my opencv library study repository with basic examples.

## Basic Example

The `basic_example.py` demonstrates fundamental OpenCV operations:
- Creating sample images
- Color space conversion (BGR to Grayscale)  
- Gaussian blur filtering
- Edge detection using Canny algorithm

### Running the Example

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the basic example:
```bash
python basic_example.py
```

This will generate four output images:
- `original.png`: Original colored image with rectangles
- `grayscale.png`: Grayscale conversion
- `blurred.png`: Gaussian blur applied
- `edges.png`: Edge detection result

## Requirements

- Python 3.6+
- OpenCV Python (opencv-python >= 4.5.0)
- NumPy (>= 1.20.0)
