import argparse
from emotion_inference.model import predict_emotion, get_model
from emotion_inference.utils import get_kaggle_id

def main():
    parser = argparse.ArgumentParser(description="Emotion prediction CLI tool")
    parser.add_argument("--input", type=str, help="Text to predict emotion")
    parser.add_argument("--kaggle", action="store_true", help="Display Kaggle ID")

    args = parser.parse_args()

    if args.kaggle:
        print(get_kaggle_id())
    elif args.input:
        model = get_model()
        print(predict_emotion(args.input, model))
    else:
        print("Please provide --input for prediction or --kaggle to display ID.")
