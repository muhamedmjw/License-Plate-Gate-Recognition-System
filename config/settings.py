"""
Configuration settings for the License Plate Recognition System

This module contains all configuration parameters for the application.
Settings are organized by component and can be modified to customize behavior.
"""

import os
from pathlib import Path

# Base directory paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
SRC_DIR = BASE_DIR / "src"

# Ensure data directories exist
DATA_DIR.mkdir(exist_ok=True)
(DATA_DIR / "database").mkdir(exist_ok=True)
(DATA_DIR / "images").mkdir(exist_ok=True)
(DATA_DIR / "images" / "captured").mkdir(exist_ok=True)
(DATA_DIR / "images" / "processed").mkdir(exist_ok=True)
(DATA_DIR / "logs").mkdir(exist_ok=True)

# ============================================================================
# CAMERA SETTINGS
# ============================================================================

CAMERA_SETTINGS = {
    # Default camera configuration
    'default_camera_index': 0,
    'backup_camera_indices': [1, 2],  # Fallback cameras to try
    
    # Camera resolution settings
    'default_resolution': (640, 480),
    'supported_resolutions': [
        (320, 240),
        (640, 480),
        (800, 600),
        (1024, 768),
        (1280, 720),
        (1920, 1080)
    ],
    
    # Frame rate settings
    'default_fps': 30,
    'min_fps': 10,
    'max_fps': 60,
    
    # Camera properties
    'auto_focus': True,
    'auto_exposure': True,
    'auto_white_balance': True,
    
    # Buffer settings
    'frame_buffer_size': 1,  # Number of frames to buffer
    'capture_timeout': 5.0,  # Seconds to wait for frame capture
    
    # Image quality settings
    'brightness': 0,      # -100 to 100
    'contrast': 0,        # -100 to 100
    'saturation': 0,      # -100 to 100
    'hue': 0,            # -100 to 100
    'gamma': 100,        # 50 to 200
    
    # Preview settings
    'preview_update_interval': 30,  # milliseconds
    'preview_resize_factor': 1.0,   # Scale factor for preview display
}

# ============================================================================
# DETECTION SETTINGS
# ============================================================================

DETECTION_SETTINGS = {
    # Main detection parameters
    'confidence_threshold': 0.5,      # Minimum confidence for valid detection
    'nms_threshold': 0.4,             # Non-maximum suppression threshold
    'max_detections_per_frame': 10,   # Maximum plates to detect per frame
    'detection_interval': 1.0,        # Seconds between detection attempts
    
    # YOLO model settings
    'yolo_model_path': 'yolov8n.pt',  # Path to YOLO model file
    'yolo_input_size': 640,           # Input size for YOLO model
    'use_gpu': False,                 # Use GPU acceleration if available
    'gpu_device': 0,                  # GPU device index
    
    # Traditional CV fallback settings
    'use_traditional_cv_fallback': True,
    'cv_min_area': 1000,              # Minimum contour area
    'cv_max_area': 50000,             # Maximum contour area
    'cv_min_aspect_ratio': 2.0,       # Minimum width/height ratio
    'cv_max_aspect_ratio': 6.0,       # Maximum width/height ratio
    
    # Preprocessing settings
    'apply_preprocessing': True,
    'gaussian_blur_kernel': (5, 5),   # Kernel size for Gaussian blur
    'morphology_kernel_size': (3, 3), # Kernel size for morphological operations
    'canny_lower_threshold': 50,      # Lower threshold for Canny edge detection
    'canny_upper_threshold': 150,     # Upper threshold for Canny edge detection
    
    # Perspective correction settings
    'apply_perspective_correction': True,
    'target_plate_width': 520,        # Target width for corrected plate
    'target_plate_height': 110,       # Target height for corrected plate
    'perspective_correction_margin': 10,  # Margin around detected plate
    
    # Filter settings
    'min_plate_width': 80,            # Minimum plate width in pixels
    'min_plate_height': 20,           # Minimum plate height in pixels
    'max_plate_width': 400,           # Maximum plate width in pixels
    'max_plate_height': 200,          # Maximum plate height in pixels
    
    # Performance settings
    'max_processing_time': 5.0,       # Maximum seconds for processing one frame
    'enable_multithreading': True,     # Use multiple threads for processing
    'thread_pool_size': 4,            # Number of worker threads
}

# ============================================================================
# OCR SETTINGS
# ============================================================================

