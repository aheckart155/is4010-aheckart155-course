# test_lab03.py
import random
from unittest.mock import patch
from week03.lab03 import generate_mad_lib, guessing_game

def test_generate_mad_lib():
    """
    Tests the generate_mad_lib function to ensure it uses the inputs correctly.
    """
    adj = "silly"
    noun = "cat"
    verb = "jumped"

    story = generate_mad_lib(adj, noun, verb)

    assert isinstance(story, str), "Function must return a string"

    story_lower = story.lower()
    assert adj.lower() in story_lower, f"Adjective '{adj}' not found in story"
    assert noun.lower() in story_lower, f"Noun '{noun}' not found in story"
    assert verb.lower() in story_lower, f"Verb '{verb}' not found in story"

    assert len(story) > 0, "Story cannot be empty"

def test_guessing_game_correct_guess():
    """
    Tests the guessing_game function with a correct guess.
    """
    with patch('week03.lab03.random.randint', return_value=50):

        with patch('builtins.input', return_value='50'):

            with patch('builtins.print') as mock_print:
                guessing_game()


                assert mock_print.called, "Function should print output"

                print_calls = [str(call) for call in mock_print.call_args_list]


                output_text = ' '.join(print_calls).lower()
                assert any(word in output_text for word in ['correct', 'right', 'won', 'yes', 'congratulations']), \
                    "Function should indicate correct guess"

def test_guessing_game_multiple_guesses():
    """
    Tests the guessing_game function with multiple incorrect guesses before correct.
    """

    with patch('week03.lab03.random.randint', return_value=42):

        with patch('builtins.input', side_effect=['30', '50', '42']):
            with patch('builtins.print') as mock_print:
                guessing_game()

                assert mock_print.called, "Function should print output"

                assert mock_print.call_count >= 3, \
                    "Function should print feedback for each guess"
