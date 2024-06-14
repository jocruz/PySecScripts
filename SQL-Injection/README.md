# SQL Injection Testing Tool

## Overview 🌟
This tool is designed to perform blind SQL injection attacks to extract sensitive information such as user passwords from a database. It systematically tests and confirms each character of a password, allowing for an in-depth security analysis of web applications.

## What is Blind SQL Injection? 🔍
Blind SQL (Structured Query Language) Injection is a type of SQL Injection attack that asks the database true or false questions and determines the answer based on the application's response. This attack is used when the web application does not display errors with information about the structure of the database.

### Example of Blind SQL Injection:
Assume a standard login page:
- A typical payload for testing might be entering `admin' AND 1=1 --` in the username field.
- This payload aims to check if the password for `admin` is correctly matched; however, in a blind SQL context, the attacker infers success if the normal user interface changes unexpectedly or if certain expected content (like an error message) does not appear.

## Relation to OWASP Top 10 🛡️
Blind SQL injections are prominently featured in the OWASP Top 10 as a part of injection flaws which are ranked highly due to their prevalence and the severe impact they can have. They exploit security vulnerabilities in an application's software and can lead to data theft, loss of data integrity, and unauthorized access.

## Why Blind SQL Injection Requires Disrupted Content Responses
The essence of a blind SQL injection is in the response handling:
- The tool depends on whether specific content ("needle") is missing from the response to confirm if the SQL query altered the server's behavior.
- This absence indicates that the SQL payload executed successfully, changing the output based on the logic of the injected SQL.

## Why Burp Suite is an Effective Tool for Testing SQL Injections 🛠️
- **Interception and Analysis**: Allows intercepting and analyzing requests and responses between the browser and the server.
- **Repeatability**: Facilitates repeated sending of altered requests to test different injections.
- **Automation**: Offers automated tools to scan and identify potential injection points effectively.

## Tool Capabilities
- **User Validation**: Checks if a user exists within the system.
- **Password Length Determination**: Discerns the length of a user's password.
- **Password Hash Extraction**: Iteratively extracts the hashed password character by character.
- **Query Counting**: Maintains a count of how many queries were executed, aiding in efficiency analysis.
