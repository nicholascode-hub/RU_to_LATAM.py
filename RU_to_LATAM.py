def translitera_russo_latino(texto):
  tabela_transliteracao = {
      "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D",
      "Е": "E", "Ё": "Yo", "Ж": "Zh", "З": "Z", "И": "I",
      "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N",
      "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T",
      "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Ts", "Ч": "Ch",
      "Ш": "Sh", "Щ": "Shch", "Ъ": "", "Ы": "Y",
      "Ь": "", "Э": "E", "Ю": "Yu", "Я": "Ya"
  }

  texto_transcrito = ""
  for letra in texto:
      if letra.upper() in tabela_transliteracao:
          texto_transcrito += tabela_transliteracao[letra.upper()]
      else:
          texto_transcrito += letra

  return texto_transcrito

def get_input_text():
  texto_russo = input("Insira o texto em russo: ")
  return texto_russo

# Exemplo de uso
texto_russo = get_input_text()
texto_latino = translitera_russo_latino(texto_russo)
print(f"Texto em russo: {texto_russo}")
print(f"Texto transcrito em latino: {texto_latino}")