*** Settings ***
Library    BuiltIn
Library    Collections
Library    ../libraries/GmailKeywords.py

*** Test Cases ***
Delete Email Test
    ${emails}=    List Emails    5
    ${first_email}=    Get From List    ${emails}    0
    ${email_id}=       Get From Dictionary    ${first_email}    id
    Delete Email    ${email_id}
    Log    Email deleted successfully
