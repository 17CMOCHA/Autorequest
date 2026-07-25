pipeline {
    agent any
    options {
        timeout(time: 30, unit: 'MINUTES')
    }
    environment {
        API_KEY = credentials('NONE')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/17CMOCHA/Autorequest.git'
            }
        }
        stage('Test Basic') {
            steps {
                bat 'echo hello'
                bat 'whoami'
                bat 'where python'
                bat 'dir'
            }
        }
    }
    post {
        always {
            echo 'done'
        }
    }
}