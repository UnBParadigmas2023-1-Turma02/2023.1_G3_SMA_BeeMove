## Os agentes
### Abelha Rainha

### Zangao

### Operaria

### Flor

A classe Flor herda a classe Agent do módulo mesa. Essa classe representa uma flor em um modelo de simulação. Sendo que representa o alimento da abelha rainha, fornecendo o nectar.

##### Atributos:

pos: Representa a posição da flor no modelo. Pode ser uma coordenada (x, y) ou outro formato de representação de posição.

nectar: Representa a quantidade de néctar da flor.

tipo: Uma string que indica o tipo da entidade, no caso, "Flor".

##### Métodos:

O construtor da classe recebe um ID atual, uma instância do modelo, a posição da flor, a quantidade inicial de néctar e o tipo da flor. O construtor chama o construtor da classe pai (Agent) e inicializa os atributos da flor.

O método step() é chamado a cada passo da simulação. Neste caso, ele verifica se a quantidade de néctar da flor é menor ou igual a zero e, caso seja verdadeiro, chama o método remove_flor para remover a flor do modelo.

O método remove_flor() remove a flor do modelo chamando o método remove_agent do objeto grid do modelo, se a posição da flor não for None.

O método come() diminui a quantidade de néctar da flor em uma unidade.


##### Código: 

![Screenshot1](../assets/codigo_flor.png)

### Model

### Graficos
