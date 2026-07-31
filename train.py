"""Model training pipeline for predicting student examination scores.

This script creates a mock dataset representing student learning habits, trains
a scikit-learn Linear Regression model, and saves the asset to disk.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import utils

# Instantiate tracking logger
logger = utils.setup_logger("TrainPipeline")

def prepare_dataset() -> pd.DataFrame:
    """Generates standard feature and label matrices for model training.
    
    Returns:
        pd.DataFrame: A structured DataFrame containing training columns.
    """
    logger.info("Initializing student training dataset parameters...")
    raw_data = {
        'study_hours': [1.5, 2.0, 3.2, 4.0, 5.1, 5.5, 6.0, 7.2, 8.0, 9.0],
        'student_score': [42.0, 48.0, 58.0, 65.0, 74.0, 77.0, 81.0, 89.0, 93.0, 98.0]
    }
    return pd.DataFrame(raw_data)

def run_training_pipeline() -> None:
    """Executes the end-to-end dataset preprocessing and model generation pipeline."""
    df = prepare_dataset()
    
    # Isolate independent features matrix (X) and dependent target vector (y)
    X = df[['study_hours']]
    y = df['student_score']
    
    logger.info("Fitting scikit-learn Linear Regression model equations...")
    model = LinearRegression()
    model.fit(X, y)
    logger.info("Model fitting sequence completed successfully.")
    
    # Ensure destination persistence directory exists
    os.makedirs(utils.MODEL_DIR, exist_ok=True)
    
    # Export trained artifact to local disk storage
    joblib.dump(model, utils.MODEL_PATH)
    logger.info("Serialized model artifact exported cleanly to: %s", utils.MODEL_PATH)

if __name__ == "__main__":
    run_training_pipeline()