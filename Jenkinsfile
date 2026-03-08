pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/VigneshHubs/student-result-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Python313\\python.exe" test_app.py'
            }
        }

    }
}
