import main

def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    n = client.get('/name/bob')
    assert r.status_code == 200
    assert 'Hello World! This is my first flask app.' in r.data.decode('utf-8')
    assert n.status_code == 200
    assert 'The name you entered: bob' in n.data.decode('utf-8')