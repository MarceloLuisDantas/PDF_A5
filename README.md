# PDF_A5
## Organizador de PDF para imprimir em A5, frente e verso.

Por acaso você já quis imprimir um PDF para ler ele físico, porém imprimir em A4 ficaria comicamente grande, então você quis imprimir em A5 frente e verso? Se sim, você foi na gráfica e pediu para fazer isso, e eles não conseguiam imprimir em A5 de um modo em que as folhas ficassem na ordem correta? Eu passei por isso hoje e, só de raiva, fiz esse script Python para reordenar as páginas de um PDF para fazer uma impressão A5, frente e verso, onde você só precisa cortar a folha no meio e jogar o lado direito para baixo.

Ao imprimir a folha A4 com as páginas do PDF em A5 frente e verso, cada folha irá ficar com 4 páginas. Imprimindo o PDF normal, a primeira página irá ficar à esquerda da primeira folha, e a segunda página à direita da primeira folha, em vez de ficar atrás da primeira folha, e assim todas as folhas ficam fora de ordem para frente e verso. Para resolver este grande problema da nossa geração, este script divide o PDF em 2 pilhas, a primeira e a segunda metade, e intercala as páginas das duas pilhas.

## Demonstração 100% necessaria que você com certeza vai ler:
Em um PDF de 10 páginas, a ordem de normal de: 

` 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 `

Ao imprimir em A5 frente e verso, ficaria na seguinte ordem: 

` 1 -> 3 -> 5 -> 7 -> 9 -> 2 -> 4 -> 6 -> 8 -> 10 ` 

No melhor dos casos, caso você organize as folhas e não apenas dividir no meio, e jogar a metade da direita pro fundo, poderia ficar assim: 

` 1 -> 3 -> 2 -> 4 -> 5 -> 7 -> 6 -> 8 -> 9 -> 10 `

Ainda assim ficaria horrível de ler caso a ordem das páginas importe. Ao intercalar a primeira metade com a segunda metade, garante que, ao imprimir as páginas como A5 em uma folha A4, todas as páginas estejam alinhadas. Então, a ordem:

` 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 ` 

ao ser reorganizada como: 

` 1 -> 6 -> 2 -> 7 -> 3 -> 8 -> 4 -> 9 -> 5 -> 10 `

ao imprimir frente e verso, cortar as folhas ao meio e jogar a pilha da direita para baixo da pilha da esquerda, ficará na ordem correta.

## Rodar
```bash
> git clone https://github.com/MarceloLuisDantas/PDF_A5.git
> cd PDF_A5
> .venv/bin/python main.py PDF_NAME.pdf
PDF exportado com sucesso: PDF_NAME_A5.pdf
> 
```
