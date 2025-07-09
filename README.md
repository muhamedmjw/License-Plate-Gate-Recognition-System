# License Plate Recognition System

A comprehensive computer vision application for automated license plate detection, recognition, and management using OpenCV, EasyOCR, and machine learning techniques.

## 🚀 Project Overview

This system captures live camera feeds, detects license plates using computer vision algorithms, applies perspective correction for optimal text extraction, and uses OCR technology to read plate numbers. All detections are stored in a database with timestamps and can be managed through an intuitive GUI interface.

**Key Features:**
- Real-time license plate detection from camera feeds
- Perspective correction for angled plates
- OCR text extraction with high accuracy
- Database storage and management
- Administrative GUI interface
- Comprehensive logging system

## 🎯 Project Goals

- **Primary Goal:** Develop a functional license plate recognition system
- **Academic Goal:** Demonstrate software engineering principles and computer vision knowledge
- **Technical Goal:** Achieve >85% plate recognition accuracy
- **Performance Goal:** Process detections in <2 seconds

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Usage](#usage)
- [Development](#development)
- [Testing](#testing)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- USB camera or IP camera
- Minimum 8GB RAM
- 500MB+ storage space

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/license-plate-recognition.git
   cd license-plate-recognition
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv license_plate_env
   
   # On Windows:
   license_plate_env\Scripts\activate
   
   # On Linux/Mac:
   source license_plate_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup database:**
   ```bash
   python scripts/setup_database.py
   ```

5. **Test camera:**
   ```bash
   python scripts/test_camera.py
   ```

## 🚀 Quick Start

1. **Run the application:**
   ```bash
   python src/main.py
   ```

2. **Using the GUI:**
   - Click "Start Camera" to begin live detection
   - View detected plates in the main window
   - Access admin panel for database management
   - Check logs for system events

3. **First Detection:**
   - Position a license plate in front of the camera
   - Wait for automatic detection and processing
   - View results in the database panel

## 📁 Project Structure

```
license-plate-recognition/
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
├── setup.py                     # Package setup
│
├── config/                      # Configuration files
│   ├── __init__.py
│   ├── settings.py             # Application settings
│   └── database_config.py      # Database configuration
│
├── src/                        # Source code
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   │
│   ├── camera/                 # Camera handling
│   │   ├── __init__.py
│   │   ├── camera_interface.py # Camera operations
│   │   └── camera_utils.py     # Camera utilities
│   │
│   ├── detection/              # Plate detection
│   │   ├── __init__.py
│   │   ├── plate_detector.py   # Main detection logic
│   │   ├── preprocessing.py    # Image preprocessing
│   │   └── perspective_corrector.py # Perspective correction
│   │
│   ├── ocr/                    # Text recognition
│   │   ├── __init__.py
│   │   ├── ocr_processor.py    # OCR operations
│   │   └── text_validator.py   # Text validation
│   │
│   ├── database/               # Database operations
│   │   ├── __init__.py
│   │   ├── database_manager.py # Database interface
│   │   └── models.py          # Data models
│   │
│   ├── gui/                    # User interface
│   │   ├── __init__.py
│   │   ├── main_window.py      # Main application window
│   │   ├── admin_panel.py      # Administrative interface
│   │   └── widgets/           # GUI components
│   │       ├── __init__.py
│   │       ├── camera_widget.py
│   │       └── database_widget.py
│   │
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── image_utils.py      # Image processing utilities
│       ├── logger.py           # Logging configuration
│       └── validator.py        # Input validation
│
├── data/                       # Data storage
│   ├── database/              # Database files
│   │   └── license_plates.db  # SQLite database
│   ├── images/                # Image storage
│   │   ├── captured/          # Original captures
│   │   └── processed/         # Processed images
│   └── logs/                  # Log files
│
├── scripts/                   # Utility scripts
│   ├── setup_database.py      # Database initialization
│   ├── test_camera.py         # Camera testing
│   └── data_migration.py      # Data migration tools
│
├── tests/                     # Test files
│   ├── __init__.py
│   ├── test_camera.py         # Camera tests
│   ├── test_database.py       # Database tests
│   ├── test_detection.py      # Detection tests
│   └── test_ocr.py           # OCR tests
│
└── docs/                      # Documentation
    ├── installation.md        # Installation guide
    ├── user_manual.md         # User manual
    ├── technical_docs.md      # Technical documentation
    └── api_reference.md       # API documentation
```

## ✨ Features

### Core Functionality
- **Real-time Detection:** Live camera feed processing
- **Plate Localization:** Automatic license plate detection in images
- **Perspective Correction:** Transform angled plates to front view
- **OCR Processing:** Extract text from corrected plate images
- **Database Storage:** Store detections with timestamps
- **Search & Filter:** Query historical detections

### Advanced Features
- **Multi-format Support:** Handle various license plate formats
- **Confidence Scoring:** Rate detection accuracy
- **Image Preprocessing:** Enhance images for better recognition
- **Error Handling:** Robust error management and logging
- **Performance Monitoring:** Track system performance metrics

### User Interface
- **Live Preview:** Real-time camera feed display
- **Detection Results:** Show processed plates and extracted text
- **Database Management:** View, search, and manage stored plates
- **Configuration Panel:** Adjust system settings
- **Logging Display:** Monitor system events and errors

## 🛠 Technology Stack

### Core Libraries
- **OpenCV (4.8.1.78):** Computer vision and image processing
- **NumPy (1.24.3):** Numerical operations and array processing
- **Pillow (10.0.0):** Image handling and manipulation
- **EasyOCR (1.7.0):** Optical character recognition
- **Ultralytics (8.0.165):** YOLO object detection models
- **Matplotlib (3.7.1):** Visualization and debugging

### Development Tools
- **pytest (7.4.0):** Testing framework
- **black (23.7.0):** Code formatting
- **flake8 (6.0.0):** Code linting
- **pytest-cov (4.1.0):** Test coverage reporting

### Built-in Libraries
- **tkinter:** GUI framework
- **sqlite3:** Database operations
- **threading:** Concurrent processing
- **logging:** System logging

## 🎮 Usage

### Basic Operation

1. **Start the application:**
   ```bash
   python src/main.py
   ```

2. **Initialize camera:**
   - Click "Start Camera" button
   - Adjust camera settings if needed
   - Ensure proper lighting and positioning

3. **Begin detection:**
   - Position vehicles with visible license plates
   - System automatically detects and processes plates
   - Results appear in real-time

### Administrative Functions

- **View Database:** Access all stored detections
- **Search Plates:** Find specific license plates
- **Export Data:** Export detections to CSV
- **System Logs:** Monitor application events
- **Configuration:** Adjust detection parameters

### Command Line Tools

- **Database setup:** `python scripts/setup_database.py`
- **Camera test:** `python scripts/test_camera.py`
- **Data migration:** `python scripts/data_migration.py`

## 👨‍💻 Development

### Development Setup

1. **Install development dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests:**
   ```bash
   pytest tests/
   ```

3. **Format code:**
   ```bash
   black src/
   ```

4. **Lint code:**
   ```bash
   flake8 src/
   ```

### Code Style
- Follow PEP 8 style guidelines
- Use black for code formatting
- Maintain test coverage >80%
- Document all functions and classes

### Adding New Features

1. Create feature branch: `git checkout -b feature/new-feature`
2. Implement feature with tests
3. Update documentation
4. Submit pull request

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_detection.py

# Run with coverage
pytest --cov=src

# Run with verbose output
pytest -v
```

### Test Categories

- **Unit Tests:** Test individual components
- **Integration Tests:** Test component interactions
- **Performance Tests:** Measure system performance
- **Accuracy Tests:** Validate detection accuracy

### Test Data
- Sample license plate images in `tests/data/`
- Mock camera feeds for testing
- Database test fixtures

## 📚 Documentation

### Available Documentation

- **[Installation Guide](docs/installation.md):** Detailed setup instructions
- **[User Manual](docs/user_manual.md):** Complete user guide
- **[Technical Documentation](docs/technical_docs.md):** System architecture
- **[API Reference](docs/api_reference.md):** Function documentation

### Generating Documentation

```bash
# Install documentation dependencies
pip install sphinx

# Generate API documentation
sphinx-build -b html docs/ docs/_build/
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Academic Information

**Project Type:** Final Year Bachelor's Project - Software Engineering  
**Duration:** July 2025 - January 2026  
**Complexity:** Medium to Advanced  
**Primary Technologies:** Computer Vision, Machine Learning, Database Management

## 📞 Support

For questions and support:
- Create an issue in the GitHub repository
- Check the documentation in the `docs/` folder
- Review the troubleshooting section in the user manual

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- EasyOCR developers for OCR capabilities
- Ultralytics for YOLO implementation
- Python community for excellent libraries

---

**Note:** This is an academic project developed for educational purposes. For production use, additional security and performance optimizations would be required.