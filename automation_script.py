import pyautogui
import pandas as pd
import time


# This block reads a CSV file containing product data and stores it in a pandas DataFrame for processing.
tabela = pd.read_csv("produtos.csv")


# This ensures a short delay (0.2 seconds) between each command to simulate human interaction.
pyautogui.PAUSE = 0.2


# This block opens the Brave browser, maximizes the window, and navigates to the login page.
pyautogui.press("win")  # Open the Windows search bar
pyautogui.write("brave")  # Search for the Brave browser
pyautogui.press("enter")  # Launch the browser
pyautogui.keyDown("winleft")  # Hold the Windows key
pyautogui.press("up")  # Maximize the browser window
pyautogui.keyUp("winleft")  # Release the Windows key
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # Enter the login page URL
pyautogui.press("enter")  # Navigate to the URL


# Adds a 2-second pause to ensure the webpage has fully loaded before proceeding.
time.sleep(2)


# This block simulates entering the login credentials and submitting the form.
pyautogui.click(x=671, y=504)  # Click on the email input field
pyautogui.write("logintest@gmail.com")  # Enter the email
pyautogui.press("tab")  # Move to the password field
pyautogui.write("AnyPassword")  # Enter the password
pyautogui.press("enter")  # Submit the login form


# This loop iterates over each row of the DataFrame and fills out a form with the product data.
for linha in tabela.index:
    pyautogui.click(x=572, y=363)  # Click on the first input field of the form
    pyautogui.write(str(tabela.loc[linha, "codigo"]))  # Enter the product code
    pyautogui.press("tab")  # Move to the next field
    pyautogui.write(str(tabela.loc[linha, "marca"]))  # Enter the product brand
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))  # Enter the product type
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))  # Enter the product category
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))  # Enter the unit price
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))  # Enter the cost
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):  # Check if there are observations (not NaN)
        pyautogui.write(str(tabela.loc[linha, "obs"]))  # Enter the observations if they exist
    pyautogui.press("tab")
    pyautogui.press("enter")  # Submit the form
    pyautogui.press("home")  # Scroll back to the top of the form for the next entry
