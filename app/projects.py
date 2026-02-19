class Projeto:
    def __init__(self, nome, desc, tecnologias, link1, link2, imagem):
        self.nome = nome
        self.desc = desc
        self.tecnologias = tecnologias
        self.link1 = link1
        self.link2 = link2
        self.imagem = imagem

blog = Projeto("Blog em Flask", 
               "Blog pessoal desenvolvido com Flask com suporte Markdown.", 
               "Python, Flask, HTML, Bootstrap, Markdown", 
               "https://github.com/Welontom/Blog-Pessoal",
               None, 
               "static/img/blog.png")

arvore_decisao = Projeto("Árvore AVL e Árvores de Decisão",
                "O projeto consiste em um método para classificar 3 tipos de flores iris: setosa, versicolor e virginica a partir do comprimento e largura das sépalas e pétalas já conhecidas.", 
                "Python, Matplotlib, Pandas, Sklearn",
                "https://github.com/Welontom/Arvore-de-decisao-Iris",
                None,
                "static/img/arvore_decisao.png")

crud = Projeto("CRUD em C#",
                "Aplicação desktop para gerenciamento de bibliotecas utilizando C# Windows Forms e MariaDB como banco de dados.", 
                "C#, SQL, MariaDB",
                "https://github.com/Welontom/TrabalhoCRUD",
                None, 
                "static/img/crud.png")

bingo = Projeto("Bingo",
                "Um dos meus primeiros projetos de computação! Bingo virtual para web.", 
                "HTML, CSS, JavaScript",
                "https://github.com/Welontom/Bingo",
                "https://welontom.github.io/Bingo/",
                "static/img/bingo.png")


projetos = [blog,arvore_decisao,crud,bingo,]