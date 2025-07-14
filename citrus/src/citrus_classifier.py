
import joblib
import numpy as np
from pathlib import Path

class CitrusClassifier:
    def __init__(self, model_dir):
        """Load trained model and preprocessor"""
        self.model_dir = Path(model_dir)
        self.model = joblib.load(self.model_dir / 'best_model.pkl')
        self.scaler = joblib.load(self.model_dir / 'scaler.pkl')
        self.feature_names = joblib.load(self.model_dir / 'feature_names.pkl')
    
    def predict(self, red, diameter):
        """Predict citrus type from features"""
        # Prepare input
        X = np.array([[red, diameter]])
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Predict
        prediction = self.model.predict(X_scaled)[0]
        
        # Get probability if available
        if hasattr(self.model, 'predict_proba'):
            proba = self.model.predict_proba(X_scaled)[0]
            confidence = max(proba)
        else:
            confidence = None
        
        # Convert to label
        label = 'orange' if prediction == 0 else 'grapefruit'
        
        return {
            'prediction': label,
            'confidence': confidence,
            'red': red,
            'diameter': diameter
        }

# Example usage
if __name__ == "__main__":
    classifier = CitrusClassifier('output/models')
    
    # Test prediction
    result = classifier.predict(red=0.5, diameter=65.0)
    print(f"Prediction: {result['prediction']}")
    if result['confidence']:
        print(f"Confidence: {result['confidence']:.3f}")
