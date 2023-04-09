from globaldf import GlobalDataFrame
from chromo import chromo
from activ import active_operation
import pandas as pd
from reading import reader


class EnsHavDataFrame(GlobalDataFrame):
    def __init__(self,file):#multip inheritance
        reader.__init__(self,file)
        source_list=['ensembl','havana','ensembl_havana']
        self.DataFrame = self.DataFrame[self.DataFrame["source"].isin(source_list)]
    
    @active_operation
    def EntriesFromEnsembl(self):
        return self.DataFrame
        
    @active_operation
    def GeneNamesGetter(self):
        l=[]
        for attribute_val in self.DataFrame["attribute"]:
            for tag_val in attribute_val.split(";"):
                if tag_val.startswith("Name="):
                    gene_name = tag_val[5:]
                    l.append(gene_name)
                    break
        gene_df = pd.DataFrame({"Gene Name": list(set(l))}) 
        return gene_df
     
     