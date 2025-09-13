#!/usr/bin/env python3
"""
Basic OpenCV Example
This is a simple example demonstrating basic OpenCV functionality for image processing.
"""

import cv2
import numpy as np

def create_sample_image():
    """Create a simple sample image for demonstration."""
    # Create a 400x400 image with 3 channels (BGR)
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    
    # Add some colored rectangles
    cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), -1)  # Blue rectangle
    cv2.rectangle(img, (200, 50), (300, 150), (0, 255, 0), -1)  # Green rectangle
    cv2.rectangle(img, (125, 200), (225, 300), (0, 0, 255), -1)  # Red rectangle
    
    # Add some text
    cv2.putText(img, 'OpenCV Example', (100, 350), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return img

def basic_operations(image):
    """Demonstrate basic OpenCV operations."""
    print("Original image shape:", image.shape)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Grayscale image shape:", gray.shape)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    
    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    return gray, blurred, edges

def main():
    """Main function to run the OpenCV example."""
    print("OpenCV Example - Basic Image Processing")
    print("=" * 40)
    
    # Create sample image
    original = create_sample_image()
    
    # Perform basic operations
    gray, blurred, edges = basic_operations(original)
    
    # Save images (since we can't display them in this environment)
    cv2.imwrite('original.png', original)
    cv2.imwrite('grayscale.png', gray)
    cv2.imwrite('blurred.png', blurred)
    cv2.imwrite('edges.png', edges)
    
    print("Images saved:")
    print("- original.png: Original colored image")
    print("- grayscale.png: Grayscale conversion")
    print("- blurred.png: Gaussian blur applied")
    print("- edges.png: Edge detection result")
    
    print("\nExample completed successfully!")

if __name__ == "__main__":
    main()