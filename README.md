# Pink Smile

Website that supports people with breast cancer sharing positive data, stories and media.

## Motivation

Every 15 seconds, somewhere in the world, a woman is diagnosed with breast cancer. Breast cancer is the most common cancer in women worldwide and is increasing, particularly in developing countries where the majority of cases are diagnosed in late stages.

## Run the app

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

Within the activated environment, use the following command to install all the necessary packages with install -r:
```
(venv) $ python -m pip install -r requirements.txt
```
 
To run Flask:
```
$ python app.py
```