# LENTA SCRAPER
#### Video Demo:  https://youtu.be/kLzvX8Bi4cg
#### Description: Hi I am Narek and this project for CS50. Project is designed to web scrapping the site lenta.com. lenta.com is a large online store where there are often discounts.In order not to miss the discounts, I made a web scrapper that will constantly monitor the store and when there are goods with discounts more than you define, you will receive a telegram message with a description of the product and a link to it.

#### In order for the scraper to work, you need
#### 1. Telegram bot-token(enter in the program window)
#### 2. Your user-id(enter in the program window)
#### 3. Enter in the program window
#### 4. Decide what type of products you are interested in
#### 5. Wait for a message (for verification, you can set the value to 50)

#### Initially, I made the program go through all the pages of the product, but for quick work, I cut off the first 10 pages. but so that the logic of the program would not change.

#### I wrote the program in vscode and put the main file in the project folder and also added requirements.txt


#### I saw examples of similar projects. I hope it will work as a final project, although to be honest it was written by me a little earlier than I started the final project.

#### First we import the request, bs4, time, threading and tkinter libraries.
#### 1. With the help of requests and bs4 we will get the data and read it.
#### 2. time will help with timeouts.
#### 3. threading will allow us to work in multiple threads.
#### 4. tkinter will help us make a window for the application

#### the send_msg function get our settings from aplication window and we know who is whant to get our messages

#### each of start1, start2, start3 functions is attached to different buttons in the application window and will search different places for discounted products

#### st1, st2, st3 help us to thread functions

#### the zash function makes it possible to make the program not work if I do not want it.the site saponjyan.ru is my site, so it includes and removes pages, I distribute it calmly and without prejudice. I think this is a very convenient option to maintain control over the program and, if necessary, be able to disable it.

#### The smag variable is the id of stores on the network, because lenta is not only an online store, but you can also look at the addresses of what is in which branches.

#### in cookies with the requests library, we add the id of the store and the site gives us data in the store with a specific id. Some items are not available in all stores.

#### if reason != "ok" , then the program will fall asleep for 10000 seconds so that the user does not understand what is happening.

#### You can disable this feature if needed.*

#### In my opinion, I described the project in as much detail as possible.

#### How to do it all in detail, I will show in the video on youtube

#### So it was Narek Saponjian for CS50