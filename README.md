# tcSubmit

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

