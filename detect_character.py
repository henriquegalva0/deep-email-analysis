import unicodedata

INVISIVEIS = ['\u200b', '\u200c', '\u200d', '\u2060', '\ufeff']
pontuacoes_legitimas = [
  '.',# ponto final
  ',', # vírgula
  ';', # ponto e vírgula
  ':', # dois pontos
  '!', # exclamação
  '?', # interrogação
  '-', # hífen
  '_', # underline
  '(', ')', # parênteses
  '[', ']', # colchetes
  '{', '}', # chaves
  '"', "'", # aspas
  '/', '\\', # barra e barra invertida
  '@', # arroba
  '#', # hashtag
  '$', # cifrão
  '%', # porcentagem
  '&', # e comercial
  '*', # asterisco
  '+', # mais
  '=', # igual
  '<', '>', # sinais de menor/maior
  '`', '~', # til e crase invertida
  '^', # circunflexo
  '|', # pipe vertical
]

def detectar_invisiveis(texto):
  return [{
      'caractere': repr(c),
      'nome_unicode': unicodedata.name(c, 'Desconhecido'),
      'posição': i
  } for i, c in enumerate(texto) if c in INVISIVEIS]

def detectar_scripts_misturados(texto):
  scripts = {}
  for i, c in enumerate(texto):
    if c in pontuacoes_legitimas:
      continue

    nome = unicodedata.name(c, "UNKNOWN")
    if "LATIN" in nome:
      script = "Latin"
    elif "CYRILLIC" in nome:
      script = "Cyrillic"
    elif "GREEK" in nome:
      script = "Greek"
    elif "ARABIC" in nome:
      script = "Arabic"
    else:
      script = "Outros"
    scripts.setdefault(script, []).append((i, c, nome))
  return scripts

def inspecionar_unicode(texto):
    return [{
        'caractere': c,
        'posição': i,
        'unicode': f'U+{ord(c):04X}',
        'nome': unicodedata.name(c, 'Desconhecido')
    } for i, c in enumerate(texto)]

def retorno_CaractereConteudo(mensagem):
  fator=0
  print("Análise de Segurança da Mensagem")

  invisiveis = detectar_invisiveis(mensagem)

  print("\nCaracteres invisíveis:")
  if invisiveis:
    print("Caractere invisível detectado")
    fator+=3
    for inv in invisiveis: fator+=0.5 #print(f" - Posição {inv['posição']}: {inv['caractere']} ({inv['nome_unicode']})")
  else: print(" - Nenhum encontrado.")

  print("\nVerificação de scripts misturados:")
  scripts = detectar_scripts_misturados(mensagem)
  actual_scripts = {k:v for k,v in scripts.items() if k != "Outros" or any("LETTER" in unicodedata.name(char[1], "") for char in v)}

  if len(actual_scripts) > 1:
    print("Mistura de alfabetos detectada\n")
    fator+=4
    for script, chars in scripts.items():
      if script != "Outros" or any("LETTER" in unicodedata.name(char[1], "") for char in chars):
        fator+=0.8
        #for pos, char, nome in chars: print(f"   • {script} — '{char}' (posição {pos}): {nome}")
  else: print("Nenhuma mistura suspeita de alfabetos")

  quantia_pontuacao=sum(1 for d in mensagem if d in ["!!","!!!","??","???"])

  if quantia_pontuacao: fator+=1.5

  return fator

def retorno_CaractereAssunto(mensagem):
  fator=0
  print("Análise de Segurança da Mensagem")

  invisiveis = detectar_invisiveis(mensagem)

  print("\nCaracteres invisíveis:")
  if invisiveis:
    print("Caractere invisível detectado")
    fator+=3
    for inv in invisiveis: fator+=0.5 #print(f" - Posição {inv['posição']}: {inv['caractere']} ({inv['nome_unicode']})")
  else: print(" - Nenhum encontrado.")

  print("\nVerificação de scripts misturados:")
  scripts = detectar_scripts_misturados(mensagem)
  actual_scripts = {k:v for k,v in scripts.items() if k != "Outros" or any("LETTER" in unicodedata.name(char[1], "") for char in v)}

  if len(actual_scripts) > 1:
    print("Mistura de alfabetos detectada\n")
    fator+=3
    for script, chars in scripts.items():
      if script != "Outros" or any("LETTER" in unicodedata.name(char[1], "") for char in chars):
        fator+=0.8
        #for pos, char, nome in chars: print(f"   • {script} — '{char}' (posição {pos}): {nome}")
  else: print("Nenhuma mistura suspeita de alfabetos")

  caracteres_estranhos = [
    '$', '%', '&', '*', '+',
    ';', '<', '=', '>', '?', '@', '\\', '^', '`', '~',
    '©', '®', '€', '£', '¥', '§', '¶', '¤', '×', '÷', '°', '™'
  ]

  caracteres_estranhos_identificados=sum(1 for c in mensagem if c in caracteres_estranhos)

  if caracteres_estranhos_identificados > 0 and caracteres_estranhos_identificados < 3: fator+=2
  elif caracteres_estranhos_identificados >= 3: fator +=3

  quantia_pontuacao=sum(1 for d in mensagem if d in ["!","?"])

  if quantia_pontuacao>2 and quantia_pontuacao<4: fator+=1
  if quantia_pontuacao>4: fator+=2

  return fator

#gооgle\u200b.com
