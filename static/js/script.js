document.addEventListener("DOMContentLoaded", function() {
    // Função para remover o foco:
    function removeFocus(button) {
        // Remove o foco do botão após 300ms.
        setTimeout(() => {
            button.blur(); // Remove o foco do botão.
        }, 300); // Tempo em milissegundos.
    };

    // Função que lida com o clique nos botões de favoritos:
    function favoritedClick() {
        // Seleciona todos os botões com a classe "fav-heart-btn".
        const buttons = document.querySelectorAll('.fav-heart-btn');

        // Adiciona um evento de clique para cada botão.
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                const heartIcon = button.querySelector('.heart-icon'); // Seleciona o ícone de coração dentro do botão.
                
                // Alterna a classe 'active' no ícone de coração.
                heartIcon.classList.toggle('active');

                // Adiciona foco e remove após 300ms.
                button.classList.add('focused');
                removeFocus(button);
            });
        });
    }

    // Função para mostrar apenas os Pokémon favoritos:
    function showFavoritedPokemons() {
        const cards = document.querySelectorAll('.pokemon-card'); // Seleciona todos os cards de Pokémon.

        cards.forEach(card => {
            const heartIcon = card.querySelector('.heart-icon'); // Seleciona o ícone de coração dentro do card.

            // Verifica se o ícone de coração tem a classe 'active'.
            if (heartIcon.classList.contains('active')) {
                card.style.display = ''; // Mostra o card se for favorito.
            } else {
                card.style.display = 'none'; // Esconde o card se não for favorito.
            }
        });
        removeFocus(this);
    }

    // Função para filtrar os cards de Pokémon pela geração selecionada:
    function filterByGeneration() {
        const select = document.getElementById('genList'); // Obtém o elemento select que contém as gerações.
        const selectedGeneration = select.value; // Obtém a geração selecionada.
        const cards = document.querySelectorAll('.pokemon-card'); // Seleciona todos os cards de Pokémon.

        cards.forEach(card => {
            // Verifica se o card pertence à geração selecionada.
            if (selectedGeneration === "0") {
                // Se "0" for selecionado, mostra todos os cards.
                card.style.display = ''; // Mostra o card.
            } else if (card.classList.contains(`gen-${selectedGeneration}`)) {
                // Se a classe do card contém a geração selecionada, mostra o card.
                card.style.display = '';
            } else {
                // Caso contrário, esconde o card.
                card.style.display = 'none';
            }
        });
    }

    // Função para inverter a ordem dos Pokémon:
    function invertList() {
        // Seleciona a linha que contém os Pokémon.
        const pokemonContainer = document.getElementById('pokemonContainer').querySelector('.row'); // Seleciona a linha que contém os Pokémon.
        const pokemons = Array.from(pokemonContainer.children); // Obtém todos os filhos da linha como um array.

        // Inverte a ordem dos Pokémon.
        pokemons.reverse().forEach(pokemon => {
            pokemonContainer.appendChild(pokemon); // Reanexa cada Pokémon na nova ordem.
        });
        removeFocus(this);
    };

    // Função para pesquisar pokémons:
    function searchPokemon() {
        // Obtém o valor do input de pesquisa.
        const input = document.getElementById('searchInput'); // Seleciona o campo de entrada de pesquisa.
        const filter = input.value.toLowerCase(); // Converte o valor do input para minúsculas.
        
        // Obtém todos os elementos com a classe card.
        const cards = document.querySelectorAll('.pokemon-card'); // Seleciona todos os cards de Pokémon.

        // Loop através de todos os elementos card.
        cards.forEach(card => {
            const cardTitle = card.querySelector('.card-title'); // Seleciona o título do card.
            const cardNumber = card.querySelector('.card-number'); // Seleciona o número do card.

            // Verifica se o texto do card contém o valor do input.
            if (cardTitle.textContent.toLowerCase().includes(filter) || cardNumber.textContent.toLowerCase().includes(filter)) {   
                // Exibe o card se o texto corresponder.
                card.style.display = '';
            } else {
                // Oc ulta o card se o texto não corresponder.
                card.style.display = 'none';
            }
        });
    }

    // Função para limpar a pesquisa e restaurar os cards:
    function clearSearch() {
        const input = document.getElementById('searchInput');
        input.value = ''; // Limpa o campo de entrada.

        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            card.style.display = ''; // Restaura a exibição de todos os cards.
        });

        const select = document.getElementById('genList'); // Seleciona o elemento select de gerações.
        select.value = "0"; // Define o valor do select para "0", que representa a opção "All".

        filterByGeneration(); // Chama a função para filtrar os cards pela geração.
        removeFocus(this);
    }

    // Função para alternar entre o modo claro e o modo escuro:
    const darkModeBtn = document.getElementById("darkModeBtn");
    const body = document.body;

    // Função para alternar o modo escuro
    function toggleDarkMode() {
        body.classList.toggle("dark-mode");

        const sunIcon = document.getElementById("sunIcon");
        const moonIcon = document.getElementById("moonIcon");

        if (body.classList.contains("dark-mode")) {
            sunIcon.style.display = "none";
            moonIcon.style.display = "block";
        } else {
            sunIcon.style.display = "block";
            moonIcon.style.display = "none";
        }
    }

    // Adiciona o evento de clique ao botão
    darkModeBtn.addEventListener("click", toggleDarkMode);

    // Chamar as funções:
    favoritedClick();
    document.getElementById('searchInput').addEventListener('keyup', searchPokemon);
    document.getElementById('invertListBtn').addEventListener('click', invertList);
    document.getElementById('clearBtn').addEventListener('click', clearSearch);
    document.getElementById('genList').addEventListener('change', filterByGeneration);
    document.getElementById('favListBtn').addEventListener('click', showFavoritedPokemons);
});