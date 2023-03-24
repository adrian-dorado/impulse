<!-- This will be .gitlab-ci.yml file: -->


stages:
  - test   # Run tests first
  - build  # Run build after tests

services:
  - postgres:14.2-bullseye

variables:
  POSTGRES_PASSWORD: test
  DATABASE_URL: postgresql://postgres:test@postgres:5432/postgres

subscriptions-unit-test-job:
  image: python:3-bullseye
  stage: test
  script:
    - cd ./subscriptions/api/subscriptions_rest
    - pip install -r requirements.txt
    - python manage.py test

products-unit-test-job:
  image: python:3-bullseye
  stage: test
  script:
    - cd ./products/products_rest
    - pip install -r requirements.txt
    - python manage.py test

lint-job:
  image: python:3-bullseye
  stage: test
  script:
    - pip install flake8
    - flake8 products subscriptions

build-front-end-job:
  stage: build
  image: node:lts-bullseye
  script:
    - cd ghi
    - npm install
    - npm run build


<!-- first page of CD instructions has example sections also for:

build-back-end-job
deploy-back-end-job-heroku
heroku-release
pages (to deploy with GitLab Pages)

I don't understand commit tags -->
