# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** This is a number guessing game built with Streamlit. The player guesses a secret number and the game gives hints until they win or run out of attempts. The starter code was written by AI and had several bugs.

**Bugs I found:**
- The hint messages were backwards. A guess that was too high told the player to go higher.
- On every even attempt, the secret was turned into a string, so numbers were compared as text ("9" > "50"). This made the hints wrong on every other guess.
- The New Game button did not reset the status, score, or history, so the game stayed stuck after a win or loss.
- The attempts counter started at 1, so it always showed one more attempt than I had actually made.
- On even attempts, a "Too High" guess added 5 to the score instead of taking points away.

**Fixes I applied:**
- I moved `check_guess` into `logic_utils.py` and swapped the hint messages so "Too High" says go lower and "Too Low" says go higher.
- I removed the `str(secret)` code in `app.py` so the guess and the secret are always compared as numbers.
- I updated the starter tests to read the outcome from the (outcome, message) result and added tests for the hint direction and the 9 vs 50 case.
- I did not fix the New Game, attempts counter, or scoring bugs.


## 📸 Demo Walkthrough

1. Started a game on Normal difficulty. The debug panel showed a secret of 97.
2. Entered 3. The game said "Go HIGHER!" and the score went down to -5.
3. Entered 100. The game said "Go LOWER!" and the score went down to -10.
4. Entered 100 again (an even attempt). The game still said "Go LOWER!", so the hint stayed correct, but the score went up by 5 to -5. This is a scoring bug I did not fix.
5. Entered 80. The game said "Go HIGHER!" and the score went back down to -10.
6. Entered 97. The game showed "Correct!" and the round ended with a win Final score: 20
7. The attempts counter was one higher than the number of guesses I made, because it starts at 1. I did not fix this one either.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
========================= test session starts =========================
platform darwin -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: /Users/cam/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.10.0
collected 5 items

tests/test_game_logic.py .....                                   [100%]

========================== 5 passed in 0.01s ==========================
```

## 🚀 Stretch Features

None completed.
