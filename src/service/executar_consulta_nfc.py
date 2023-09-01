from selenium.webdriver import Keys
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time



def executar_consulta_nfc(parametro, data_param):
    empresas=["FRANQUIA PRACA DE CASA FORTE","FRANQUIA SHOPPING CARPINA","FRANQUIA SHOPPING PLAZA","FRANQUIA RIO MAR","FRISABOR FERREIRA COSTA IMBIRIBEIRA","FRISABOR FERREIRA COSTA JOAO PESSOA","FRISABOR MARCO ZERO","FRISABOR BRENNAND PLAZA","FRISABOR BOA VISTA"]
    listaFlavia =empresas[:4]

    resultados = [] 
    empresa_mais_tentativas = ""
    max_tentativas = 0

    if parametro=="all":
        
        for empresa in empresas:
            tentativas = 0 
            while tentativas < 3:
                try:
                    dono = "flaviafranquias" if empresa in listaFlavia else "setegestao"
                    servico = Service(ChromeDriverManager().install())
                    navegador = wd.Chrome(service=servico)
                    navegador.get("https://rajpdv.com.br/index.php")
                    # Login
                    navegador.find_element(By.XPATH, '//*[@id="cliente"]').send_keys(dono)
                    navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys("luciano.machado")
                    navegador.find_element(By.XPATH,'//*[@id="senha"]').send_keys('123456')
                    navegador.find_element(By.XPATH,'//*[@id="gtco-header"]/div[2]/div/div/div/div[2]/div/div/div/div/form/div[4]/div/input').click()
                    time.sleep(2)
                    navegador.get('https://rajpdv.com.br/fiscal/consultar_nfce.php')
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'//*[@id="filtro_data_inicial"]').send_keys(data_param)
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'//*[@id="select2-filtro_regional-container"]').click()
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'/html/body/span/span/span[1]/input').send_keys(empresa,Keys.ENTER)
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'/html/body/div[2]/div[5]/section[2]/div/div/form/div/div[3]/input').click()
                    time.sleep(9)
                    navegador.switch_to.alert.accept()
                    time.sleep(50)
                    resultados.append(f"Consulta NFC executada com sucesso para {empresa} na data: {data_param}")
                    break

                except Exception as e:
                    resultados.append(f"Erro ao executar a consulta NFC para {empresa}: na tentativa {tentativas + 1}\n")
                    tentativas += 1 

                    if tentativas > max_tentativas:  # Atualiza a empresa com mais tentativas
                        max_tentativas = tentativas
                        empresa_mais_tentativas = empresa
          
        if max_tentativas > 0:
            resultados.append(f"A empresa com mais tentativas foi '{empresa_mais_tentativas}' com {max_tentativas} tentativas.")
        return resultados      
    else:
            tentativas = 0 
            while tentativas < 3:
                try:
                    dono = "flaviafranquias" if parametro in listaFlavia else "setegestao"
                    servico = Service(ChromeDriverManager().install())
                    navegador = wd.Chrome(service=servico)
                    navegador.get("https://rajpdv.com.br/index.php")
                    # Login
                    navegador.find_element(By.XPATH, '//*[@id="cliente"]').send_keys(dono)
                    navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys("luciano.machado")
                    navegador.find_element(By.XPATH,'//*[@id="senha"]').send_keys('123456')
                    navegador.find_element(By.XPATH,'//*[@id="gtco-header"]/div[2]/div/div/div/div[2]/div/div/div/div/form/div[4]/div/input').click()
                    time.sleep(2)
                    navegador.get('https://rajpdv.com.br/fiscal/consultar_nfce.php')
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'//*[@id="filtro_data_inicial"]').send_keys(data_param)
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'//*[@id="select2-filtro_regional-container"]').click()
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'/html/body/span/span/span[1]/input').send_keys(parametro,Keys.ENTER)
                    time.sleep(1)
                    navegador.find_element(By.XPATH,'/html/body/div[2]/div[5]/section[2]/div/div/form/div/div[3]/input').click()
                    time.sleep(9)
                    navegador.switch_to.alert.accept()
                    time.sleep(50)
                    resultados.append(f"Consulta NFC executada com sucesso para {parametro} na data: {data_param}")
                    break

                except Exception as e:
                    resultados.append(f"Erro ao executar a consulta NFC na tentativa {tentativas + 1}\n")
                    tentativas += 1 
            return resultados      