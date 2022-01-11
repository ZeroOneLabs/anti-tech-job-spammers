import os
import plistlib

# This script will confirm the list of emails you've added to your Mail rule

username = os.getenv("USER")
mail_plist = f"/Users/{username}/Library/Mail/V9/MailData/SyncedRules.plist"


with open(mail_plist, "rb") as f:
    mail_data = plistlib.load(f, fmt=None, dict_type=dict)

for rule in mail_data:
    if rule["RuleName"] == "Recruiter spam":
        
        for item in rule["Criteria"]:
            print(item["Expression"])
