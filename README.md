# Tezos-BruteForce-Tester
Selenium Python Script to Automate/Bruteforce - Test and Validate Potential Passwords/Emails to assist in finding a valid TZ1 address.

Note this is for recovering coins during the initial crowdfund, where you should have received and saved a PDF file.

Requirements
- Selenium Webdriver
- Firefox
- Python3
I used archlinux so can't help with windows users.

No Rights Reserved.

Purpose: I built these tools to brute force a wallet. We were unsure of both the password and the email. So we had to try create a list
of possible passwords and email combinations and then test several hundred. This is an arduous process without a script.  Hopefully, this is useful to someone.

Tools
pwcheck.py

Uses Tezos password check script in either online or offline mode to generate possible TZ1 addresses/hashes. Takes input from a list of possible passwords. Could easily be adapted to cycle through emails as well.  Outputs TZ1 address to std out.

checktezos.py

Tests a file with a list of tz1 addresses from a text file against the tezos check site. If a postive result you will see a balance in Tezos appear in standard out.
Should be possbile to test 45000+ addresses/day.

