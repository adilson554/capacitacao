from selenium import webdriver
from selenium.webdriver.common.by import By
import time

aguardar = 2 # 2 segundos


driver = webdriver.Firefox()

url = "http://"+input("Digite o site sem www.: ")
driver.get(url)
time.sleep(aguardar)
username = driver.find_element(By.ID, "chave")
password = driver.find_element(By.ID,"senha")
username.send_keys(input("Digite o username: "))
password.send_keys(input("Digite a senha: "))
time.sleep(aguardar)
login = driver.find_element(By.ID,"submit1")
login.click()


def consulta_por_rg(numerorg):
    menu = driver.find_element(By.ID,"divoCMenu0_0")
    consultas = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]")
    participação = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]")
    profissional = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]")
    porRG = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]")

    menu.click()
    consultas.click()
    participação.click()
    profissional.click()
    porRG.click()
    time.sleep(aguardar)

    rg = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[2]/form/table/tbody/tr[1]/td[2]/font/input[1]")
    rg.send_keys(numerorg)
    pesquisar = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[2]/form/table/tbody/tr[4]/td[2]/a[1]")
    pesquisar.click()
    time.sleep(aguardar)

    try:
        funcNome = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[5]/td[2]/font")
        funcRG = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[6]/td[2]/font[1]")
        funcCPF = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[7]/td[2]/font")

        tablePeriodo = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[11]/td/table/tbody/tr[2]/td[1]")
        tablePeriodo2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[11]/td/table/tbody/tr[3]/td[1]")
        tableCodigo = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[11]/td/table/tbody/tr[2]/td[2]")
        tableCodigo2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[11]/td/table/tbody/tr[3]/td[2]")
        tableEvento = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[11]/td/table/tbody/tr[2]/td[3]")
        tableEvento2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[11]/td/table/tbody/tr[3]/td[3]")
    except:
        save = open("relatorio.txt", "a")
        save.write(str(numerorg))
        save.write("----")
        save.write("Deu Erro")
        save.write("\n")
        save.close()
    else:
        x = funcNome.text + ";" + funcRG.text + ";" + funcCPF.text[0:11] + ";" + tablePeriodo.text + ";" + tableCodigo.text + ";" + tableEvento.text
        y = funcNome.text + ";" + funcRG.text + ";" + funcCPF.text[0:11] + ";" + tablePeriodo2.text + ";" + tableCodigo2.text + ";" + tableEvento2.text
        save = open("relatorio.txt", "a")
        save.write(x)
        save.write("\n")
        save.write(y)
        save.write("\n")
        save.close()
        
        
def sair():
    logout = driver.find_element(By.ID, "divoCMenu0_1")
    logout.click()
    time.sleep(5)
    driver.close()
    exit()
        

listarg = open("tabulados/listarg.txt", "r")
for linha in listarg:
	consulta_por_rg(linha[0:10])
listarg.close()
sair()



