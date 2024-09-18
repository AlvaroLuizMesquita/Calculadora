Este projeto é uma calculadora simples implementada em Python. A calculadora permite ao usuário realizar operações básicas: adição, subtração, multiplicação e divisão. A interface é de linha de comando, onde o usuário escolhe a operação e insere os números desejados.
Funcionalidades

Exibição do Nome do Projeto: O programa inicia com uma arte ASCII que representa o nome da calculadora.
•	Operações Matemáticas: O usuário pode escolher entre quatro operações:
•	Adição
•	Subtração
•	Multiplicação
•	Divisão


Tratamento de Erros: A calculadora trata a tentativa de divisão por zero, retornando uma mensagem adequada ao usuário.
Estrutura do Código


Funções Principais
•	exebir_nome(): Exibe o nome do projeto em formato ASCII.
•	adicao(x, y): Retorna a soma de x e y.
•	subtracao(x, y): Retorna a subtração de y de x.
•	mulplicacao(x, y): Retorna o produto de x e y.
•	divisao(x, y): Retorna a divisão de x por y, tratando a divisão por zero.
•	opcoes(): Exibe as opções de operações disponíveis.
•	finalizar_app(): Limpa a tela e exibe uma mensagem de encerramento.
•	opcao_invalida(): Trata a entrada inválida e permite que o usuário retorne ao menu principal.
•	operacao(): Executa a operação escolhida pelo usuário e exibe o resultado.
•	main(): Função principal que coordena a execução do programa.



Esta calculadora é um projeto simples que pode ser expandido. Possíveis melhorias incluem:
Adicionar mais operações (ex: potência, raiz quadrada).
Implementar um loop para permitir múltiplas operações sem reiniciar o programa.
Melhorar o tratamento de erros e validações de entrada.
