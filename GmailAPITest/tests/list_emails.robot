*** Settings ***
Library    ../libraries/GmailKeywords.py

*** Test Cases ***
List Emails Test
    ${emails}=    List Emails    5
    Log    Retrieved Emails: ${emails}
    Should Not Be Empty    ${emails}    No emails found