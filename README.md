# Study Plan Project

This project was inspired by my need to keep track of all the things that I wish to learn. 

This code makes it so that the user can develop a study plan for themselves using the Google Calendar API. 

## How It Works

When the program is ran, the user is asked whether they would like to add entries into their calendar using the Fibonacci Study Plan or delete entries they have already made. That leaves the question, what is the Fibonacci Study Plan?

## The Fibonacci Sequence

Before discussing the Fibonacci Study Plan we should first discuss the Fibonacci sequence. The sequence begins with either a 0 or a 1; however, the second element is always a 1. The consecutive elements in the Fibonacci sequence can be found by adding the previous two elements. For this program, the code utilizes a definiton of the Fibonacci sequence where the first number is 1 and not 0. As a consequence of this the first few numbers in the sequence are 1, 1, 2, 3, 5, etc.  

## The Fibonacci Study Plan

It is quite certain that whenever we wish to retain some information, it is not possible to simply read it over once and remember it forever. Thus, it would be a useful if we were able to set reminders for ourselves as to review content later in the future as well. A problem which immediately arises involves the question as to how we will space out our review periods. The Fibonacci Study Plan solves this problem by utilizing the Fibonacci sequence where the numbers would represent how many days in the future to review. For example, the first element of the Fibonacci sequence is 1, that would mean that an entry should be placed in the user's Google Calendar for one day in the future. The second element in the Fibonacci sequence is also 1, this would mean that the user's Google Calendar should set an entry into their Google Calendar for 1 day in the future after the last entry. 

## Prerequisites

In order to utilize this code, a file named "credentials.json" needs to be included in the workspace directory. This file can be retreived by visiting console.google.developers.com. After logging into the site, it is necessary to create a project and enable the Google Calendar API. After doing this, one can download their credentials by visiting the "credential section" and downloading the file under the category "OAuth 2.0 Client IDs". Any users of this code should ensure that they rewrite any environment variables to fit their own needs. 