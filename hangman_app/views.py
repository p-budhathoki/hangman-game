import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import HangmanGame


def index(request):
    return render(request, "index.html")


def new_game(request):
    words = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]
    selected_word = random.choice(words)
    max_incorrect_guesses = len(selected_word) // 2
    game = HangmanGame.objects.create(
        word=selected_word, max_incorrect_guesses=max_incorrect_guesses
    )
    return JsonResponse({"id": game.id})


def game_state(request, game_id):
    game = HangmanGame.objects.get(id=game_id)
    state = get_game_state(game)
    return JsonResponse(state)


def guess(request, game_id, letter):
    print(letter)
    game = HangmanGame.objects.get(id=game_id)
    print(game.word)
    if game.status == "InProgress":
        if letter not in game.guessed_letters:
            game.guessed_letters += letter
            if letter not in game.word:
                game.incorrect_guesses += 1
            game.save()
    state = get_game_state(game)
    response_data = {"game_state": state, "correct_guess": letter in game.word}
    return JsonResponse(response_data)


def get_game_state(game):
    masked_word = "".join(
        [letter if letter in game.guessed_letters else "_" for letter in game.word]
    )
    status = game.status
    if "_" not in masked_word:
        status = "Won"
    elif game.incorrect_guesses >= game.max_incorrect_guesses:
        status = "Lost"
    state = {
        "status": status,
        "word_state": masked_word,
        "incorrect_guesses_made": game.incorrect_guesses,
        "incorrect_guesses_allowed": game.max_incorrect_guesses,
    }
    return state
