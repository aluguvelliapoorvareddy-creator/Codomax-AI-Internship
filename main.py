"""Interactive terminal runtime application for inferring student grades.

Loads the exported model artifact and safely processes incoming user terminal prompts.
"""

import numpy as np
import joblib
import utils

# Instantiate tracking logger
logger = utils.setup_logger("Application")

def load_prediction_model():
    """Attempts to pull the saved core predictor artifact from local disk storage.
    
    Returns:
        LinearRegression or None: The trained model matrix if found, else None.
    """
    try:
        return joblib.load(utils.MODEL_PATH)
    except FileNotFoundError:
        logger.error("Required model artifact file missing at target path: %s", utils.MODEL_PATH)
        print("\n[!] Error: Model file missing. Please execute 'train.py' first.")
        return None

def process_prediction(model, continuous_hours: float) -> float:
    """Feeds structured input inputs to the model and scales out-of-bound predictions.
    
    Args:
        model: Loaded scikit-learn model object instance.
        continuous_hours (float): Hours evaluated for score output.
        
    Returns:
        float: Bounded prediction score mapping securely between 0 and 100.
    """
    input_features = np.array([[continuous_hours]])
    raw_prediction = model.predict(input_features)[0]
    
    # Force logical real-world score limits between 0.0 and 100.0%
    return float(np.clip(raw_prediction, 0.0, 100.0))

def launch_interface() -> None:
    """Starts the application prompt interface loop via standard terminal input."""
    print("\n" + "=" * 45)
    print("      PROFESSIONAL STUDENT SCORE PREDICTOR      ")
    print("=" * 45)
    
    model = load_prediction_model()
    if model is None:
        return

    print("\nSystem ready. Enter hours studied to generate predicted score forecasts.")
    print("Type 'quit' or 'exit' anytime to safely close out of the application framework.\n")

    while True:
        user_raw = input("Enter Study Hours (0 - 24): ").strip().lower()
        
        if user_raw in ['exit', 'quit']:
            print("Terminating application runtime environment. Goodbye!")
            break
            
        try:
            hours = float(user_raw)
            
            # Reject values outside a standard day duration
            if not (0.0 <= hours <= 24.0):
                print("[-] Validation Error: Input value must fit within a standard 0 to 24 hour window.\n")
                continue
                
            predicted_grade = process_prediction(model, hours)
            print(f"[+] Predicted Exam Grade: {predicted_grade:.2f} / 100.00\n")
            
        except ValueError:
            print("[-] Formatting Error: Input provided cannot be interpreted as a numerical float.\n")

if __name__ == "__main__":
    launch_interface()