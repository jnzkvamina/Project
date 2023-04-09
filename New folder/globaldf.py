from reading import reader 
from activ import active_operation
import pandas as pd

class GlobalDataFrame(reader):
   
    @active_operation
    def UniqueSeqList(self): 
        id_rows = self.DataFrame.loc[self.DataFrame["attribute"].str.contains("ID", regex=False)]
        id_values = id_rows["attribute"].str.extract(r'ID=([^;]+)', expand=False)
        unique_ids = set(id_values)
        unique_id_list =(list(unique_ids))
        unique_id_df = pd.DataFrame({"ID": unique_id_list})
        return unique_id_df

    @active_operation
    def FeaturesOfTheSameSource(self):
        d = {}
        source_list = self.DataFrame["source"]
        for source in source_list:
            d[source] = d.get(source, 0) + 1
        df=pd.DataFrame(d, index=['number of features'])
        return df

    
    

 
    

