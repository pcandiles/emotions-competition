import pickle
from pathlib import Path

def download_model(model_path):
    # Example with direct download link from Google Drive or Dropbox
    import gdown
    url = "https://colab.research.google.com/drive/14VrdHMyJZnYCyyvFhySF732kojvzzBII?usp=drive_link"
    gdown.download(url, str(model_path), quiet=False)

def get_model():
    model_path = Path(__file__).parent / "emotion_model.pkl"
    if not model_path.exists():
        print("Downloading model...")
        download_model(model_path)
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict_emotion(text, model):
    # Assume model includes vectorizer + classifier pipeline
    return model.predict([text])[0]
