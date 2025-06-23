from typing import Any
from protocols import FileReader, FileProcessor, FileWriter


class ProcessingPipeline:
    def __init__(self, reader: FileReader, processor: FileProcessor, writer: FileWriter):
        self.reader = reader
        self.processor = processor
        self.writer = writer

    def run(self, input_path: str, output_path: str):
        data = self.reader.read(input_path)
        processed_data = self.processor.process(data)
        self.writer.write(processed_data, output_path)
