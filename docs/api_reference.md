# API Reference

## Overview

This document provides a comprehensive reference for all classes, functions, and methods in the License Plate Recognition System. The API is designed to be modular and extensible for educational purposes.

## Camera Module (`src/camera/`)

### CameraInterface Class

#### `__init__(self, camera_index=0)`
Initialize camera interface.

**Parameters:**
- `camera_index` (int): Camera device index (default: 0)

**Raises:**
- `CameraNotFoundError`: If camera cannot be accessed

**Example:**
```python
camera = CameraInterface(camera_index=0)
```

#### `start_camera(self)`
Start camera capture.

**Returns:**
- `bool`: True if camera started successfully

**Example:**
```python
if camera.start_camera():
    print("Camera started successfully")
```

#### `stop_camera(self)`
Stop camera capture and release resources.

**Example:**
```python
camera.stop_camera()
```

#### `capture_frame(self)`
Capture a single frame from the camera.

**Returns:**
- `numpy.ndarray`: Captured frame as BGR image
- `None`: If capture fails

**Example:**
```python
frame = camera.capture_frame()
if frame is not None:
    # Process frame
    pass
```

#### `get_camera_info(self)`
Get camera properties and capabilities.

**Returns:**
- `dict`: Camera information including resolution, FPS, etc.

**Example:**
```python
info = camera.get_camera_info()
print(f"Resolution: {info['width']}x{info['height']}")
```

### Camera Utilities

#### `list_available_cameras()`
List all available camera devices.

**Returns:**
- `list`: List of available camera indices

**Example:**
```python
from src.camera.camera_utils import list_available_cameras
cameras = list_available_cameras()
print(f"Available cameras: {cameras}")
```

#### `test_camera(camera_index)`
Test if a specific camera is working.

**Parameters:**
- `camera_index` (int): Camera index to test

**Returns:**
- `bool`: True if camera is accessible

**Example:**
```python
if test_camera(0):
    print("Camera 0 is working")
```

## Detection Module (`src/detection/`)

### PlateDetector Class

#### `__init__(self, model_path=None, confidence_threshold=0.5)`
Initialize plate detection system.

**Parameters:**
- `model_path` (str): Path to YOLO model file
- `confidence_threshold` (float): Minimum confidence for detections

**Example:**
```python
detector = PlateDetector(confidence_threshold=0.6)
```

#### `detect_plates(self, image)`
Detect license plates in an image.

**Parameters:**
- `image` (numpy.ndarray): Input image in BGR format

**Returns:**
- `list`: List of detection dictionaries with keys:
  - `bbox`: Bounding box coordinates [x, y, width, height]
  - `confidence`: Detection confidence score
  - `corners`: Corner points for perspective correction

**Example:**
```python
detections = detector.detect_plates(image)
for detection in detections:
    bbox = detection['bbox']
    confidence = detection['confidence']
    print(f"Plate found at {bbox} with confidence {confidence}")
```

#### `set_confidence_threshold(self, threshold)`
Update confidence threshold for detections.

**Parameters:**
- `threshold` (float): New confidence threshold (0.0 to 1.0)

**Example:**
```python
detector.set_confidence_threshold(0.7)
```

### PerspectiveCorrector Class

#### `__init__(self)`
Initialize perspective correction system.

#### `correct_perspective(self, image, corners)`
Correct perspective distortion of license plate.

**Parameters:**
- `image` (numpy.ndarray): Input image containing license plate
- `corners` (numpy.ndarray): Four corner points of the plate

**Returns:**
- `numpy.ndarray`: Perspective-corrected image
- `None`: If correction fails

**Example:**
```python
corrector = PerspectiveCorrector()
corrected_image = corrector.correct_perspective(image, corners)
```

#### `find_plate_corners(self, image, bbox)`
Find corner points of license plate for perspective correction.

**Parameters:**
- `image` (numpy.ndarray): Input image
- `bbox` (list): Bounding box [x, y, width, height]

**Returns:**
- `numpy.ndarray`: Four corner points
- `None`: If corners cannot be found

**Example:**
```python
corners = corrector.find_plate_corners(image, bbox)
if corners is not None:
    corrected = corrector.correct_perspective(image, corners)
```

### Preprocessing Functions

#### `preprocess_image(image, enhance_contrast=True)`
Preprocess image for better detection.

**Parameters:**
- `image` (numpy.ndarray): Input image
- `enhance_contrast` (bool): Whether to enhance contrast

**Returns:**
- `numpy.ndarray`: Preprocessed image

**Example:**
```python
from src.detection.preprocessing import preprocess_image
processed = preprocess_image(image, enhance_contrast=True)
```

#### `enhance_image_quality(image)`
Enhance image quality for better OCR results.

**Parameters:**
- `image` (numpy.ndarray): Input image

**Returns:**
- `numpy.ndarray`: Enhanced image

**Example:**
```python
enhanced = enhance_image_quality(plate_image)
```

## OCR Module (`src/ocr/`)

### OCRProcessor Class

#### `__init__(self, languages=['en'], gpu=False)`
Initialize OCR processor.

**Parameters:**
- `languages` (list): List of language codes for OCR
- `gpu` (bool): Whether to use GPU acceleration

**Example:**
```python
ocr = OCRProcessor(languages=['en'], gpu=False)
```

#### `extract_text(self, image)`
Extract text from license plate image.

**Parameters:**
- `image` (numpy.ndarray): License plate image

**Returns:**
- `dict`: Dictionary containing:
  - `text`: Extracted text
  - `confidence`: OCR confidence score
  - `bbox`: Text bounding box

**Example:**
```python
result = ocr.extract_text(plate_image)
if result:
    print(f"Detected text: {result['text']}")
    print(f"Confidence: {result['confidence']}")
```

#### `preprocess_for_ocr(self, image)`
Preprocess image specifically for OCR.

**Parameters:**
- `image` (numpy.ndarray): Input image

**Returns:**
- `numpy.ndarray`: OCR-ready image

**Example:**
```python
ocr_ready = ocr.preprocess_for_ocr(plate_image)
```

### TextValidator Class

#### `__init__(self)`
Initialize