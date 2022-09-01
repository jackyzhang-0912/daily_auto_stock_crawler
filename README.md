# Daily Auto Stock Crawler for MacOs
### Brief Intro
#### A crawler that runs automatically every day at 16:00 to gather targeted stocks' information and send them to specific email address.    
#### All automated, hands-free！
---
### Modules
#### [plist file](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html) (auto part) + [selenium](https://www.selenium.dev/) (crawler part) + [smtplib](https://docs.python.org/3/library/smtplib.html) (email part)
---
### Usage
- Install all the used python packages in crawler.py if needed
- Change the Label name (currently as "com.jacky.crawler.plist")
- Place the plist file and the crawler file under the /Library/LaunchAgents/ directory
- Change the python path in ProgramArguments if different from the one in plist file
- Change the StartCalendarInterval arguments to customize the preferred executed time
- Change the StandardOutPath for outputs

- When everything is ready, run `sudo launchctl bootstrap gui/501 ./com.jacky.crawler.plist`, replace the file name with new name
- Then run `sudo launchctl list | grep 'Your_file_name'` to check the job'status. If the code is 0, then it is running correctly. Otherwise, run `launchctl error The_error_code` to get more information about the error
- Run `sudo launchctl bootout gui/501 ./com.jacky.crawler.plist` to end the job
---
### Helpful Resources
#### https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html
#### https://alvinalexander.com/mac-os-x/launchd-plist-examples-startinterval-startcalendarinterval/
#### Debug tool: [launchcontrol](https://www.soma-zone.com/LaunchControl/) (`brew install launchcontrol`)
---
### Problems encountered during the development

#### Operation not permitted (error code 1) when using sh file to run python  
- ####  Run python file directly in plist file

#### When using Python to run, ImportError, no module named Selenium, occurs. 
- #### Put the exact python path instead of python3 in the ProgramArguments in plist (Use `which python3` to find the path)