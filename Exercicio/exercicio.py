from selenium import webdriver

#----------Inicio funções

def printaQtd(list):
    tam = len(list)
    print('\nO texto “Getting Started” aparece %d vezes na página!\n' %(tam))

def formataStr(texto):
    return (texto.replace(' ', '').replace('.', '').replace('2', '')).lower()

def countChar(texto):
    # Uso um dicionário para guardar a frequencia dos caracteres, sendo char como key e o value a qtd de vezes que ele aparece
    frequency = {} 
  
    for char in texto: 
        if char in frequency: 
            frequency[char] += 1
        else: 
            frequency[char] = 1

    return sorted(frequency.items(), key=lambda x: x[1])

def printChar(freq):

    # Filtro por caracteres que possuem a frequencia maior que 1
    lista = [item for item in freq if item[1]>1]

    if len(lista) > 0:
        print("A string “Getting Started” possui caracteres repetidos!\n")

        for char in lista:
            print('* %c aparece %d vezes' %(char[0], char[1]))

    else:
        print("A string “Getting Started” não possui caracteres repetidos!")

#----------Fim funções

PATH = '.\chromedriver.exe'
browser = webdriver.Chrome(PATH)

# Abrindo a pagina
browser.get('https://selenium-python.readthedocs.io/')

# Encontro sidebar navigation
sideBar = browser.find_element_by_class_name('sphinxsidebarwrapper')

# Busco e acesso o link para Getting Started dentro do sideBar
gs_link = sideBar.find_element_by_xpath('//a[@href="getting-started.html"]')
gs_link.click()

# Encontro o texto "Getting Started" na tela
gs_find = browser.find_elements_by_xpath('//*[contains(text(), "Getting Started")]')

# Esse passo abaixo foi necessário pois quando printei gs_find, estavam as duas vezes q Getting Started aparece na página e mais um elemento vazio 
gs_list = [item for item in gs_find if len(item.text) > 0]

if len(gs_list) > 0:

    # Printo qts vezes a string aparece na página
    printaQtd(gs_list)
    
    gs_text = gs_list[0].text

    # Formato str para ter só caracteres que me interessam e uso lower para deixa-la toda em minusculo
    gs_text = formataStr(gs_text)

    # Conto e printo a frequencia dos caracteres na str
    freq_char = countChar(gs_text)
    printChar(freq_char)

browser.set_page_load_timeout(1)
browser.quit()