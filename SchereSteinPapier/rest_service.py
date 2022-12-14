from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

score = []

class DataClass(Resource):
    def get(self):
        return score

class DataHandlingClass(Resource):
    def get(self,name):
        if name in score:
            return score[name]
        return {'Message' : 'Nicht vorhanden'}

    def put(self,name):
        symbols = ["Rock","Spok","Paper","Lizzard","Siccors"]
        existing = False
        for i in score:
            if i['Name'] == name:
                existing = True
        data_rock = request.form['rock']
        data_spok = request.form['spok']
        data_paper = request.form['paper']
        data_lizzard = request.form['lizzard']
        data_siccors = request.form['siccors']
        data_block = [data_rock,data_spok,data_paper,data_lizzard,data_siccors]
        if existing:
            cnt = 0
            for i in score:
                if i['Name'] == name:
                    i[symbols[cnt]] = data_block[cnt]
                cnt += 1
        else:
            score.append({'Name' : name, 'Symbol':'Rock', 'Rock': data_rock})
            score.append({'Name' : name, 'Symbol':'Spok', 'Spok': data_spok})
            score.append({'Name' : name, 'Symbol':'Paper', 'Paper': data_paper})
            score.append({'Name' : name, 'Symbol':'Lizzard', 'Lizzard': data_lizzard})
            score.append({'Name' : name, 'Symbol':'Siccors', 'Siccors': data_siccors})
        if existing:
            return {"Message" : "Überschrieben"}
        return {"Message" : "Neu hinzugefügt"}

api.add_resource(DataClass, '/handling')
api.add_resource(DataHandlingClass, '/handling/<string:name>')

if __name__ == '__main__':
    app.run()