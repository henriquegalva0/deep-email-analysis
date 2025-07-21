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

def analisar_mensagem(mensagem):
  fator=0
  print("Análise de Segurança da Mensagem")

  invisiveis = detectar_invisiveis(mensagem)

  print("\nCaracteres invisíveis:")
  if invisiveis:
    print("Caractere invisível detectado")
    fator+=2
    for inv in invisiveis: fator+=0.1 #print(f" - Posição {inv['posição']}: {inv['caractere']} ({inv['nome_unicode']})")
  else: print(" - Nenhum encontrado.")

  print("\nVerificação de scripts misturados:")
  scripts = detectar_scripts_misturados(mensagem)
  actual_scripts = {k:v for k,v in scripts.items() if k != "Outros" or any("LETTER" in unicodedata.name(char[1], "") for char in v)}

  if len(actual_scripts) > 1:
    print("Mistura de alfabetos detectada\n")
    fator+=3
    for script, chars in scripts.items():
      if script != "Outros" or any("LETTER" in unicodedata.name(char[1], "") for char in chars):
        fator+=0.3
        for pos, char, nome in chars: print(f"   • {script} — '{char}' (posição {pos}): {nome}")
  else: print("Nenhuma mistura suspeita de alfabetos")
  return fator

# Exemplo
mensagem = """gооgle\u200b.com"""
print(analisar_mensagem(mensagem))