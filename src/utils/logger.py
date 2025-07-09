#!/usr/bin/env python3
"""
Logger Utility Module
Provides centralized logging configuration for the License Plate Recognition System

This module sets up logging with file rotation, console output, and different log levels.
"""

import logging
import logging.handlers
import os
import sys
from datetime import datetime
from pathlib import Path


class ColoredFormatter(logging.Formatter):
    """Custom formatter that adds colors to console output."""
    
    # Color codes for different log levels
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
        'RESET': '\033[0m'      # Reset color
    }
    
    def format(self, record):
        """Format log record with colors for console output."""
        if hasattr(record, 'levelname') and record.levelname in self.COLORS:
            # Add color to level name
            colored_levelname = f"{self.COLORS[record.levelname]}{record.levelname}{self.COLORS['RESET']}"
            record.levelname = colored_levelname
        
        return super().format(record)


class LoggerManager:
    """Manages logging configuration and provides logger instances."""
    
    def __init__(self):
        """Initialize the logger manager."""
        self.log_directory = Path("data/logs")
        self.log_directory.mkdir(parents=True, exist_ok=True)
        
        # Create log file names with timestamp
        self.log_filename = self.log_directory / f"lpr_system_{datetime.now().strftime('%Y%m%d')}.log"
        self.error_log_filename = self.log_directory / f"lpr_errors_{datetime.now().strftime('%Y%m%d')}.log"
        
        self._setup_root_logger()
    
    def _setup_root_logger(self):
        """Setup the root logger with handlers for file and console output."""
        # Get root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        
        # Clear any existing handlers
        root_logger.handlers.clear()
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        console_formatter = ColoredFormatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # Create file handler with rotation
        try:
            file_handler = logging.handlers.RotatingFileHandler(
                self.log_filename,
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5,
                encoding='utf-8'
            )
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(file_formatter)
            root_logger.addHandler(file_handler)
        except Exception as e:
            print(f"Warning: Could not create file handler: {e}")
        
        # Create error file handler
        try:
            error_handler = logging.handlers.RotatingFileHandler(
                self.error_log_filename,
                maxBytes=5*1024*1024,  # 5MB
                backupCount=3,
                encoding='utf-8'
            )
            error_handler.setLevel(logging.ERROR)
            error_handler.setFormatter(file_formatter)
            root_logger.addHandler(error_handler)
        except Exception as e:
            print(f"Warning: Could not create error file handler: {e}")
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)
        root_logger.addHandler(console_handler)
    
    def get_logger(self, name=None):
        """Get a logger instance with the specified name."""
        if name is None:
            name = __name__
        
        logger = logging.getLogger(name)
        return logger
    
    def set_log_level(self, level):
        """Set the global log level."""
        if isinstance(level, str):
            level = getattr(logging, level.upper())
        
        logging.getLogger().setLevel(level)
        
        # Update console handler level
        for handler in logging.getLogger().handlers:
            if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
                handler.setLevel(level)
    
    def cleanup_old_logs(self, days_to_keep=30):
        """Clean up old log files."""
        import glob
        import time
        
        try:
            # Find all log files
            log_files = glob.glob(str(self.log_directory / "*.log*"))
            
            current_time = time.time()
            cutoff_time = current_time - (days_to_keep * 24 * 60 * 60)
            
            for log_file in log_files:
                try:
                    file_time = os.path.getmtime(log_file)
                    if file_time < cutoff_time:
                        os.remove(log_file)
                        print(f"Removed old log file: {log_file}")
                except Exception as e:
                    print(f"Error removing log file {log_file}: {e}")
                    
        except Exception as e:
            print(f"Error during log cleanup: {e}")


# Global logger manager instance
_logger_manager = None


def setup_logger(name=None, log_level=logging.INFO):
    """
    Setup and return a logger instance.
    
    Args:
        name (str, optional): Logger name. If None, uses calling module name.
        log_level (int, optional): Logging level. Defaults to INFO.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    global _logger_manager
    
    if _logger_manager is None:
        _logger_manager = LoggerManager()
    
    # Set log level
    _logger_manager.set_log_level(log_level)
    
    # Get logger name from calling module if not provided
    if name is None:
        import inspect
        frame = inspect.currentframe().f_back
        name = frame.f_globals.get('__name__', 'lpr_system')
    
    logger = _logger_manager.get_logger(name)
    
    # Log initial message
    logger.info(f"Logger initialized for {name}")
    
    return logger


def get_logger(name=None):
    """
    Get an existing logger instance or create a new one.
    
    Args:
        name (str, optional): Logger name.
    
    Returns:
        logging.Logger: Logger instance.
    """
    global _logger_manager
    
    if _logger_manager is None:
        return setup_logger(name)
    
    return _logger_manager.get_logger(name)


def set_debug_mode(enabled=True):
    """
    Enable or disable debug mode logging.
    
    Args:
        enabled (bool): Whether to enable debug mode.
    """
    global _logger_manager
    
    if _logger_manager is None:
        _logger_manager = LoggerManager()
    
    level = logging.DEBUG if enabled else logging.INFO
    _logger_manager.set_log_level(level)


def cleanup_logs(days_to_keep=30):
    """
    Clean up old log files.
    
    Args:
        days_to_keep (int): Number of days to keep log files.
    """
    global _logger_manager
    
    if _logger_manager is None:
        _logger_manager = LoggerManager()
    
    _logger_manager.cleanup_old_logs(days_to_keep)


# Convenience functions for quick logging
def log_info(message, logger_name=None):
    """Log an info message."""
    logger = get_logger(logger_name)
    logger.info(message)


def log_error(message, logger_name=None, exc_info=False):
    """Log an error message."""
    logger = get_logger(logger_name)
    logger.error(message, exc_info=exc_info)


def log_warning(message, logger_name=None):
    """Log a warning message."""
    logger = get_logger(logger_name)
    logger.warning(message)


def log_debug(message, logger_name=None):
    """Log a debug message."""
    logger = get_logger(logger_name)
    logger.debug(message)


# Example usage and testing
if __name__ == "__main__":
    # Test the logger
    logger = setup_logger("test_logger")
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Test convenience functions
    log_info("Testing convenience function")
    log_error("Testing error logging")
    log_warning("Testing warning logging")
    log_debug("Testing debug logging")
    
    print("Logger test completed. Check the logs directory for output files.")