from processing.ProcessingResult import ProcessingResult


class CompositionProcessor:
    recognizers: list = []

    def __init__(self):
        #add_recognizer()
        pass

    def add_recognizer(self, recognizer):
        self.recognizers.append(recognizer)

    def process_objects(self, objects):
        results = []
        for recognizer in self.recognizers:
            confidence = recognizer.recognize_composition(objects)
            composition_type = recognizer.composition_type()
            result = ProcessingResult(composition_type, confidence)
            results.append(result)
        return results
