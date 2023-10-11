
document.addEventListener('DOMContentLoaded', function() {
        const startGameButton = document.getElementById('start-game-btn');
        const guessButton = document.getElementById('guess-btn');
    
        startGameButton.addEventListener('click', startNewGame);
        guessButton.addEventListener('click', makeGuess);
    
    let gameId = null;

    function startNewGame() {
        fetch('/game/new/')
            .then(response => response.json())
            .then(data => {
                gameId = data.id;
                updateGameUI();
            });
    }

    function updateGameUI() {
        fetch(`/game/${gameId}/`)
            .then(response => response.json())
            .then(data => {
                const wordStateElement = document.getElementById('word-state');
                const guessesLeftElement = document.getElementById('guesses-left');
                const messageElement = document.getElementById('message');

                wordStateElement.textContent = `Word: ${data.word_state}`;
                guessesLeftElement.textContent = `Incorrect Guesses Left: ${data.incorrect_guesses_allowed - data.incorrect_guesses_made}`;

                if (data.status === 'Won') {
                    messageElement.textContent = 'Congratulations! You won!';
                } else if (data.status === 'Lost') {
                    messageElement.textContent = 'Game Over. The word was: ' + data.word_state;
                } else {
                    messageElement.textContent = '';
                }
            });
    }

    function makeGuess() {
        const guessInput = document.getElementById('guess-input');
        console.log(guessInput.value);
        const letter = guessInput.value;
        const messageContainer = document.getElementById('message-container');
    
        if (letter.match(/[a-zA-Z]/) && letter.length === 1) {
            fetch(`/game/${gameId}/guess/${letter}/`)
                .then(response => response.json())
                .then(data => {
                    updateGameUI();
                    guessInput.value = '';
                    const message = document.createElement('p');
    
                    if (data.correct_guess) {
                        if (data.game_state.status === 'Won') {
                            message.textContent = 'Congratulations! You guessed the word correctly!';
                        } else {
                            message.textContent = 'Correct guess! Keep going!';
                        }
                    } else {
                        if (data.game_state.status === 'Lost') {
                            message.textContent = `Game Over. The word was: ${data.game_state.word_state}`;
                        } else {
                            message.textContent = 'Incorrect guess! Try again!';
                        }
                    }
    
                    // Clear previous messages and display the new message
                    messageContainer.innerHTML = '';
                    messageContainer.appendChild(message);
                });
        } else {
            messageContainer.textContent = 'Please enter a valid single letter.';
        }
    }
    

    // Start a new game when the page loads
    startNewGame();
});

