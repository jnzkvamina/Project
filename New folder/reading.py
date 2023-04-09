import pandas as pd
import os

class reader:
    def __init__(self, file):
        self.filename, self.extension = os.path.splitext(file)
        if self.extension == ".gff3":
            self.DataFrame = filter(file)
        else:
            print("not GFF3 format")
        
def filter(file):
    DataFrameGFF3 = pd.read_csv(file, sep="\t", header=None, comment="#", names=["seqid", "source", 
        "type", "start", "end", "score", "strand", "phase", "attribute"])
    return DataFrameGFF3
