# TaskStudy CI Demo

Core logic of a Student Task & Study Management System with unit tests and a
Continuous Integration pipeline (GitHub Actions, plus an equivalent Jenkinsfile).

Run locally:

    pip install -r requirements.txt
    flake8 app tests
    pytest --cov=app

Jenkins on Linux or in Docker uses `Jenkinsfile`.
Jenkins installed directly on Windows uses `Jenkinsfile.windows`
(set "Script Path" to Jenkinsfile.windows in the Jenkins job).
