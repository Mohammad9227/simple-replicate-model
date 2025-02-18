# Prediction interface for Cog ⚙️
# https://cog.run/python

from cog import BasePredictor, Input

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load any resources if needed (currently not required)"""
        pass

    def predict(
        self,
        input_text: str = Input(description="Text to be reversed"),
    ) -> str:
        """Reverses the given text"""
        return input_text[::-1]  # Reverse the string