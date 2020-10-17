# Pink Smile

Website that supports breast cancer patients by sharing positive data, stories and media.

## Motivation

Breast cancer is the most common cancer in women worldwide and is increasing, particularly in developing countries where the majority of cases are diagnosed in late stages.

Keeping a positive attitude has been proven to improve recovery expectations.

The mission of Pink Smile is to support breast cancer patients by sharing multimedia content, survivor testimonials, breast cancer organizations and answering questions related to breast cancer with PinkBot.

## How this application was developed

Technologies:
- Python
- Flask
- HTML
- CSS

Database: I requested access to
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
