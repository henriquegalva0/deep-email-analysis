# Project
I'm currently working on a cibersec project and I must develop a pipeline to analyze the content of emails.

# Team
My team is working on developing another tools to verify the emails' authors and attachments.

# Model
With google-bert/bert-base-uncased I was able to feed the model an email dataset so as it can identify phishing techniques on emails.

# Other tools
There is a tool to detect strange characters such as invisible or homographs.
There is another tool to detect common phishing words.

# Missing data
I can't display the data on the git for security means, so use your own data creating a folder named 'data' and deploy a .csv named 'emails'.

# Usage
Download the requirements.txt file with
  pip install -r requirements.txt
Run email.py with
  python email_classifier.py
Test the model inputing an email in the variable "email_teste" on testing_classifier.py and run with
  python testing_classifier.py
