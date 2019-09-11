import urllib.request, json
from urllib.parse import urlparse
from app import app

def to_json(data):
    response = app.response_class(response=json.dumps(data), mimetype='application/json')
    return response
    
@app.route('/')
def index():
    url = app.config['DATA_URL']
    with urllib.request.urlopen(url) as data_url:
        data = json.load(data_url)
        start_date = data['fechaCreacion']
        end_date = data['fechaFin']
        existing_dates = set(data['fechas'])
        start_year, start_month, *_ = list(map(int, start_date.split('-')))
        end_year, end_month, *_ = list(map(int, end_date.split('-')))
        missing_dates = []
        for y in range(start_year, end_year + 1):
            for m in range(1, 13):
                if y == end_year and m > end_month:
                    break
                if y == start_year and m < start_month:
                    continue
                some_date = '{}-{:02d}-{:02d}'.format(y, m, 1)
                if some_date not in existing_dates:
                    missing_dates.append(some_date)
        data['fechasFaltantes'] = missing_dates
        return to_json(data)

@app.route('/sampledata')
def sampledata():
    data = {'id': 6, 'fechaCreacion': '1969-03-01', 'fechaFin': '1970-01-01', 'fechas': ['1969-03-01', '1969-05-01', '1969-09-01', '1970-01-01']}
    return to_json(data)
