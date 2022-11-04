import httpx
cookies = {
    '_ga': 'GA1.2.2079248050.1664066541',
    '_gid': 'GA1.2.2142078304.1664066541',
    'PHPSESSID': '39cc0e635e162b385fdf3e7c08676954',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.2.2079248050.1664066541; _gid=GA1.2.2142078304.1664066541; PHPSESSID=39cc0e635e162b385fdf3e7c08676954',
    'Origin': 'http://pergamum.lncc.br',
    'Referer': 'http://pergamum.lncc.br/pergamum/biblioteca/index.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

data = 'rs=ajax_dados_acervo&rst=&rsrnd=1664067421482&rsargs[]=8560&rsargs[]='

response = httpx.post(
    'http://pergamum.lncc.br/pergamum/biblioteca/index.php', 
    #cookies=cookies, 
    headers=headers, data=data, verify=False)