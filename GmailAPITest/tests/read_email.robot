*** Settings ***
Library    BuiltIn
Library    Collections
Library    ../libraries/GmailKeywords.py

*** Test Cases ***
Read Email Content Test
    ${emails}=         List Emails    5
    ${first_email}=    Get From List    ${emails}    0
    ${email_id}=       Get From Dictionary    ${first_email}    id
    ${content}=        Get Email Content    ${email_id}
    Log                Email content: ${content}
