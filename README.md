# Use-Selenium-Webdriver-to-scrap-Kickstarter
Selenium Webdrivers can automate browsers. Primarily it is for automating web applications for testing purposes. This repository contains code that can automate webpage to scroll down so that you can scrap all information. 
## How to use
<ol>
<li> <b> Download Selenium Webdriver:</b> After download, need to update the file path (should be different from mine);
<li> <b> Change website:</b> I am using Kickstarter.com. You can use it with any other website, just change the URL; 
<li> <b> Automation:</b> The demo code shows how to change website Language to be English and currency to be USD. You can use this .click() function for other purposes;
<li> <b> Scroll down pages: </b>It is initially set to be 100. Can be changed while updating the number in range();
<li> <b> Parse informtion:</b> Use beautiful soup or other packages to get targeted information.
</ol>

## What's in the Demo 
It automates to open the browser, go to Kickstarter.com, set language to be English and currency to be USD, scroll down to the botton 100 times, use beautiful soup to get following information: Project Title, Funded Percentage, Funded Amount, Project Goal, Project Category, Sub Category, Project City, Project State.
