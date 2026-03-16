pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python test_app.py'
            }
        }

    }
}