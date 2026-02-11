Some ideas for your own tasks                                                                                                                
===

(which literally copy `example-task` and tweak a few lines)

1. **Introduce a Syntax Error**\
Edit main.go to have a typo (fmt.Prntln, missing closing brace, wrong import path). Change nothing else. The agent now has to fix the code before compiling. One-line change to the source, zero changes to tests.       
                                                                                                                                                                                                                           
2. **Change the Language** \
Swap main.go for a main.c or main.py, update the Dockerfile to install gcc or python3 instead of golang-go, update instruction.md and tests to expect the new binary/output. Same structure, different flavor.

3. **Multi-File Build**\
Split the program into two files: main.go imports a function from utils.go, but utils.go has a missing return statement. Agent must fix it and compile. Add one file, tweak one test.

4. **Change the Output**\
Keep everything but change "Hello, World!" to something else in main.go (e.g. "LLMday Warsaw 2026!"), and update the expected string in test_outputs.py. Literally two lines changed. The twist: also remove the
solution/ directory so there's no cheat sheet.

5. **Add a Command-Line Argument**\
Modify main.go so it expects os.Args[1] and prints "Hello, <name>!". Update instruction.md to explain this. Update tests to run /app/hello World and check for "Hello, World!". Three files touched, a few lines each.

