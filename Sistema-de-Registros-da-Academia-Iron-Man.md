# Documento de Visão

## Sistema de Registros da Academia Iron Man
## Documento de Visão

### Histórico da Revisão

### Histórico da Revisão 

|  Data  | Versão | Descrição | Autores |
|:-------|:-------|:----------|:------|
| 19/06/2021 |  **`1.00`** | Versão Inicial  | Icaro Gabriel e Flávio Matias |


### 1. Objetivo do Projeto 

O projeto __Sistema de Registros da Academia Iron Man__ tem como objetivo desenvolver um sistema de gestão para a academia, que auxilie no controle das matrículas e pagamentos dos alunos. Através da plataforma, será possível monitorar diariamente o status financeiro de cada aluno, garantindo o acompanhamento eficiente de quem está ativo e regular com suas mensalidades. Além disso, o sistema fornecerá dados específicos de cada aluno, como suas medidas corporais e histórico de treinos, possibilitando um acompanhamento personalizado e mais eficiente no planejamento dos treinos e evolução física.

### 2. Descrição do Problema 

|         __        | __   |
|:------------------|:-----|
| **_O problema_**    | Há dificuldade em controlar os alunos, seus pagamentos e seus treinos. Muitos alunos podem acabar treinando sem pagar ou esquecer o treino do dia, o que prejudica o acompanhamento e o progresso.  |
| **_afetando_**      | Isso afeta principalmente os alunos, que ficam sem saber exatamente o que treinar ou não têm um histórico claro de seu desempenho ao longo do tempo. Também impacta os funcionários e o dono, que perdem o controle financeiro e do progresso dos alunos. |
| **_cujo impacto é_**| A falta de organização gera confusão, perda de dinheiro, e alunos desmotivados ou sem um plano de treino claro. Além disso, a dependência dos instrutores para lembrar os treinos compromete a autonomia e os resultados dos alunos. |
| **_uma boa solução seria_** | Um sistema que centralize as informações de matrícula, pagamentos e treinos. Isso permitiria que os alunos soubessem exatamente o que treinar e ajudaria a academia a controlar de forma eficiente quem está pagando e treinando, garantindo mais organização e motivação para todos. |

### 3. Descrição dos Usuários

| Nome | Descrição | Responsabilidades |
|:---  |:--- |:--- |
| Administrador  | O administrador é o responsável pela operação completa do sistema, tendo acesso total a todas as funcionalidades. Ele gerencia todos os dados e informações da academia. | O administrador tem controle sobre as matrículas dos alunos, seus treinos, medidas, vencimentos e pagamentos. Ele também pode editar e atualizar informações dos alunos, além de gerar relatórios financeiros.|
| Cliente  | O cliente é o aluno da academia que utiliza o sistema para acessar suas informações pessoais e financeiras. | O cliente pode visualizar suas informações de treino, medidas corporais e histórico de pagamentos. Além disso, ele tem a capacidade de realizar o pagamento das mensalidades diretamente pelo sistema. |
| Visitante | O visitante é alguém que tem acesso limitado ao sistema sem a possibilidade de realizar qualquer ação dentro da plataforma. | O visitante pode acessar o sistema, mas não tem permissão para visualizar informações privadas, fazer pagamentos ou alterar qualquer dado. |

### 4. Descrição do Ambiente dos Usuários

Muitas pessoas, por diversos motivos, têm dificuldades em lembrar quais treinos realizar ou o que está programado para o dia. Isso pode resultar em desorganização e até mesmo em perda de foco. Com o uso do aplicativo, os alunos poderão conferir seus treinos diretamente na plataforma, sem a necessidade de lembrar ou depender de anotações manuais. O sistema proporciona um acompanhamento claro e prático dos exercícios diários.

Além disso, um grande motivador para que as pessoas mantenham a disciplina e o foco nos treinos é ver seu desempenho ao longo do tempo. O aplicativo registra o progresso de cada aluno, permitindo que ele visualize sua evolução e compare resultados passados. Esse acompanhamento contínuo ajuda na motivação, mostrando a evolução do físico e do desempenho nos treinos.

Outro aspecto importante do sistema é a possibilidade de consultar as datas de vencimento das mensalidades e realizar os pagamentos diretamente pelo aplicativo. Isso facilita o controle financeiro tanto para o aluno quanto para a academia, garantindo que os pagamentos sejam feitos pontualmente, sem a necessidade de interações manuais ou correções posteriores.

### 5. Principais Necessidades dos Usuários

Para a academia e seus administradores, a principal necessidade é ter uma ferramenta eficiente para controlar as matrículas, pagamentos, e os treinos dos alunos, garantindo que todas as informações sejam organizadas de maneira centralizada e acessível. Isso inclui o gerenciamento das datas de vencimento das mensalidades, o acompanhamento da evolução física dos alunos e a programação dos treinos.

