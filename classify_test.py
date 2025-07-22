from detect_words.py import retorno_Palavra(assunto_alvo,1)
from detect_character.py import retorno_CaractereAssunto(assunto_alvo)

def Calcular_Pontuacao_ConteudoAssunto(assunto_alvo,conteudo_alvo):
  
  # Peso e Notas Assunto
  peso_Pa = 4.8
  peso_Ca = 3.1
  peso_Ga = 2.1

  nota_Pa = retorno_Palavra(assunto_alvo,1)          # PONTUAÇÃO RELATIVA PALAVRAS-CHAVE
  nota_Ca = retorno_CaractereAssunto(assunto_alvo)   # PONTUAÇÃO RELATIVA CARACTERES
  nota_Ga = 10                                       # PONTUAÇÃO RELATIVA GRAMATICA

  # Peso e Notas Conteudo
  peso_Pc = 3.0
  peso_Cc = 2.4
  peso_Lc = 3.1
  peso_Gc = 1.5

  nota_Pc = retorno_Palavra(conteudo_alvo,0)           # PONTUAÇÃO RELATIVA PALAVRAS
  nota_Cc = retorno_CaractereConteudo(conteudo_alvo)   # PONTUAÇÃO RELATIVA CARACTERES
  nota_Lc = 10                                         # PONTUAÇÃO RELATIVA LLM
  nota_Gc = 10                                         # PONTUAÇÃO RELATIVA GRAMATICA

  # Dicionarios da Relação Peso x Nota
  Assunto_PesoNota={peso_Pa:nota_Pa, peso_Ca:nota_Ca, peso_Ga:nota_Ga}
  Conteudo_PesoNota={peso_Pc:nota_Pc, peso_Cc:nota_Cc, peso_Lc:nota_Lc, peso_Gc:nota_Gc}

  # Cálculo da Nota
  nota_AssTotal_numerador=0
  nota_ConTotal_numerador=0

  nota_AssTotal_denominador=0
  nota_ConTotal_denominador=0

  for peso,nota in Assunto_PesoNota.items():
    nota_AssTotal_numerador+=nota*peso
    nota_AssTotal_denominador+=peso
    print(f'numerador: {nota_AssTotal_numerador}, denominador: {nota_AssTotal_denominador}')
  print(nota_AssTotal_numerador/nota_AssTotal_denominador,end='\n')

  for peso,nota in Conteudo_PesoNota.items():
    nota_ConTotal_numerador+=nota*peso
    nota_ConTotal_denominador+=peso
    print(f'numerador: {nota_ConTotal_numerador}, denominador: {nota_ConTotal_denominador}')
  print(nota_ConTotal_numerador/nota_ConTotal_denominador,end='\n\n')

  pontuacao_total = ((nota_AssTotal_numerador/nota_AssTotal_denominador)+(nota_ConTotal_numerador/nota_ConTotal_denominador))*(0.3)

  return round(pontuacao_total,3)

print(Calcular_Pontuacao_ConteudoAssunto(assunto_especifico,email_especifico))
