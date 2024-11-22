**Questão**: 

Imagine que você está desenvolvendo um jogo baseado no universo de *Sonic the Hedgehog*. Para isso, você precisa modelar os personagens e alguns elementos básicos do jogo utilizando conceitos de POO. 

1. Crie uma classe chamada `Personagem` que tenha os seguintes atributos e métodos:
   - **Atributos**:
     - `nome` (o nome do personagem, como Sonic, Tails ou Knuckles)
     - `velocidade` (velocidade máxima do personagem, em números inteiros)
     - `energia` (um valor de energia, entre 0 e 100)
   - **Métodos**:
     - `correr()`: Reduz a energia em 10 unidades e imprime uma mensagem dizendo que o personagem está correndo na velocidade atual.
     - `descansar()`: Aumenta a energia em 20 unidades (não ultrapassando 100) e imprime uma mensagem dizendo que o personagem está descansando.

2. Agora, crie uma classe derivada chamada `Inimigo` que herde de `Personagem`. Adicione os seguintes comportamentos:
   - Um atributo adicional `ataque` (um número inteiro que representa o poder de ataque do inimigo).
   - Um método chamado `atacar()` que imprime uma mensagem indicando que o inimigo está atacando com um poder específico.

**Tarefa**: 
Baseado nas classes acima:
- Instancie um objeto do tipo `Personagem` representando o Sonic, com `velocidade = 100` e `energia = 80`.
- Faça o Sonic correr duas vezes e depois descansar.
- Instancie um objeto do tipo `Inimigo` representando o Dr. Robotnik, com `velocidade = 20`, `energia = 50`, e `ataque = 30`.
- Faça o Dr. Robotnik atacar e depois descansar.

Escreva o código necessário para implementar e testar as classes acima.

---

**Bônus**: Como você poderia usar o conceito de **polimorfismo** para permitir que tanto `Personagem` quanto `Inimigo` possam ser tratados de forma genérica, mas com comportamentos diferentes?