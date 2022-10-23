import pysolr
import json

solr = pysolr.Solr('http://localhost:8983/solr/search/', timeout=10)

def Update(solr):
    #goeldi
    print('atualizando Goeldi...')
    with open(r'./goeldi.json', encoding="utf-8") as file_json:
        docs = json.loads(file_json.read())
        solr.add(docs)
        file_json.close()

    #inpe
    print('atualizando INPE...')
    with open(r'./inpe.json', encoding="utf-8") as file_json:
        docs = json.loads(file_json.read())
        solr.add(docs)
        file_json.close()
    
    #mcti
    print('atualizando INPE...')
    with open(r'./mcti.json', encoding="utf-8") as file_json:
        docs = json.loads(file_json.read())
        solr.add(docs)
        file_json.close()
    
Update(solr)