Para os alunos, as necessidades são acessar facilmente os detalhes de seus treinos diários, acompanhar o seu progresso ao longo do tempo e garantir que seus pagamentos sejam feitos de forma rápida e prática. Além disso, os alunos buscam uma plataforma que os ajude a manter o foco e a motivação, oferecendo um registro claro do seu desempenho e das suas atividades.

### 6.	Alternativas Concorrentes

As alternativas concorrentes geralmente são sistemas ou soluções que atendem a academias específicas ou que focam em uma parte do gerenciamento, como controle de pagamentos ou agendamento de treinos. Muitas dessas soluções ainda dependem de processos manuais ou não oferecem uma integração completa entre as informações dos alunos, seus treinos e pagamentos. A proposta do sistema é fornecer uma plataforma única, acessível e integrada, que reúna todos esses aspectos em um só lugar, atendendo tanto às necessidades dos administradores quanto dos alunos de maneira prática e eficiente.

### 7.	Visão Geral do Produto

Em resumo, o sistema da academia é uma aplicação que permite aos administradores gerenciar as informações dos alunos, incluindo suas matrículas, treinos, medidas e pagamentos. Os alunos, por sua vez, podem consultar seus treinos diários, acompanhar seu desempenho ao longo do tempo e realizar o pagamento das mensalidades diretamente pelo aplicativo.

O sistema deve ter uma interface intuitiva e de fácil navegação, proporcionando acesso rápido e simples para os alunos visualizarem seus dados e registrarem os pagamentos, além de permitir que os administradores gerenciem todas as informações de forma centralizada e eficiente.

### 8. Requisitos Funcionais

| Código | Nome | Descrição |
|:---  |:--- |:--- |
| RF01 | Entrar na conta | Visitante acessa a plataforma para fazer login e entrar no sistema. |
| RF02 | Cadastrar aluno | Admin cadastra novos alunos no sistema. |
| RF03 | Visualizar e editar dados dos alunos |  Admin pode visualizar e editar informações dos alunos cadastrados. |
| RF04 | 	Matricular aluno | Admin matricula alunos na academia, gerando suas respectivas datas de pagamento. |
| RF05 | Visualizar e editar matrículas | Admin pode visualizar e editar informações sobre as matrículas dos alunos. |
| RF06 | Criar, editar e visualizar treinos dos alunos | Admin cria, edita e visualiza treinos personalizados para os alunos. |
| RF07 | Criar, editar e visualizar medidas dos alunos | Admin cria, edita e visualiza as medidas corporais dos alunos. |
| RF08 | Criar planos de pagamento | Admin cria planos de pagamento, oferecendo diferentes opções para os alunos. |
| RF09 | Visualizar e editar planos de pagamento | Admin pode visualizar e editar os planos de pagamento existentes. |
| RF10 | Criar novo grupo muscular | Admin pode criar novos grupos musculares para a personalização de treinos. |
| RF11 | Criar nova medida | Admin pode criar novas medidas corporais para acompanhamento dos alunos. |
| RF12 | Renovar matrícula do aluno | Admin renova a matrícula dos alunos para novo período de pagamento. |
| RF13 | Cancelar matrícula do aluno | Admin cancela a matríca dos alunos em caso de atraso ou desistência. |
| RF14 | Registrar pagamento do aluno | Admin registra os pagamentos dos alunos, garantindo que não haja cobranças pendentes. |
| RF15 | Visualizar e alterar dados da conta | Cliente pode visualizar e alterar seus dados cadastrais na plataforma. |
| RF16 | Visualizar medidas | ACliente pode visualizar suas medidas corporais registradas no sistema. |
| RF17 | Visualizar ficha de treino | Cliente pode consultar sua ficha de treino personalizada. |
| RF18 | Visualizar e pagar mensalidade | Cliente pode visualizar e pagar suas mensalidades de forma online. |
| RF19 | Visualizar matrícula | ACliente pode verificar os dados da sua matrícula, incluindo status e data de renovação. |
| RF20 | Visualizar planos de pagamento | Cliente pode consultar os planos de pagamento disponíveis e sua adesão a eles. |


### 9. Requisitos Não-funcionais

 Código | Nome | Descrição | Categoria | Classificação
|:---  |:--- |:--- |:--- |:--- |
| RNF01 | Design responsivo | O sistema deve adaptar-se a qualquer tamanho de tela de dispositivo, seja, computador, tablets ou smart phones. | Usabilidade| Obrigatório |
| RNF02 | Controle de acesso | Só usuários autenticados podem ter acesso ao sistema, com exceção ao auto cadastramento do usuário. | Segurança | Obrigatório |
| RNF03 | Aplicativo | A aplicação deve ser um aplicativo executável. | Arquitetura | Obrigatório |
| RNF04 | Dados pessoais | Os clientes não devem visualizar dados de outros clientes. | Privacidade | Obrigatório |
