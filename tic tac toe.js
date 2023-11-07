 // JavaScript code for the Tic Tac Toe game
        const cells = document.querySelectorAll('.cell');
        let currentPlayer = 'X';

        cells.forEach(cell => {
            cell.addEventListener('click', () => {
                if (cell.textContent === '') {
                    cell.textContent = currentPlayer;
                    cell.classList.add(currentPlayer.toLowerCase());
                    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
                }
            });
        });

