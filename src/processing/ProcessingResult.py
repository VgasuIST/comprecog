

class ProcessingResult:
    composition_type: str
    confidence: float

    def __init__(self, composition_type, confidence):
        self.composition_type = composition_type
        self.confidence = confidence

    def get_composition_type(self):
        return self.composition_type

    def get_confidence(self):
        return self.confidence
