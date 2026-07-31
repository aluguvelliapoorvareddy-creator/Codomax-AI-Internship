"""Utility functions and configuration constants for the score predictor project.

This module houses file path constants and logging configurations to keep
the core training and inference scripts clean and standardized.
"""

import os
import logging

# Define system path constants for model persistence
MODEL_DIR = "models"
MODEL_FILENAME = "score_predictor_model.pkl"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

def setup_logger(name: str) -> logging.Logger:
    """Configures and returns a standardized console logger.
    
    Args:
        name (str): The name of the module initializing the logger.
        
    Returns:
        logging.Logger: Pre-configured logger instance.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger(name)