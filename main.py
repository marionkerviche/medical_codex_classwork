from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/MNdataUtilization.csv')

# df['payer'].value_counts()
# df.columns
# df['principal_diagnosis_code'].value_counts()

app = Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/county_name/<value>', methods=['GET'])
def county_name(value):
   # filter_value = request.args.get(icdcode)
    filtered = df[df['county_name'] == value]
  #  result = filtered.to_json(orient="records") 
    return filtered.to_json(orient="records") 

@app.route('/county_name/<value>/sex/<value2>')
def county_name_2(value, value2):
    filtered = df[df['county_name'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    return filtered2.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)

