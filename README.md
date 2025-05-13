#  Calculadora de IR Retido na Fonte (Versão Executável)

##  Descrição
Este programa calcula automaticamente o **Imposto de Renda Retido na Fonte (IRRF)** com base na **renda** informada pelo usuário. 
Ele aplica a **alíquota** correta e subtrai a **parcela dedutível**, exibindo os valores de forma organizada.

Agora você pode rodar o programa como um **executável (`.exe`)**, sem necessidade de instalar Python! 

##  Como funciona?
O programa realiza o seguinte cálculo passo a passo:
1. O usuário **insere sua renda**.
2. O sistema identifica a **faixa de tributação** correspondente.
3. Com base na faixa, ele aplica:
   - **Valor Base (`Vb`)** → Multiplicação da renda pela alíquota aplicável: `Vb = Renda * Alíquota`
   - **Imposto Retido (`Vir`)** → Subtração da parcela dedutível: `Vir = Vb - Parcela`
4. Exibe os valores detalhados no terminal.

##  Faixas do IRRF
| Faixa de Renda (`R`) | Alíquota (`A`) | Parcela Dedutível (`P`) |
|----------------------|---------------|--------------------------|
| `R <= 2259.20`      | 0%            | R$ 0,00                  |
| `2259.21 <= R <= 2828.65` | 7.5%   | R$ 169.44                |
| `2828.66 <= R <= 3751.05` | 15%    | R$ 381.44                |
| `3751.06 <= R <= 4664.68` | 22.5%  | R$ 662.77                |
| `R > 4664.68`       | 27.5%         | R$ 896.00                |

##  Tecnologias Utilizadas
- **Python 3.x** (convertido para `.exe`)
- Interface em **terminal** (modo texto)
- **Tratamento de exceções** (`try-except`) para evitar entradas inválidas
- Formatação de saída com **`f-strings`**

##  Como executar?
1. **Baixe** o arquivo executável `Calculadora_IRRF.exe`.
2. **Abra** o executável clicando duas vezes ou via prompt de comando (`cmd`).
3. Insira sua **renda** quando solicitado.
4. Veja os cálculos do **IR retido** imediatamente!

##  Melhorias futuras
- Criar uma **versão com interface gráfica (GUI)**.
- Permitir a **exportação dos resultados em PDF ou CSV**.
- Implementar suporte para outros cálculos jurídicos.

---
raphacgon
