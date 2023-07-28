# tcSubmit

Reads any files found in the folder format `<yyyy>/<month_number>-<month>/<day_number>.md`. Automatically parses the file found for the current day and submits the information to a time log application in ServiceNow.

The parsed information starts with a shorthand name that corresponds to a project in ServiceNow so the hours are submitted against the correct project. An example entry might look like this:

File: `2023/1-January/3.md`

```text
TCA 5
STRY001234 - worked on rest integration for knowledge
STRY001345 - added ui action to interface

TCB 3
status meeting
Test call with David
Sprint planning session
```

In the above example, two time cards are submitted for two different projects, TCA (test company A) and TCB (test company B). TCA and TCB would be configured in the config file like so:

```json
{
    "base_path": "/Users/bob/Documents/Obsidian",
    "instance_name": "internalservicenowstable",
    "shortcuts": {
        "TCA": "78hhc9714g5fd9507a354e42846d313a",
        "TCB": "6j4218de875dd330b26e426acebb13ce",
    }
}
```

### Installation

Add to .zshrc (replace folder with yours):

`alias submit="python3 /Users/blake/Documents/Programs/tcSubmit/main.py"`


### Auto Run

Set permissions and ownership:
`sudo chown root:wheel tcsubmit.plist`

`sudo chmod 644 tcsubmit.plist`

Add plist to /Library/LaunchDaemons

`sudo cp tcsubmit.plist /Library/LaunchDaemons`

**MAKE SURE THE LOGIN ITEM HAS FULL DISK ACCESS USING THE SECURITY SETTINGS PAGE**

Start the service

`sudo launchctl bootstrap system/com.blake.tcsubmit`

`sudo launchctl enable system/com.blake.tcsubmit`

Check that it's loaded correctly (must use sudo since this is a system service)

`sudo launchctl list | grep com.blake`

