#!/usr/bin/env python
# coding: utf-8

# # Envio Automático de Orçamento de Social Media

# Na primeira etapa, cria-se o pdf com os dados do orçamento

# In[2]:


projeto = input ("Digite a descrição do projeto: ")

horas_estimadas = input ("Digite o total de horas estimadas: ")

valor_hora = input ("Digite o valor da hora trabalhada: ")

prazo_estimado = input ("Digite o prazo estimado para entrega: ")

valor_total_estimado = int (horas_estimadas) * int (valor_hora) 

print (valor_total_estimado)

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template_social_rm.png", x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))

pdf.output ("orçamento_social_media.pdf")
print ("Orçamento Gerado com Sucesso")


# Na segunda etapa, utilizara-se a ferramenta de automação, para enviar o orçamento ao cliente via email, sendo essa a sequencia:
# 
# - Abrir nova aba
# - Escrever o endereço do Gmail e dar enter
# - Clicar no botão escrever
# - Preencher o destinatário e o assunto
# - Escrever o email
# - Anexar o Orçamento
# - Clicar em enviar

# In[6]:


import pyautogui
import pyperclip


# In[15]:


pyautogui.PAUSE = 5

pyautogui.hotkey("ctrl", "t")
pyperclip.copy ("gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyautogui.click (x=99, y=209)

pyperclip.copy ("rnunes.md@gmail.com")
pyautogui.hotkey ("ctrl", "v")
pyautogui.hotkey ("tab")

pyperclip.copy ("Orçamento- Social Media")
pyautogui.hotkey ("ctrl", "v")
pyautogui.hotkey ("tab")

mensagem = f"""Estimado cliente,
Segue abaixo e em anexo o resultado de seu orçamento conosco:

Horas estimadas: {horas_estimadas}
Valor hora: {valor_hora}
Prazo de entrega: {prazo_estimado}
Total: R${valor_total_estimado}

Qualquer dúvida, favor entrar em contato, estou à disposição.

Atenciosamente,
Robson Nunes."""

pyperclip.copy (mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click (x=1333, y=977)
pyperclip.copy ("orçamento_social_media.pdf")
pyautogui.hotkey ("ctrl", "v")
pyautogui.click (x=1710, y=980)

pyautogui.click (x=1183, y=980)


# In[7]:


import time


# In[12]:


time.sleep (10)
pyautogui.position()


# In[ ]:




