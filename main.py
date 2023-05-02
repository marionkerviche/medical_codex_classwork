from flask import Flask
import pandas as pd

df = pd.read_csv('./data/MNdataUtilization.csv')

# df['payer'].value_counts()
# df.columns
# df['principal_diagnosis_code'].value_counts()

app = Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN ICD code details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return top10rows
# something is wrong here, go back and watch lecture

@app.route('/icd', methods=['GET'])
def icdcode():
    # R73 for example
    filter_value = request.args.get(icdcode)
    filtered = df[df['principal_diagnosis_code'] == filter_value]
  #  result = filtered.to_json(orient="records") 
    return filtered.to_json(orient="records") 

#just look at code from zoom recording

if __name__ == '__main__':
    app.run(debug=True)