OCR_SETTINGS = {
    # EasyOCR configuration
    'languages': ['en'],              # Languages for OCR recognition
    'use_gpu': False,                 # Use GPU acceleration for OCR
    'gpu_device': 0,                  # GPU device index for OCR
    
    # OCR parameters
    'paragraph': False,               # Treat text as paragraph
    'width_ths': 0.7,                # Width threshold for text boxes
    'height_ths': 0.7,               # Height threshold for text boxes
    'decoder': 'greedy',             # Decoder type: 'greedy' or 'beamsearch'
    'beamWidth': 5,                  # Beam width for beam search decoder
    'batch_size': 1,                 # Batch size for processing
    
    # Text preprocessing
    'preprocess_for_ocr': True,
    'resize_factor': 2.0,            # Resize factor before OCR
    'apply_gaussian_blur': True,
    'gaussian_kernel_size': (1, 1),
    'apply_morphology': True,
    'morphology_iterations': 1,
    'apply_threshold': True,
    'threshold_type': 'adaptive',     # 'binary', 'adaptive', or 'otsu'
    'threshold_value': 127,           # Threshold value for binary thresholding
    
    # Text validation
    'min_text_length': 3,             # Minimum characters in valid text
    'max_text_length': 15,            # Maximum characters in valid text
    'min_confidence': 0.3,            # Minimum OCR confidence
    'allowed_characters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    
    # Performance settings
    'ocr_timeout': 10.0,              # Maximum seconds for OCR processing
    'enable_caching': True,           # Cache OCR results for similar images
    'cache_size': 100,                # Maximum cached results
}

# ============================================================================
# DATABASE SETTINGS
# ============================================================================

DATABASE_SETTINGS = {
    # Database file settings
    'db_path': str(DATA_DIR / "database" / "license_plates.db"),
    'backup_path': str(DATA_DIR / "database" / "backups"),
    'enable_backup': True,
    'backup_interval': 3600,          # Backup interval in seconds (1 hour)
    'max_backups': 10,                # Maximum number of backup files to keep
    
    # Connection settings
    'connection_timeout': 30.0,       # Database connection timeout
    'enable_wal_mode': True,          # Enable Write-Ahead Logging
    'enable_foreign_keys': True,      # Enable foreign key constraints
    'cache_size': 2000,               # Database cache size in pages
    
    # Data management
    'max_records': 10000,             # Maximum records to keep in database
    'auto_cleanup': True,             # Automatically remove old records
    'cleanup_interval': 86400,        # Cleanup interval in seconds (24 hours)
    'retention_days': 30,             # Days to retain records
    
    # Performance settings
    'batch_insert_size': 100,         # Number of records to insert in batch
    'enable_indexing': True,          # Create database indexes
    'vacuum_interval': 604800,        # Database vacuum interval (7 days)
    
    # Logging settings
    'log_queries': False,             # Log SQL queries (for debugging)
    'log_slow_queries': True,         # Log slow queries
    'slow_query_threshold': 1.0,      # Threshold for slow queries (seconds)
}

# ============================================================================
# GUI SETTINGS
# ============================================================================

GUI_SETTINGS = {
    # Main window settings
    'window_title': 'License Plate Recognition System',
    'window_width': 1200,
    'window_height': 800,
    'min_width': 800,
    'min_height': 600,
    'resizable': True,
    'center_window': True,
    
    # Theme settings
    'theme': 'default',               # GUI theme: 'default', 'dark', 'light'
    'font_family': 'Arial',
    'font_size': 10,
    'title_font_size': 12,
    'header_font_size': 14,
    
    # Colors
    'primary_color': '#2E86AB',
    'secondary_color': '#A23B72',
    'success_color': '#2E7D32',
    'warning_color': '#F57C00',
    'error_color': '#C62828',
    'background_color': '#F5F5F5',
    'text_color': '#333333',
    
    # Layout settings
    'padding': 10,
    'margin': 5,
    'button_padding': (10, 5),
    'frame_padding': (15, 15),
    
    # Camera preview settings
    'preview_width': 640,
    'preview_height': 480,
    'preview_fps': 30,
    'show_detection_boxes': True,
    'detection_box_color': 'green',
    'detection_box_thickness': 2,
    
    # Results display settings
    'results_list_height': 10,
    'show_confidence_scores': True,
    'show_timestamps': True,
    'date_format': '%Y-%m-%d %H:%M:%S',
    
    # Admin panel settings
    'admin_window_width': 800,
    'admin_window_height': 600,
    'enable_admin_panel': True,
    'admin_password': None,           # Set to enable password protection
    
    # Update intervals
    'gui_update_interval': 100,       # milliseconds
    'status_update_interval': 1000,   # milliseconds
    'progress_update_interval': 500,  # milliseconds
}

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

