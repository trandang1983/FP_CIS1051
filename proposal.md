# Proposal

## What will (likely) be the title of your project?

Antibody work-up for human blood  using a Python program.

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A website/app that reads cvs files contaning immunomhematology results from  antomated instruments to provide information about what types of antibodies a patient may have and to recommend what antigen negative blood should be transfused to the patient. The work-up is still being done by human.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

#General rules:
Immunomhematology results from panels are read line by line.
Each colum contains the presence of an antigen. 
If the serum reaction to that antigen is negative, it means that the antibody corresponding to that antigen is ruled out.
By runing a panel or a set of panel, it is usually possible to detect what antibodies are ruled out.
After ruling out, the remaning antibodies needs to be ruled in.
An antibody is ruled in when its P-value is met: 3 positive and 3 negative reactions corresponding to that antibody.
#There are exceptions that need to be included into the program and/or handled by human.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

NONE

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

NONE

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

I understand

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

The sofware is able to read files and recommend safe bood transfurions for patients

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

The software is continously updated to the point that it could be proposed to be validated in a hospital setting.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The software is used in a hospital setting.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I would need to register for the product and get it validated using data from hospitals. Validation is the topic that I need to research. I will need to discuss with the QA official in my hospital where I work to find out what the requirements are and what steps to follow.
