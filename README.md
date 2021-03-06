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

### B. Creating a new App
In the tab "Pipeline", click "Create New App" in the option "Production Apps"

### C. Enabling automatic deployment from GitHub to Heroku
Read here how to switch on the automatic deployment from GitHub to Heroku:
https://devcenter.heroku.com/articles/github-integration#automatic-deploys
Just go to the "Deploy" tab in your Heroku app and switch on "Automatic Deploys".

### D. Preparing deployable application
When deploying an app to Heroku, it needs to be set up in a way that allows Heroku to create a [slug](https://devcenter.heroku.com/articles/buildpacks) (an executable application copy) from your application. For this, it needs to contain a [Procfile](https://devcenter.heroku.com/articles/procfile) that tells Heroku which commands are executed by the app on startup, such as the "web worker".
If you don't want to dig into the various dependencies that need to be set up for a runable app, you can also use pre-fabricated basic apps from the ["Getting Started"](https://devcenter.heroku.com/start) section. Heroku provides these basic apps for various languages, such as Python, Java, Clojure, Ruby, Node.js... Here we go for the Python version:
https://devcenter.heroku.com/articles/python-support
As our Heroku App is already set up to build automatically from each push to the GitHub repository, we download the zip of the ["Python getting started package"](https://github.com/heroku/python-getting-started.git) (described [here](https://devcenter.heroku.com/articles/getting-started-with-python#prepare-the-app)) and extract its content directly into the folder synched with GitHub.

Now is a good time to save progress so far in GitHub, so that there's a branch with a basic Python App version to start over from, if necessary:
(as described in [this Stackoverflow thread about how to create remote branches](https://stackoverflow.com/questions/1519006/how-do-you-create-a-remote-git-branch))
```
git checkout -b python-base
git push origin python-base:python-base
```

### E. Checking out the app on the web
When the app is pushed to the connected GitHub repo (which is also conencted to Heroku) with
```
git push
```
then, via the [Heroku Dashboard](https://dashboard.heroku.com/), the app can be clicked and opened via "Open App" on the right-hand side.

### F. Running the app locally
Often it makes sense to be able to test an app locally (i.e. when working on development branches locally).
In order to be able to do so, the Heroku CLI needs to be installed (by following the [Getting Started instructions](https://devcenter.heroku.com/articles/getting-started-with-python) until the Heroku CLI is installed).
Then, in the same local folder where the app files are located, the command
```
heroku local web -f Procfile.windows
```
(on Windows, for other systems just use ```heroku local web```)
sets up the local version of the app: it creates the local Procfile.windows, static files, and runs the app on a local webserver. The app can now be opened via
http://localhost:5000/

### G.


