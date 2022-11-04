fetch("http://pergamum.lncc.br/pergamum/biblioteca/index.php", {
  "headers": {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded"
  },
  "referrer": "http://pergamum.lncc.br/pergamum/biblioteca/index.php",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "rs=ajax_dados_acervo&rst=&rsrnd=1664067421482&rsargs[]=8560&rsargs[]=",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});