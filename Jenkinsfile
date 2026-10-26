pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh '. venv/bin/activate && flake8 app tests'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest --cov=app --cov-report=xml --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }

    post {
        success { echo 'CI build passed.' }
        failure { echo 'CI build failed. Check the console output.' }
    }
}
