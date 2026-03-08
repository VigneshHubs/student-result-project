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
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python test_app.py'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }

    }
}



