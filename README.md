# Studio Scaffold for Mesop


Mesop scaffold for Studio style apps.

This is an example of a multi-page Mesop UX application, where:

* individual pages have their own state management while also having access to an application state
* Mesop custom components are used to facility app scaffolding, with side navigation and header


![](./assets/example.gif)


## Prerequisites

A python virtual environment, with required packages installed.

Using [uv](https://github.com/astral-sh/uv):

```
# create a virtual environment
uv venv venv
# activate the virtual environment
. venv/bin/activate
# install the requirements
uv pip install -r requirements.txt
```


## Mesop scaffold app

### Prerequisites

This app uses Gemini, so you'll also need to create a `.env` file with the following:

```
PROJECT_ID=YOUR_PROJECT_ID
LOCATION=us-central1
MODEL_ID=gemini-2.0-flash-exp
```

Your GCP Project ID can be obtained via `gcloud config get project`


### Start the app


Start the app to explore

```
mesop main.py
```

# Disclaimer

This is not an official Google project