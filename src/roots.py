import math

def bissecao(f, a, b, ni, t, i=0, l=[]):
  """
  Esta função realiza o cálculo do método de bisseção.
  f: função contínua
  a: intervalo esquerdo
  b: intervalo direito
  ni: número máximo de iterações
  t: tolerância
  """
  x = a + (b-a) / 2
  # Condição de parada em relação ao número de vezes que será executado ni
  if i < ni:
    # Condição de parada caso o módulo seja menor que a tolerância
    if abs(b-a) < t:
      return x
    # Condição de parada caso o ponto médio em f seja 0
    if f(x) == 0:
      return x
    # Caso recursivo
    if f(x) * f(a) < 0:
      return bissecao(f,a,x,ni,t,i+1,l+[x, (b-a) / 2])
    else:
      if (b-a) != 0:
      # Caso Recursivo
        return bissecao(f,x,b,ni,t,i+1,l+[x, (b-a) / 2])
      else:
        return bissecao(f,x,b,ni,t,i+1,l)
  return l


def newtonRaphson(f, fl, xi, ni, t, i=0, l=[]):
  """
  Esta função realiza o cálculo do método de Newton.
  f: função contínua
  fl: derivada da função 
  xi: raiz
  ni: número máximo de iterações
  t: tolerância
  """
  # Cálculo do método de Newton para encontrar a raiz
  x1 = xi-f(xi) / fl(xi)
  # Condição de parada em relação ao número de vezes que será executado ni
  if i < ni:
    if x1 > 0:
    # Caso Recursivo
      return newtonRaphson(f,fl,x1,ni,t,i+1,l+[x1, abs((xi-x1)/x1)])
    else:
      return newtonRaphson(f,fl,x1,ni,t,i+1,l)
  return l


def secante(f, x0, x1, ni, t, i=0, l=[]):
  """
  Esta função realiza o cálculo do método de bisseção.
  f: função contínua
  x0,x1: raizes 
  ni: número máximo de iterações
  t: tolerância
  """
  f0 = f(x0)
  # Condição de parada em relação ao número de vezes que será executado ni
  if i < ni:
    f1 = f(x1)
    x2 = (x0*f1-x1*f0)/(f1-f0)
    f0=f1
    if x2 > 0:
    # Caso Recursivo
      return secante(f, x1, x2, ni, t, i+1, l+[x2, abs((x2-x1)/x2)])
    else:
      return secante(f, x1, x2, ni, t, i+1, l)
  return l


def imprimeBis(f, a, b, ni, t, j=0, i=0, L=[]):
  """
  Esta função imprime o resultado do método da bisseção na tela
  """
  if ni > i:
    if j == 0:
      bis = bissecao(f, a, b, ni, t)
      L = bis
      print("==> Método da Bisseção:")
      print("-"*68)
      print("i\t\t\t  raiz  \t\t\terro")
      print("-"*68)
    print("{}\t\t{:0<20}\t\t{:0<20}".format(i+1,L[i+j],L[i+1+j]))
    return imprimeBis(f, a, b, ni, t, j+1, i+1, L)


def imprimeNew(f, a, b, ni, t, j=0, i=0, L=[]):
  """
  Esta função imprime o resultado do método de Newton na tela
  """
  if ni > i:
    if j == 0:
      new = newtonRaphson(f, a, b, ni, t)
      L = new
      print("==> Método de Newton Raphson:")
      print("-"*68)
      print("i\t\t\t  raiz  \t\t\terro")
      print("-"*68)
    print("{}\t\t{:0<20}\t\t{:0<20}".format(i+1,L[i+j],L[i+1+j]))
    return imprimeNew(f, a, b, ni, t, j+1, i+1, L)


def imprimeSec(f, a, b, ni, t, j=0, i=0, L=[]):
  """
  Esta função imprime o resultado do método da secante na tela
  """
  if ni > i:
    if j == 0:
      sec = secante(f, a, b, ni, t)
      L = sec
      print("==> Método da Secante:")
      print("-"*68)
      print("i\t\t\t  raiz  \t\t\terro")
      print("-"*68)
    print("{}\t\t{:0<20}\t\t{:0<20}".format(i+1,L[i+j],L[j+1+i]))
    return imprimeSec(f, a, b, ni, t, j+1, i+1, L)


def separarValores(L, ni, x1=[],x2=[], i=0, j=0):
  if ni > i:
    return separarValores(L, ni, x1+[L[i+j]], x2+[L[j+1+i]], j+1, i+1)
  return x1, x2


def main():
  imprimeBis(lambda x: 3**x - 5*x, 1,2,8,10**-15)
  imprimeNew(lambda x: 3**x - 5*x, lambda y: (y ** 3) * math.log(3),2,6,10**-15)
  imprimeSec(lambda x: 3**x - 5*x, 1,2,7,10**-15)
 
main()
