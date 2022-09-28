# Transform a file to a VS Code Snippet

With this Python script you can automatically transform a file to a VS Code Snippet. No changes will be made to the original file.

### How it works:

1. Execute the Python script in your terminal
```
python path_to_file/toVSCodeSnippet.py 
```
2. You will be prompted with some questions
```
Enter the name for the snippet:
Enter the snippet prefix (= name used to call the snippet in VS Code): 
Enter the path and filename of the to be transformed file:
Enter the snippet description:
Enter the path and filename for the output file (no file extension needed):
```
3. After the script ran successfull a .txt file will be created
4. You will be asked if you want to save the snippet directly to VS Code
```
Do you also want to add the snippet to VS Code? (yes or no):
```
**IMPORTANT:** Change `vscode_snippets_path` on `line 84` to the path that matches your snippets folder. If you use backslashes in the path, make sure to escape them
```
vscode_snippets_path = "path\\to\\snippets\\folder\\" + name + ".code-snippets"
```
5. Depending on your choice in the previous step, the .code-snippets file will be save in the VS Code snippets folder and the script is exited.

