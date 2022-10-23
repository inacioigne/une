import httpx

def CreateCore():

    url = 'http://localhost:8983/api/cores'

    json_data = {
        'create': {
            'name': 'search',
            'configSet': 'une',
            },
        }
    r = httpx.post('http://localhost:8983/api/cores', json=json_data, timeout=None)

    print(r.status_code)

def CreateCollection():

    json_data = {
            'create': {
                'name': 'test3',
                'config': 'une',
                'numShards': 1,
            },
        }
    r = httpx.post('http://localhost:8983/api/collections', json=json_data, timeout=None)
    print(r)

#CreateCore()
CreateCollection()

