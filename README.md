# Flask-Continuous-Delivery
This is an implementation of Continuous Delivery of Flask Application on Google Cloud Platform.

## Instructions
It is recommended to run this project on a new python virtual environment.

Set up a new python virtual enviroment in GCP:
```
virtualenv --python $(which python3) ~/.venv
source ~/.venv/bin/activate
```

Create app engine app:
```
gcloud app create
```

Clone repository:
```
git clone https://github.com/tzring/Credit-Card-Approval.git
```

Install dependencies:
```
make install
```

Linting:
```
make lint
```

Test:
```
make test
```

Deploy:
```
gcloud app deploy
```

## Routes
- **/**: Hello world page
- **/name/\<value>**: return the name you entered
- **/cd**: A page used to test continuous delivery
