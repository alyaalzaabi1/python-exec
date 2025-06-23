from processors.csv_reader import CSVReader
from processors.csv_validator import CSVValidator
from processors.csv_transformer import CSVTransformer
from processors.file_writer import CSVWriter
from pipeline import ProcessingPipeline

# Validator pipeline
pipeline1 = ProcessingPipeline(CSVReader(), CSVValidator(), CSVWriter())
pipeline1.run("data.csv", "validated.csv")

# Transformer pipeline
pipeline2 = ProcessingPipeline(CSVReader(), CSVTransformer(), CSVWriter())
pipeline2.run("data.csv", "transformed.csv")
