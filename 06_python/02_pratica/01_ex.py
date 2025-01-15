nota1 = 7
nota2 = 8
nota3 = 8
# Declaramos as variáveis que recebem as notas. A tipagem é dinâmica, ou seja, os valores são atribuídos são considerados números inteiros por conta da sua formatação. Se estivessem entre aspas, por exemplo, seriam considerados string o se houvesse um ponto seriam considerados float

media = (nota1 + nota2 + nota3) / 3
# Declaramos a variável que armazena a média. O valor é definido por uma expressão matemática onde somamos todas as notas e dividimos pelo número de notas. Note que as somas estão entre parênteses para garantir a ordem de precedência das operações. Assim obtemos primeiro o valor total das notas antes de dividir. Caso contrário, a divisão seria realizada primeiro, causando um erro semântico (lógica), ao qual o Python não exibe mensagem de erro ou interrompe o programa.

# Usamos uma estrutura condicional para decidir qual mensagem será exibida a partir do resultado da expressão.

# A primeira condição verifica se a média é maior ou igual a 7. Caso seja, a expressão retorna um valor True e executa o comando que está dentro desse bloco de código, destacado pela identação e ignora as verificações posteirores.
if media >= 7:
	print("Aprovado")

# A segunda condição só é verificada caso a anterior não seja atendida. Ela verifica se o valor é maior ou igual a 5, mas implicitamente, menor que 7, pois os valores maiores que 7 já foram verificados antes, portanto o resultado é necessariamente menor que 7. Se essa condição for atendida, o comando dentro desse bloco será executado e finaliza a estrutura condicional.
elif media >= 5:
	print("Recuperação")

# Caso nenhuma das condições anteriores seja atendida, ou seja, se o valor for menor que 5, o bloco de código else é executado. Não precisamos de uma condição explícita aqui, pois, fica implícito que qualquer valor que seja menor que 5 resultará em True.
else:
	print("Reprovado")
	print("Boa sorte na próxima")