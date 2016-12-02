import request
# This is a Rest request protocol that generates API for http clients that consume any public API
# This involves getting all the data in the request cycle
def get_data():
    return request.get(_url('/data/'))
# This is used to filter data based on a given url
def display_data():
    return request.get(_url('/data/{:d}'.format(data_id)))
# This public API is used to add data into the URL
def add_data(summary, description=""):
    return request.post(_url('/data/{:d}.')),json={
    'summary'=summary,
    'description'=description
    })

def data_done(data_id):
return request.delete(_url('/data/{:d}/'.format(data_id)))
# This is used to update data using the API
def update_data(data_id, summary, description):
    return request.put(url, json={
    summary='summary'
    description='description'
    })