LOGGING_SETTINGS = {
    # Log file settings
    'log_dir': str(DATA_DIR / "logs"),
    'log_filename': 'license_plate_recognition.log',
    'max_log_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5,                  # Number of backup log files
    
    # Logging levels
    'console_level': 'INFO',           # Console logging level
    'file_level': 'DEBUG',             # File logging level
    'gui_level': 'WARNING',            # GUI logging level
    
    # Log format
    'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'date_format': '%Y-%m-%d %H:%M:%S',
    
    # Module-specific logging
    'module_levels': {
        'camera': 'INFO',
        'detection': 'INFO',
        'ocr': 'INFO',
        'database': 'INFO',
        'gui': 'WARNING'
    },
    
    # Performance logging
    'log_performance': True,
    'performance_threshold': 1.0,      # Log operations taking longer than this
    'log_memory_usage': False,         # Log memory usage information
    
    # Error logging
    'log_exceptions': True,
    'log_stack_traces': True,
    'error_notification': True,        # Show error notifications in GUI
}

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================

PERFORMANCE_SETTINGS = {
    # Processing settings
    'max_concurrent_detections': 2,    # Maximum parallel detections
    'processing_queue_size': 10,       # Maximum queued frames
    'skip_frames': 0,                  # Skip every N frames for performance
    
    # Memory management
    'max_memory_usage': 512,           # Maximum memory usage in MB
    'garbage_collection_interval': 60, # Seconds between garbage collection
    'clear_cache_interval': 300,       # Seconds between cache clearing
    
    # Optimization settings
    'enable_optimization': True,
    'optimize_images': True,
    'image_quality': 85,               # JPEG quality for saved images
    'compression_level': 6,            # PNG compression level
    
    # Monitoring settings
    'enable_performance_monitoring': True,
    'monitoring_interval': 10,         # Seconds between performance checks
    'performance_log_interval': 60,    # Seconds between performance logs
    
    # Resource limits
    'max_cpu_usage': 80,               # Maximum CPU usage percentage
    'max_detection_time': 3.0,         # Maximum time for one detection
    'max_ocr_time': 2.0,               # Maximum time for OCR processing
}

# ============================================================================
# VALIDATION SETTINGS
# ============================================================================

VALIDATION_SETTINGS = {
    # License plate format validation
    'validate_format': True,
    'license_plate_patterns': [
        r'^[A-Z]{3}-\d{4}$',          # ABC-1234
        r'^[A-Z]{2}\d{2}-\d{3}$',     # AB12-123
        r'^[A-Z]\d{3}-[A-Z]{3}$',     # A123-ABC
        r'^[A-Z]{2}-\d{2}-[A-Z]{2}$', # AB-12-CD
        r'^[A-Z]{3}\d{3}$',           # ABC123
        r'^[A-Z]{2}\d{4}$',           # AB1234
        r'^\d{3}[A-Z]{3}$',           # 123ABC
    ],
    
    # Text validation
    'min_valid_characters': 3,
    'max_valid_characters': 10,
    'required_alphanumeric': True,
    'allow_special_chars': ['-', ' '],
    
    # Confidence validation
    'min_detection_confidence': 0.3,
    'min_ocr_confidence': 0.2,
    'confidence_weight_detection': 0.6,
    'confidence_weight_ocr': 0.4,
    
    # Duplicate detection
    'enable_duplicate_detection': True,
    'duplicate_time_threshold': 5.0,   # Seconds to consider as duplicate
    'duplicate_similarity_threshold': 0.9,  # Text similarity threshold
    
    # Quality validation
    'min_image_quality': 0.3,
    'blur_threshold': 100,             # Laplacian variance threshold
    'brightness_range': (30, 220),     # Acceptable brightness range
    'contrast_threshold': 50,          # Minimum contrast
}

# ============================================================================
# EXPORT SETTINGS
# ============================================================================

EXPORT_SETTINGS = {
    # File formats
    'default_format': 'csv',
    'supported_formats': ['csv', 'json', 'xml', 'pdf'],
    
    # CSV settings
    'csv_delimiter': ',',
    'csv_quote_char': '"',
    'csv_include_headers': True,
    'csv_date_format': '%Y-%m-%d %H:%M:%S',
    
    # JSON settings
    'json_indent': 2,
    'json_sort_keys': True,
    'json_ensure_ascii': False,
    
    # Export options
    'include_images': False,           # Include image data in exports
    'image_format': 'base64',          # Format for image data
    'max_export_records': 10000,       # Maximum records per export
    
    # File settings
    'default_export_dir': str(DATA_DIR / "exports"),
    'filename_template': 'license_plates_{timestamp}',
    'timestamp_format': '%Y%m%d_%H%M%S',
}

