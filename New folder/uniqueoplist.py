from activ import active_operation
from globaldf import GlobalDataFrame
from enshav import EnsHavDataFrame
from reading import reader

from chromo import chromo
import pandas as pd

class thelist:
    def __init__(self):
        self.UniqueOperationList()
     
    @active_operation
    def BasicInfoGetter(self): 
        d={}
        i=0
        col_info_list=[
            ["The ID of the landmark used to establish the coordinate system for the current feature.",
            "Describes the algorithm or operating procedure that generated this feature(name of the software,database name).",
            "Type of feature. Must be a term or accession from the SOFA sequence ontology.",
            "Start position of the feature, with sequence numbering starting at 1.",
            "End position of the feature, with sequence numbering starting at 1.",
            "A floating point value.",
            "defined as + (forward) or - (reverse).",
            "One of '0', '1' or '2'. '0' indicates that the first base of the feature is the first base of a codon, '1' that the second base is the first base of a codon, and so on..",
            "A semicolon-separated list of tag-value pairs, providing additional information about each feature."],
            GlobalDataFrame("Documents/New folder/seq.gff3").DataFrame.dtypes.tolist()
            ]

        d = {col_name: (col_info_list[0][i],col_info_list[1][i]) for i, col_name in enumerate(GlobalDataFrame("Documents/New folder/seq.gff3").DataFrame.columns)}
        return pd.DataFrame(d, index=['description', 'data type'])

    
    @active_operation
    def UniqueOperationList(self): 
        l=[]
        l1=[]
        l2=[]
        
        for el in list(dir(GlobalDataFrame)):
            if not "_" in str(el) and el!="UniqueOperationList" :
                l.append(el)
        for el in list(dir(EnsHavDataFrame)):
            if not "_" in str(el) and el!="UniqueOperationList" and el!="BasicInfoGetter" and el!="FeaturesOfTheSameSource":
                l1.append(el)
        for el in list(dir(chromo)):
            if not "_" in str(el):
                l2.append(el)
        self.df1 = pd.DataFrame(l, columns=['GlobalDataFrame'])
        self.df2 = pd.DataFrame(l1, columns=['EnsHavDataFrame'])
        self.df3 = pd.DataFrame(l2, columns=['chromo'])
        return self.df1, self.df2, self.df3
    


    @active_operation
    def NumOfEntries(self):
        counts_d1={}  
        counts_d2={} 
        counts_d3={}   
        for func_name in self.df1['GlobalDataFrame']:
            if func_name!="BasicInfoGetter" and func_name!="FeaturesOfTheSameSource" and func_name!="FractionOfUnassembledSequences":
                counts_d1[func_name]= len(getattr(GlobalDataFrame("Documents/New folder/seq.gff3"), func_name)())

        for func_name in self.df2['EnsHavDataFrame']:
            if func_name!="BasicInfoGetter" and func_name!="FeaturesOfTheSameSource" and func_name!="FractionOfUnassembledSequences":
                counts_d2[func_name]= len(getattr(EnsHavDataFrame("Documents/New folder/seq.gff3"), func_name)())

        for func_name in self.df3['chromo']:
            if func_name!="BasicInfoGetter" and func_name!="FeaturesOfTheSameSource" and func_name!="FractionOfUnassembledSequences": 
                counts_d3[func_name]= len(getattr(chromo("Documents/New folder/seq.gff3"), func_name)())
        
        df=pd.DataFrame([counts_d1,counts_d2,counts_d3],index=["Global Data","Data from ensembl,havana,ensembl_havana","Chromosomal Data"])  
        df['BasicInfoGetter']=[9,9,9]
        df['FeaturesOfTheSameSource']=[len(GlobalDataFrame("Documents/New folder/seq.gff3").DataFrame),len(EnsHavDataFrame("Documents/New folder/seq.gff3").DataFrame), 'NaN']
        text_file = open("Documents/New folder/templates/numofentries.html", "w")
        text_file.write("<a style=\"position:relative; top:200px; left:20px;\", href=\"{{ url_for('index') }}\">To the main page</a>")
        text_file.write(df.to_html())
        text_file.close()
        return df