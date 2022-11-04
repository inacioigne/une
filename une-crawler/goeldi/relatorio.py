import ipdb
from .login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def DownloadRelatorio(inicio, fim):
    driver = Login()
  
    frame_home = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'frame_home'))
        )
    
    driver.switch_to.frame(frame_home)
    
    
    #Navega até relatórios e abre uma nova janela
    relatorios = driver.find_element(By.XPATH, '//*[@id="5a"]/table/tbody/tr/td/table/tbody/tr/td[2]')
    relatorios.click()
    sub_relatorios = driver.find_element(By.XPATH, '//*[@id="5b"]/table/tbody/tr/td/table/tbody/tr[2]/td/div')
    sub_relatorios.click()
    #Muda de janela
    windows = driver.window_handles
    #ipdb.set_trace()
    driver.switch_to.window(windows[1])
    
    #Muda de frame
    frame_relatorios = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_meio'))
        )
    driver.switch_to.frame(frame_relatorios)
   
    tab_relatorios = driver.find_element(By.XPATH, '//*[@id="+abre_2"]/table/tbody/tr/td')
    tab_relatorios.click()
    conferencia_materiais = driver.find_element(By.ID, '+abre_205')
    conferencia_materiais.click()
    bibliografico = driver.find_element(By.XPATH, '//*[@id="+fecha_205"]/table[6]/tbody/tr/td')
    bibliografico.click()
    #Filtros
    time.sleep(10)
    todos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'id_v_cod_tipo_obra_Todos'))
        )
    
    todos.click()
    livros = driver.find_element(By.ID, 'id_v_cod_tipo_obra_1')
    livros.click()
    data_inicial = driver.find_element(By.ID, 'v_data_inicial')
    data_inicial.send_keys(inicio)
    data_final = driver.find_element(By.ID, 'v_data_final')
    data_final.send_keys(fim)
    resumo = driver.find_element(By.ID, 'id_v_opcao_762')
    resumo.click()

    #Baixa relatório
    exportar = driver.find_element(By.ID, 'id_btn_exportar')
    exportar.click()
    btn_ok = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_ok'))
        )
    
    btn_ok.click()
    time.sleep(10)
