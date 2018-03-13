# [Shad0w Synd1cate Cybersecurity and IT Group of Las Vegas](https://www.meetup.com/Cyber-Security-and-IT-Computer-Group-of-Las-Vegas/events/246569084/)  
This is a basic static website that can be deployed to an S3 bucket on AWS and used for experiments, prototyping, user feedback, and so on.  
This site includes links to the group email and social media accounts, as well as a link to the group's [discussion forum](http://shad0wsynd1cate.com/index.php) on [vBulletin](https://www.vbulletin.com/).  
The Bootstrap template comes with its own README to fill you in on the details.  

## To run the prototype static site in your browser:  
1. [Clone this repository](https://help.github.com/articles/cloning-a-repository/)
2. Open your terminal (command prompt).
3. Navigate to the directory:  
`Shad0wSynd1cate/static-site/`  
(The one that contains the *index.html* file.)  
4. On the command line type:  
`>>> open -a "YourBrowserName" index.html`  
Options for "YourBrowserHere" include "FirefoxDeveloperEdition" or
"Google Chrome", for example.  

Your browser should open the website in a new tab.

### Security Note:  
The Shad0w Synd1cate site uses jQuery, which can have cross-site vulnerability issues like attaching unsanitized user input to the DOM.  
This is not currently a concern, but it may become one if this site is updated to accept user input.  
[More info here](https://github.com/jquery/jquery/issues/3949)  
