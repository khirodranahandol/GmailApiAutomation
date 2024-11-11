*** Settings ***
Library    ../libraries/GmailKeywords.py

*** Variables ***
${TO_EMAIL}     ranahandol.khirod13@gmail.com
${SUBJECT}      Test Email
${BODY}         This is a test email sent by Robot Framework.

*** Test Cases ***
Send Email Test
    Send Email    ${TO_EMAIL}    ${SUBJECT}    ${BODY}
    Log    Email sent successfully
