#!/usr/bin/env python3
"""
License Plate Recognition System
Main entry point for the application

This file initializes the system and launches the GUI interface.
"""

import sys
import os
import logging
from pathlib import Path

# NOTE: Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import GUI components
try:
    import tkinter as tk
    from tkinter import messagebox, ttk
except ImportError:
    print("Error: tkinter not available. Please install tkinter.")
    sys.exit(1)

# Import project modules
try:
    from src.utils.logger import setup_logger
    from src.gui.main_window import MainWindow
    from src.database.database_manager import DatabaseManager
    from config.settings import DATABASE_SETTINGS
except ImportError as e:
    print(f"Error importing project modules: {e}")
    print("Please ensure all required files are in place and dependencies are installed.")
    sys.exit(1)


class LicensePlateRecognitionApp:
    """Main application class that coordinates all components."""
    
    def __init__(self):
        """Initialize the application."""
        self.root = None
        self.main_window = None
        self.database_manager = None
        self.logger = None
        
    def setup_logging(self):
        """Setup application logging."""
        try:
            self.logger = setup_logger()
            self.logger.info("Application logging initialized")
        except Exception as e:
            print(f"Warning: Could not setup logging: {e}")
            # Create a basic logger as fallback
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            self.logger = logging.getLogger(__name__)
    
    def setup_directories(self):
        """Create necessary directories if they don't exist."""
        directories = [
            'data',
            'data/database',
            'data/images',
            'data/images/captured',
            'data/images/processed',
            'data/logs'
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            
        self.logger.info("Directory structure verified")
    
    def setup_database(self):
        """Initialize the database connection."""
        try:
            self.database_manager = DatabaseManager()
            self.database_manager.initialize_database()
            self.logger.info("Database initialized successfully")
        except Exception as e:
            self.logger.error(f"Database initialization failed: {e}")
            messagebox.showerror(
                "Database Error",
                f"Could not initialize database: {e}\n\nPlease check the database configuration."
            )
            return False
        return True
    
    def setup_gui(self):
        """Initialize the GUI components."""
        try:
            self.root = tk.Tk()
            self.root.title("License Plate Recognition System")
            self.root.geometry("1200x800")
            
            # Set application icon if available
            try:
                # You can add an icon file in the project root if desired
                # NOTE: self.root.iconbitmap('icon.ico')
                pass
            except:
                pass
            
            # Create main window
            self.main_window = MainWindow(self.root, self.database_manager)
            
            self.logger.info("GUI initialized successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"GUI initialization failed: {e}")
            messagebox.showerror(
                "GUI Error",
                f"Could not initialize GUI: {e}\n\nPlease check your display settings."
            )
            return False
    
    def handle_exit(self):
        """Handle application exit."""
        try:
            self.logger.info("Application shutting down...")
            
            # Close database connection
            if self.database_manager:
                self.database_manager.close()
            
            # Close main window
            if self.main_window:
                self.main_window.on_closing()
            
            # Destroy root window
            if self.root:
                self.root.quit()
                self.root.destroy()
                
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")
        finally:
            sys.exit(0)
    
    def run(self):
        """Main application entry point."""
        try:
            # Setup logging first
            self.setup_logging()
            self.logger.info("Starting License Plate Recognition System...")
            
            # Setup directories
            self.setup_directories()
            
            # Setup database
            if not self.setup_database():
                return False
            
            # Setup GUI
            if not self.setup_gui():
                return False
            
            # Configure exit handler
            self.root.protocol("WM_DELETE_WINDOW", self.handle_exit)
            
            # Start the main event loop
            self.logger.info("Application started successfully")
            self.root.mainloop()
            
        except KeyboardInterrupt:
            self.logger.info("Application interrupted by user")
            self.handle_exit()
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            messagebox.showerror(
                "Application Error",
                f"An unexpected error occurred: {e}\n\nPlease check the logs for more details."
            )
            self.handle_exit()
            return False
        
        return True


def check_dependencies():
    """Check if all required dependencies are available."""
    required_modules = [
        'cv2',
        'numpy',
        'PIL',
        'easyocr',
        'ultralytics'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print("Error: Missing required dependencies:")
        for module in missing_modules:
            print(f"  - {module}")
        print("\nPlease install the missing dependencies using:")
        print("pip install -r requirements.txt")
        return False
    
    return True


def main():
    """Main function - entry point of the application."""
    print("=" * 50)
    print("License Plate Recognition System")
    print("=" * 50)
    print("Starting application...")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Create and run the application
    app = LicensePlateRecognitionApp()
    success = app.run()
    
    if success:
        print("Application closed successfully.")
    else:
        print("Application closed with errors.")
        sys.exit(1)


if __name__ == "__main__":
    main()