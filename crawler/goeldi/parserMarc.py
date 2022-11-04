import config
from selenium.webdriver.common.by import By

def ParserMarc(trs):

    controfield = {}
    datafield =  {}
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        field = tds[0].text
        subfield = tds[2].text
        if int(field) < 9:
            controfield[field] = subfield
        else:
            subfields = {}
            subfield = subfield.split('$')[1:]
            for sub in subfield:
                code = sub.split(' ', 1)[0]
                value = sub.split(' ', 1)[1]
                subfields[code] = value
            if field in config.MARC_REPETIVEL:
                if field not in datafield.keys():
                    datafield[field] = [subfields]
                else:
                    datafield[field].append(subfields)
            else:
                datafield[field] = subfields

    marcJson = {'controfield': controfield, 'datafield': datafield}
    return marcJson