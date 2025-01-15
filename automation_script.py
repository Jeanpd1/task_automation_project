import pyautogui
import pandas as pd
import time

# Importar produtos da base de dados

tabela = pd.read_csv("produtos.csv")

# Tempo de espera entre comandos
pyautogui.PAUSE = 0.2
# Abrir sistema (navegador Brave)
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.keyDown("winleft")
pyautogui.press("up")
pyautogui.keyUp("winleft")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera o site carregar
time.sleep(2)

# Fazendo login no sistema
pyautogui.click(x=671, y=504)
pyautogui.write("logintest@gmail.com")
pyautogui.press("tab")
pyautogui.write("AnyPassword")
pyautogui.press("enter")

# Laço de repetição para percorrer o database
for linha in tabela.index:
    pyautogui.click(x=572, y=363) # Click no primeiro campo
    pyautogui.write(str(tabela.loc[linha,"codigo"])) # pega linha da tabela e digita no campo 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home") # Foram feitos testes com .scroll e também houve êxito