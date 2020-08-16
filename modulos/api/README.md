# API Rest com Flask

O Flask em sua essência procura manter uma estrutura simples mas extensível.
De forma que muitas das decisões e funcionalidades sejam escolhidas por você ao 
escolher usar determinada biblioteca para integração com um banco de dados específico, por exemplo.

- WerkZeug - Implementa Web Server Gateway Interface (WSGI)
- Jinja2 - Template engine escrito em Python para marcações como {{ nome_da_variavel }} 

### Views
"O Flask através do WerkZeug abstrai uma boa parte 
deste trabalho tornando isto uma tarefa bastante trivial,
 por baixo dos panos quando usamos o decorator @app.route 
 na verdade estamos alimentando uma lista de mapeamento do 
 Werkzeug implementada pelo werkzeug.routing.Map e esta 
 lista de mapeamento contém elementos do tipo Rule que 
 é justamente a regra que liga uma url com uma função 
 Python em nosso projeto."
 
 "Views precisam retornar um objeto do tipo Response ou 
 uma tupla formada por até 3 elementos, um body que pode 
 ser um objeto serializável como por exemplo um texto, 
 um inteiro representando o código de status HTTP e 
 um dicionário de headers, sendo que os dois ultimos 
 elementos são opcionais."
 
 "Retornar uma tupla de 3 elementos, no formato
  (string, status_code, headers_dict)"