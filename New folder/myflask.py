from flask import Flask,render_template,request 
import pandas as pd
from globaldf import GlobalDataFrame
from uniqueoplist import thelist
from enshav import EnsHavDataFrame
from chromo import chromo
from reading import reader
import activ

app = Flask(__name__)
gdf=GlobalDataFrame("Documents/New folder/seq.gff3")
edf=EnsHavDataFrame("Documents/New folder/seq.gff3")
cdf=chromo("Documents/New folder/seq.gff3")


@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/activeoplist')
def activeoplist():
    result=activ.active_operations
    return render_template('activeoplist.html', result=result) 
    
@app.route('/basicinfogetter')
def basicinfogetter():
    result=thelist().BasicInfoGetter()
    return render_template('basicinfogetter.html', result=result)

@app.route('/uniqueseqlist')
def uniqueseqlist():
    result=gdf.UniqueSeqList() 
    return render_template('uniqueseqlist.html',result=result)

@app.route('/uniqueseqlist2')
def uniqueseqlist2():
    result=edf.UniqueSeqList() 
    return render_template('uniqueseqlist.html',result=result)
    
@app.route('/featuresofthesamesource')
def featuresofthesamesource():
    result=gdf.FeaturesOfTheSameSource()
    return render_template('featuresofthesamesource.html', result=result, keys=result.columns)

@app.route('/featuresofthesamesource2')
def featuresofthesamesource2():
    result=edf.FeaturesOfTheSameSource()
    return render_template('featuresofthesamesource.html', result=result, keys=result.columns)   
    
@app.route('/uniqueoperationlist')
def uniqueoperationlist():
    result=thelist().UniqueOperationList()
    return render_template('uniqueoperationlist.html', result=result)

@app.route('/numofentries')
def numofentries():
    thelist().NumOfEntries()
    return render_template('numofentries.html')

@app.route('/entriesfromensembl')
def entriesfromensembl():
    result = edf.EntriesFromEnsembl().iloc[0:500]
    result=result.to_html()
    text_file = open("Documents/New folder/templates/entriesfromensembl.html", "w")
    text_file.write("<a href=\"{{ url_for('index') }}\">To the main page</a>")
    text_file.write(result)
    text_file.close()
    
    return render_template('entriesfromensembl.html')

@app.route('/genenamesgetter')
def genenamesgetter():
    result=edf.GeneNamesGetter()
    return render_template('genenamesgetter.html', result=result["Gene Name"].iloc[0:1000].copy())

@app.route('/entriesforeachtypeofoper')
def entriesforeachtypeofoper():
    result=edf.EntriesForEachTypeOfOper()
    return render_template('entriesforeachtypeofoper.html', result=result)

@app.route('/entrieswithentirechr')
def entrieswithentirechr():
    result=cdf.EntriesWithEntireChr()
    return render_template('entrieswithentirechr.html', result=result)

@app.route('/codedesc')
def codedesc():
    return render_template('codedesc.html')

@app.route('/fractionofunassembledsequences')
def fractionofunassembledsequences():
    result=cdf.FractionOfUnassembledSequences()
    return render_template('fractionofunassembledsequences.html', result=result)
    
@app.route('/process', methods=['POST'])
def process():
    result=gdf.FeaturesOfTheSameSource()
    source = request.form['source']
    return render_template('process.html', result=(result[source][0]),source=source)
    
if __name__ == '__main__':
    app.run(debug=True)