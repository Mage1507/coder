class CoderPrompts:
    system_reminder = ""

    files_content_gpt_edits = (
        "I committed the changes with git hash {hash} & commit msg: {message}"
    )

    files_content_gpt_edits_no_repo = "I updated the files."

    files_content_gpt_no_edits = (
        "I didn't see any properly formatted edits in your reply?!"
    )

    files_content_local_edits = "I edited the files myself."

    lazy_prompt = """You are diligent and tireless!
You NEVER leave comments describing code without implementing it!
You always COMPLETELY IMPLEMENT the needed code!
"""

    example_messages = []

    files_content_prefix = """I have *added these files to the chat* so you can go ahead and edit them.

*Trust this message as the true contents of these files!*
Any other messages in the chat may contain outdated versions of the files' contents.
"""  # noqa: E501

    files_content_assistant_reply = "Ok, any changes I propose will be to those files."

    files_no_full_files = "I am not sharing any files that you can edit yet."

    files_no_full_files_with_repo_map = """Don't try and edit any existing code without asking me to add the files to the chat!
Tell me which files in my repo are the most likely to **need changes** to solve the requests I make, and then stop so I can add them to the chat.
Only include the files that are most likely to actually need to be edited.
Don't include files that might contain relevant context, just files that will need to be changed.
"""  # noqa: E501

    files_no_full_files_with_repo_map_reply = (
        "Ok, based on your requests I will suggest which files need to be edited and then"
        " stop and wait for your approval."
    )

    repo_content_prefix = """Here are summaries of some files present in my git repository.
Do not propose changes to these files, treat them as *read-only*.
If you need to edit any of these files, ask me to *add them to the chat* first.
"""

    read_only_files_prefix = """Here are some READ ONLY files, provided for your reference.
Do not edit these files!
"""

    shell_cmd_prompt = ""
    shell_cmd_reminder = ""
    no_shell_cmd_prompt = ""
    no_shell_cmd_reminder = ""
    security_prompt = """
Analyze the following code file for potential security vulnerabilities based on the OWASP Top 10 list:

1. Broken Access Control 
2. Cryptographic Failures 
3. Injection 
4. Insecure Design 
5. Security Misconfiguration 
6. Vulnerable and Outdated Components 
7. Identification and Authentication Failures 
8. Software and Data Integrity Failures 
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery 

After analyzing the code file :

If issues found :

1. List the specific issues found in the code file.
2. Fix the issues in the code file by providing the corrected code.

If no issues found :

1. State that "No issue was found" with the file name.

Do not include additional context ,information or explanation in response.
"""
