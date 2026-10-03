# Sistema de Cotação de Moedas

Aplicação desktop em Python (Tkinter) para consulta de cotações de moedas estrangeiras. A aplicação já realiza buscas reais de cotação via API, mantém um histórico das consultas feitas na sessão e permite exportar esse histórico para Excel ou TXT.

## Status do projeto

🚧 Em desenvolvimento — interface, busca de cotação, histórico e exportação já funcionam

## Funcionalidades atuais

- Tela de boas-vindas com painel em tom teal escuro e detalhe em dourado, sem depender de nenhuma imagem externa
- Tela de busca com combobox contendo moedas pré-definidas (código + nome)
- Busca de cotação em tempo real através da API pública [Frankfurter](https://frankfurter.dev)
- Tratamento de erros de conexão com a API (sem internet, timeout, API fora do ar) e validação de seleção vazia
- Histórico das cotações consultadas na sessão, exibido em uma tabela (com barra de rolagem)
- Exportação do histórico para planilha Excel (`.xlsx`) ou arquivo de texto (`.txt`)
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
- [requests](https://pypi.org/project/requests/) (consumo da API de cotação)
- [openpyxl](https://pypi.org/project/openpyxl/) (exportação do histórico para Excel)

### Instalação das dependências

```bash
pip install requests openpyxl
```

## Próximos passos

- [x] Integrar API pública de cotação de moedas
- [x] Exibir o resultado da cotação na tela após a busca
- [x] Tratar erros de conexão
- [x] Adicionar histórico de consultas
- [x] Adicionar exportação do histórico (Excel e TXT)
- [x] Melhorar o design da tela de boas-vindas
- [ ] Melhorar o design da tela principal (busca e histórico)
- [ ] Persistir o histórico entre execuções do programa
- [ ] Adicionar mais moedas à lista de opções

## Autor

Thiago