from reading import reader
from activ import active_operation


class chromo(reader):

    def __init__(self,file):
        reader.__init__(self,file)
        self.New_Data=self.DataFrame[self.DataFrame["source"] == 'GRCh38'] 
    
    @active_operation
    def EntriesWithEntireChr(self):
        result=self.New_Data.to_html()
        text_file = open("Documents/New folder/templates/entrieswithentirechr.html", "w")
        text_file.write("<a style=\"position:relative; top:50px; left:1300px;\", href=\"{{ url_for('index') }}\">To the main page</a>")
        text_file.write(result)
        text_file.close()
        return self.New_Data
    
    @active_operation
    def FractionOfUnassembledSequences(self):
        Old_DF=self.New_Data
        New_DF=Old_DF[Old_DF["type"] == 'supercontig']     
        return New_DF.index.size,Old_DF.index.size,New_DF.index.size/Old_DF.index.size


