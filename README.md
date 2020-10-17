# Pink Smile

Web application that supports breast cancer patients by sharing positive data, stories and media.

## Motivation

Breast cancer is the most common cancer in women worldwide.

Keeping a positive attitude has been proven to improve recovery expectations.

The mission of Pink Smile is to support breast cancer patients by sharing multimedia content, survivor testimonials, breast cancer organizations and providing reliable information about breast cancer with PinkBot.

Besides the main objetive, here are other ideas Pink Smile intends to show:

Statistics section:
- It's very common to develop breast cancer, _you_ - patient - are not alone!
- The mortality rate of cancer breast is one of the lowest in comparison to the others.
- The incidence is higher in North America and Europe, but the mortality rate is higher in Africa and South America -- it has to change.

Organizations section:
- A lot of people is willing to help
- African American and Latin American communities _need_ to have their own organizations -- why?

## How this application was developed

### Technologies:
- Python
- Flask
- HTML
- CSS

### Databases: 
I requested access to
- John Snow Labs 
- International Agency for Research on Cancer

## How to use this application

Create a new virtual environment to avoid issues with existing installations.

Create a project folder and a virtual environment folder within:
```
$ mkdir pink-smile

$ cd pink-smile

$ py -3 -m venv venv
```

Activate the environment:
```
$ venv\Scripts\activate
```
Your shell prompt will change to show the name of the activated environment.

Within the activated environment, use the following command to install all the necessary packages:
```
(venv) $ python -m pip install -r requirements.txt
```
 
Run Flask:
```
$ python app.py
```

The web application is running on http://127.0.0.1:5000/ !

## Challenges and setbacks
- It was hard to find a nice database and get access
- It's just the second app I develop with Flask so I spent a lot of time looking at documentation
- I have contacts that were happy to share their stories but couldn't schedule a meeting
- I spent a lot of time developing PinkBot and didn't finished it on time

## Future
I'm positive that the web app will be in production at the end of October. My priorities now are:
- Talk with breast cancer survivors and share their stories
- Finish PinkBot

I will fork this repository and continue developing the app at https://github.com/mariagrandury/pink-smile-prod, don't hesitate to have a look!
