# Sistema de Cotação de Moedas

Aplicação desktop em Python (Tkinter) para consulta de cotações de moedas estrangeiras. Este é o primeiro estágio do projeto: a interface gráfica base, com seleção de moeda pré-definida. A integração com uma API de cotação em tempo real está planejada para as próximas versões.

## Status do projeto

🚧 Em desenvolvimento — versão inicial (somente interface)

## Funcionalidades atuais

- Tela de boas-vindas com imagem de fundo
- Tela de busca com combobox contendo moedas pré-definidas (código + nome)
- Estrutura orientada a objetos (classe `AppCotacao`), evitando variáveis globais

## Moedas disponíveis (versão atual)

| Código | Moeda               |
|--------|----------------------|
| USD    | Dólar Americano      |
| EUR    | Euro                 |
| GBP    | Libra Esterlina      |
| JPY    | Iene Japonês         |
| BRL    | Real Brasileiro      |
| CAD    | Dólar Canadense      |
| AUD    | Dólar Australiano    |
| CHF    | Franco Suíço         |

## Tecnologias utilizadas

- Python 3
- Tkinter / ttk (interface gráfica)

> É necessário ter uma imagem em `./img/fundo_2.png` para a tela inicial carregar corretamente.

## Próximos passos

- [ ] Integrar API pública de cotação de moedas
- [ ] Exibir o resultado da cotação na tela após a busca
- [ ] Tratar erros de conexão e moeda inválida
- [ ] Adicionar histórico de consultas
- [ ] Melhorar o design da interface

## Autor

Thiago