# Installation Guide

## Prerequisites

Before installing the License Plate Recognition System, ensure your system meets these requirements:

### System Requirements
- **Operating System:** Windows 10/11, macOS 10.15+, or Linux Ubuntu 18.04+
- **Python Version:** Python 3.8 or higher
- **RAM:** Minimum 8GB (16GB recommended for better performance)
- **Storage:** At least 2GB free space
- **Camera:** USB webcam or built-in camera

### Hardware Requirements
- **CPU:** Intel i5 or AMD equivalent (minimum)
- **GPU:** Optional but recommended for faster processing
- **Camera:** Any USB camera with 720p resolution or higher

## Installation Steps

### Step 1: Install Python

If you don't have Python installed:

**Windows:**
1. Download Python from [python.org](https://python.org)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 2: Clone the Repository

```bash
# Clone the project
git clone https://github.com/yourusername/license-plate-recognition.git
cd license-plate-recognition

# Or download as ZIP and extract
```

### Step 3: Create Virtual Environment

Creating a virtual environment keeps your project dependencies isolated:

```bash
# Create virtual environment
python -m venv license_plate_env

# Activate the environment
# On Windows:
license_plate_env\Scripts\activate

# On macOS/Linux:
source license_plate_env/bin/activate
```

You should see `(license_plate_env)` in your terminal prompt when activated.

### Step 4: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

This will install:
- OpenCV for computer vision
- EasyOCR for text recognition
- NumPy for numerical operations
- Pillow for image processing
- Ultralytics for YOLO detection
- Matplotlib for visualization

### Step 5: Verify Installation

Test that everything is working:

```bash
# Test Python imports
python -c "import cv2, easyocr, numpy; print('All imports successful!')"

# Test camera (if available)
python scripts/test_camera.py
```

### Step 6: Initialize Database

```bash
# Set up the SQLite database
python scripts/setup_database.py
```

This creates the necessary database tables for storing detection results.

## Troubleshooting

### Common Issues

**1. OpenCV Installation Error**
```bash
# If OpenCV fails to install
pip install opencv-python-headless==4.8.1.78
```

**2. EasyOCR Download Issues**
```bash
# EasyOCR downloads models on first use
# Ensure good internet connection
# Models will be cached after first download
```

**3. Camera Not Detected**
```bash
# Test camera access
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera found:', cap.isOpened())"
```

**4. Permission Errors (macOS/Linux)**
```bash
# Add camera permissions
# macOS: System Preferences > Security & Privacy > Camera
# Linux: Add user to video group
sudo usermod -a -G video $USER
```

**5. Module Not Found Errors**
```bash
# Ensure virtual environment is activated
# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Platform-Specific Notes

**Windows:**
- Use Command Prompt or PowerShell
- Some antivirus software may flag OpenCV
- Windows Defender may need exclusions

**macOS:**
- May need to install Xcode command line tools
- Camera permissions required in System Preferences

**Linux:**
- May need additional packages: `sudo apt install libgl1-mesa-glx`
- Ensure camera permissions are set correctly

## Verification

After installation, verify everything works:

```bash
# Run the main application
python src/main.py

# You should see the GUI window open
# Test camera functionality
# Check database connection
```

## Development Setup (Optional)

If you plan to modify the code:

```bash
# Install development dependencies
pip install pytest black flake8 pytest-cov

# Run tests
pytest tests/

# Format code
black src/

# Check code style
flake8 src/
```

## Next Steps

1. **Read the [User Manual](user_manual.md)** to learn how to use the system
2. **Check [Technical Documentation](technical_docs.md)** to understand the architecture
3. **Review [API Reference](api_reference.md)** if you want to modify the code

## Getting Help

If you encounter issues:
1. Check this troubleshooting section
2. Review error messages carefully
3. Ensure all prerequisites are met
4. Check that your camera is working
5. Verify Python version compatibility

## Uninstallation

To remove the project:

```bash
# Deactivate virtual environment
deactivate

# Remove project folder
rm -rf license-plate-recognition/

# Remove virtual environment
rm -rf license_plate_env/
```

---

**Note:** This is a student project focused on learning computer vision and software development. The installation process is designed to be educational and straightforward.