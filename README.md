# Kids Science Agent

An interactive and fun program designed to teach science concepts to children through interesting facts, tricky riddles, and a short science quiz game.

## How to Run

1.  Ensure you have Python (version 3 or higher) installed on your system.
2.  Download or copy the `kids_science_agent.py` file.
3.  Open your terminal or command prompt and navigate to the directory where `kids_science_agent.py` is located.
4.  Run the program using the following command:

    ```bash
    python kids_science_agent.py
    ```

## How to Use

Once the program is running, a menu will be displayed in the terminal:

Welcome to the Science Fun Zone!
Type (f) for a fun science fact.
Type (r) for a tricky riddle.
Type (q) for a science quiz game (5 questions).
Type (x) to exit.
Your choice:


* **`(f)`:** Enter `f` and press Enter to get an interesting science fact.
* **`(r)`:** Enter `r` and press Enter to be asked a riddle. You can then type your answer. The program will tell you if you're correct and show the right answer.
* **`(q)`:** Enter `q` and press Enter to start a short science quiz game with 5 questions. At the end, your score will be displayed.
* **`(x)`:** Enter `x` and press Enter to close the program.
* **Any invalid input:** If your input doesn't match any of the options above, an error message will be shown, and the menu will reappear.

## Code Structure

The `kids_science_agent.py` file includes the following sections:

* **Lists:**
    * `science_facts`: A collection of interesting science facts.
    * `science_riddles`: A list of science-related riddles.
    * `riddle_answers`: The corresponding answers to the `science_riddles`.
    * `science_questions`: A list of science questions.
    * `question_answers`: The corresponding answers to the `science_questions`.
* **Functions:**
    * `tell_fact()`: Selects and prints a random science fact.
    * `ask_riddle()`: Asks a random riddle and checks the user's answer.
    * `ask_single_question()`: Asks a single science question and checks the user's answer.
    * `play_question_game()`: Runs a 5-question science quiz game.
    * `show_menu()`: Displays the main menu and gets the user's input.
    * `main()`: Controls the main program loop and calls the appropriate functions based on user input.

## Contributing

If you have ideas to improve the program, add more facts, riddles, or questions, we would love to see your contributions! You can do this by creating a Pull Request on GitHub.

## License

[Specify your project's license here, e.g., MIT License.]

---

**Saving the File and Uploading:**

1.  **Save the content:** Copy the English text above and save it in a file named **`README.md`**. Make sure the filename is exactly `README.md` (case-sensitive). The `.md` extension indicates it's a Markdown file, which GitHub will automatically render in a user-friendly way.

2.  **Location:** Save this `README.md` file in the **root directory** of your `kids_science_agent` project on your local machine, right next to your `kids_science_agent.py` file.

3.  **Upload to GitHub:** When you upload your `kids_science_agent.py` file to your GitHub repository, also upload the `README.md` file to the same root directory of the repository.

Once you have both files in the root of your GitHub repository, GitHub will automatically recognize and display the contents of `README.md` on the main page of your repository. This will make it easy for anyone visiting your project to understand what it is and how to use it.