# ============================================================================
# DEVELOPMENT SETTINGS
# ============================================================================

DEVELOPMENT_SETTINGS = {
    # Debug settings
    'debug_mode': False,
    'verbose_logging': False,
    'show_debug_info': False,
    'enable_profiling': False,
    
    # Testing settings
    'test_mode': False,
    'mock_camera': False,
    'mock_database': False,
    'test_data_dir': str(BASE_DIR / "tests" / "data"),
    
    # Development tools
    'enable_hot_reload': False,
    'auto_save_settings': True,
    'backup_on_change': True,
    'validate_settings': True,
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_setting(category, key, default=None):
    """Get a setting value from the specified category."""
    categories = {
        'camera': CAMERA_SETTINGS,
        'detection': DETECTION_SETTINGS,
        'ocr': OCR_SETTINGS,
        'database': DATABASE_SETTINGS,
        'gui': GUI_SETTINGS,
        'logging': LOGGING_SETTINGS,
        'performance': PERFORMANCE_SETTINGS,
        'validation': VALIDATION_SETTINGS,
        'export': EXPORT_SETTINGS,
        'development': DEVELOPMENT_SETTINGS
    }
    
    if category in categories:
        return categories[category].get(key, default)
    return default

def update_setting(category, key, value):
    """Update a setting value in the specified category."""
    categories = {
        'camera': CAMERA_SETTINGS,
        'detection': DETECTION_SETTINGS,
        'ocr': OCR_SETTINGS,
        'database': DATABASE_SETTINGS,
        'gui': GUI_SETTINGS,
        'logging': LOGGING_SETTINGS,
        'performance': PERFORMANCE_SETTINGS,
        'validation': VALIDATION_SETTINGS,
        'export': EXPORT_SETTINGS,
        'development': DEVELOPMENT_SETTINGS
    }
    
    if category in categories:
        categories[category][key] = value
        return True
    return False

def validate_settings():
    """Validate all settings for consistency and correctness."""
    errors = []
    
    # Validate paths exist
    if not Path(DATABASE_SETTINGS['db_path']).parent.exists():
        errors.append("Database directory does not exist")
    
    # Validate numeric ranges
    if not (0 <= DETECTION_SETTINGS['confidence_threshold'] <= 1):
        errors.append("Detection confidence threshold must be between 0 and 1")
    
    if not (0 <= OCR_SETTINGS['min_confidence'] <= 1):
        errors.append("OCR confidence threshold must be between 0 and 1")
    
    # Validate camera settings
    if CAMERA_SETTINGS['default_fps'] <= 0:
        errors.append("Camera FPS must be positive")
    
    return errors

def reset_to_defaults():
    """Reset all settings to their default values."""
    # This would reload the module or reset all dictionaries
    # Implementation depends on how settings persistence is handled
    pass

# ============================================================================
# CONSTANTS
# ============================================================================

# Version information
VERSION = "1.0.0"
BUILD_DATE = "2025-07-09"
AUTHOR = "License Plate Recognition Team"

# Application constants
APP_NAME = "License Plate Recognition System"
APP_DESCRIPTION = "Computer Vision License Plate Detection and Recognition"
COPYRIGHT = "© 2025 Educational Project"

# File extensions
SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
SUPPORTED_VIDEO_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.wmv']

# Default values that might be used across modules
DEFAULT_TIMEOUT = 10.0
DEFAULT_RETRIES = 3
DEFAULT_BUFFER_SIZE = 1024
MAX_FILENAME_LENGTH = 255

# Status codes
STATUS_SUCCESS = 0
STATUS_ERROR = 1
STATUS_WARNING = 2
STATUS_INFO = 3

if __name__ == "__main__":
    # Print settings summary when run directly
    print(f"{APP_NAME} v{VERSION}")
    print(f"Build Date: {BUILD_DATE}")
    print(f"Database Path: {DATABASE_SETTINGS['db_path']}")
    print(f"Log Directory: {LOGGING_SETTINGS['log_dir']}")
    
    # Validate settings
    errors = validate_settings()
    if errors:
        print("\nSettings validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\nAll settings are valid.")