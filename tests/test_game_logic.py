from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_message_direction():
    # guess above secret should tell the player to go lower
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_numeric_not_string_comparison():
    # "9" > "50" as text, but 9 < 50 as numbers
    assert check_guess(9, 50)[0] == "Too Low"