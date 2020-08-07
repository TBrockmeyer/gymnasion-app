# gymnasion-app
A simple app to test out the CI/CD functionality of heroku

This repo is being created to explore how Heroku and GitHub can be leveraged to have a sleek tryout process for testing simple web apps.
Heroku is a [cloud Paas](https://en.wikipedia.org/wiki/Heroku) that allows to quickly deploy apps for openign and testing via the web.
Github is a [software development platform](https://en.wikipedia.org/wiki/GitHub) allowing source code management.
Together, these two allow to maintain the code of an application living on an SCM system and deploying continuously and in an automated manner.

### A. Creation of a Heroku Pipeline with GitHub
Follow these instructions to create a CI/CD pipeline in Heroku that is connected with a GitHub repository:
https://devcenter.heroku.com/articles/github-integration

(If you want to run tests through Heroku CI, follow these instructions to enable it ($10/month and enabled pipeline):
https://devcenter.heroku.com/articles/heroku-ci)

### B. Create new App
In the tab "Pipeline", click "Create New App" in the option "Production Apps"

### C. Enable automatic deployment from GitHub to Heroku
Read here how to switch on the automatic deployment from GitHub to Heroku:
https://devcenter.heroku.com/articles/github-integration#automatic-deploys
Just go to the "Deploy" tab in your Heroku app and switch on "Automatic Deploys".

### D.

