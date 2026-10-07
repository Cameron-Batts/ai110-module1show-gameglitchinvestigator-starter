# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked fine, but the hints did not match my guesses. I guessed a number higher than the secret and the game told me to go higher. I also noticed that the New Game button did not really restart the game after I won, and the attempts left number started one too low. After I looked at the code, I found that these problems came from a few specific places in app.py.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60, secret 50 | "Too High" and a hint to go LOWER | Outcome says "Too High" but the message says "Go HIGHER!" | none; check_guess, return messages |
| Guess 9, secret 50 on an even attempt (2nd, 4th, etc.) | "Too Low" | Sometimes "Too High", because the secret was turned into a string and "9" > "50" as text | none; app.py submit block (secret = str(...)) and the except TypeError branch in check_guess |
| Click New Game after winning | A fresh game I can play | Still shows "You already won" and the game stays stuck | none; app.py, the if new_game block (status, score, history never reset) |
| Start the app on Normal | 8 attempts left | Shows 7 attempts left | none; app.py, attempts starts at 1 |

---

## 2. How did you use AI as a teammate?

I used Claude to help me read the code, find the bugs, and write tests. One correct suggestion was to remove the code that turned the secret into a string on even attempts and to always compare two integers. This was correct because the string comparison was the reason the hints were random on every other guess. I checked it by running pytest, where a test with guess 9 and secret 50 now returns "Too Low", and by playing the game with the debug info open.

One suggestion I did not accept as written was [describe yours, for example: the AI wanted to rewrite the whole scoring system and the attempts logic at the same time]. I did not use it because it was out of scope for the hint bugs and it made the change much bigger and harder to review. I only kept the small fix to check_guess and the comparison, and I checked it by running pytest again and replaying the game.

---


## 3. Debugging and testing your fixes

I decided a bug was fixed when the same input that failed before gave the right result, both in a test and in the live game. I ran pytest with tests like guess 60 vs secret 50 returning "Too High" with a LOWER message, and guess 9 vs secret 50 returning "Too Low". These showed me that the logic worked on its own, apart from Streamlit. The AI helped me by suggesting the test cases, especially the 9 vs 50 case that catches the string comparison bug, and I made sure I understood why each test was there.

---

## 4. What did you learn about Streamlit and state?

Streamlit runs the whole Python file from top to bottom every time you click a button or type something. Because of that, normal variables get reset on every run. Session state is like a small notebook that Streamlit keeps between runs, so things like the secret number, the score, and the attempts can be remembered. If you forget to reset something in session state, like the status after a win, the app can get stuck.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing a small test right after each fix, so I know the bug is really gone. Next time I would start committing earlier and more often, so my git history shows each step instead of one big change. This project showed me that AI generated code can look clean and still be wrong in small ways, so I need to read it and test it before I trust it.
