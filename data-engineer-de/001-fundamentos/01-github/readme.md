Aqui inicia-se o processo de utilização e entendimento do github.
Quais passos devemos efetuar para que possamos efetuar o versionamento das pastas e arquivos utilizando o github via VS Code.

Os pricipais passos são:
    Criar um repositório no site do github, de preferência com o nome da pasta mãe, ou seja, um nome agrupador
    Criar uma pasta dentro da máquina em um local mais restrito. No meu caso criei dentro do caminho abaixo no linux ubuntu via WSL:
       
        > home
            > crcaldascampos
                > github
                    > .git ---------------> pasta do sistema git
                    > .gitconfig ---------> arquivo do sistema git
                    > .gitignore ---------> arquivo do sistema git
                    > requirements.txt ---> arquivo de requisições do python
                    > data-engineer-de ---> pata mãe que armazenará tudo atrelado aos módulos da especialização de data engineer
                        > 001-fundamentos > pasta do módulo de fundamentos
                            > 001-01-github
                        
                        > python ---------> mais para frente numerar essa pasta