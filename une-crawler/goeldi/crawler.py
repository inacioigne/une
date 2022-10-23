from .relatorio import DownloadRelatorio
from .getMarc import GetMarc
import ipdb

def CrawlerGoeldi():
    DownloadRelatorio("01012022", "31082022")

    #Ler relatório
    # with open(r'tmp\teste_2022-10-02-20-11-41.txt', encoding="utf8") as file:
    #     reader = file.readlines()
    #     file.close()
    # codesPergamun = list()
    # for line in reader[1:]:
    #     codesPergamun.append(line.split('\t', 1)[0])
    # itemID =  codesPergamun[1] 
    
    # for itemID in codesPergamun:
    #     print(itemID)
    #     GetMarc(itemID)
    
    