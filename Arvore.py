# Fábio Santos

from DataStructure import simplelist
from collections    import Counter
from collections    import defaultdict
import itertools


xpto = defaultdict(list)


class TreeNode:
    def __init__(self, chave=None,lista=None, esquerda=None, direita=None):
        self.chave = chave
        self.lista = lista
        self.listaencadeada = simplelist() 
        self.listaencadeada.append(chave,lista)
        self.esquerda = esquerda
        self.direita = direita


    def __repr__(self):
        return '%s <- %s %s  -> %s' % (
          self.esquerda and self.esquerda.chave,
          self.chave,self.lista,self.direita and  
          self.direita.chave)


def busca(source, chave):
    # Realização de tratamento de Dados, buscando dado presente
    if source is None:
        return None


    # Chave que está sendo procurada está na raiz
    if source.chave == chave:
        return source


    # Chave que está sendo procurada é maior que raiz
    if source.chave < chave:
        #raiz.direita.listaencadeada.show()
        return busca(source.direita, chave)
    else:
    # chave que está procurada é menor que a da raiz.
        #raiz.esquerda.listaencadeada.show()
        return busca(source.esquerda, chave)

      # Inserindo um nodo em uma árvore binária de pesquisa


def inserir(source, nodo):
      # Nodo inserido precisa ser inserido na raiz
      if source is None:
          source = nodo

      # Nodo precisa ser inserido  na subárvore direita
      elif source.chave < nodo.chave:
          if source.direita is None:
              source.direita = nodo
          else:
              #self.listaencadeada.append(raiz.direita,nodo)
              inserir(source.direita, nodo)

      # Nodo precisa ser inserido na sub árvore esquerda.
      else:
          if source.esquerda is None:
              source.esquerda = nodo
          else:
              inserir(source.esquerda, nodo)
              #self.listaencadeada.append(raiz.esquerda,nodo)


def listar(my_list): 
      
    # Criando um empty dicionario 
    for d in my_list:
       for key, value in d.items():
            xpto[key].append(value)
    final_list = []        
    for p in xpto:
      freq = [xpto[p].count(w) for w in xpto[p]]
      new_list = list(num for num,_ in itertools.groupby([{p[0][0]:p[0][1]} for p in list(num for num,_ in itertools.groupby(list(zip(xpto[p]))))]))  


      for add in range(len(new_list)):
       try: 
        if new_list[add].keys() == new_list[add+1].keys():
              final_list.append({list(new_list[add])[0]: [list(new_list[add].values())[0], list(new_list[add+1].values())[0] ]})


       except IndexError:
         pass


    return final_list


def CountFrequency(my_list): 
  
    # Creando um empty dicionario  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    result = []
    for key, value in freq.items(): 
        data = "%s : %s"%(key, value)
        result.append(data)
    return result    


def BuscadorATP3(source, keys, termo):
  ordenar = []
  result = {}
  for chave in keys:
    key = min(chave.keys())
    resultado = busca(source, key)
    ordenar.append(chave) if resultado else None
  

  valor = []
  for arvore in listar(ordenar):
    key, value = list(arvore.items())[0]
    if key == termo:
      [valor.append(item) for item in value]
      result['termo_buscado'] = key
    else:
       None
        

  count = 0
  print("Saida Arvore: ", valor)
  result['processado'] = CountFrequency(valor)  
  

  return result

# Fim