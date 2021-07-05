#Fabio Santos

from random import randint
import random


from Arvore import (
   TreeNode, 
   inserir, 
   busca,
   listar, 
   BuscadorATP3)


keys = [
{1: ["bola", "arq1.txt"]},  {2: ["casa", "arq1.txt"]},
{2: ["casa", "arq2.txt"]},  {1: ["bola", "arq1.txt"]},
{3: ["dado", "arq1.txt"]},  {3: ["dado", "arq1.txt"]},
{3: ["dado", "arq2.txt"]},  {3: ["dado", "arq3.txt"]},
{3: ["dado", "arq2.txt"]},  {4: ["arvore", "arq1.txt"]}, 
{4: ["arvore", "arq2.txt"]}]


def main():
  # inserindo valores na arvore ATP 2 
  source = TreeNode(0)
  for chave in keys:
    key = min(chave.keys())
    nodo = TreeNode(chave=key,lista=chave[key])
    inserir(source, nodo)
  

  # Procura por( valores na árvore.
  menu = str(input("Entre com os termos a ser pesquisados (separados por espaço): "))
  for termo in menu.split():
    print("-"*20, termo, "-"*20)
    result = BuscadorATP3(source, keys, termo)
    print("Resultado da busca - ",result['processado'])


if __name__ == '__main__':
    main()

