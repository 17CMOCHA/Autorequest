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
        stage('Install Dependencies') {
            steps {
                timeout(time: 15, unit: 'MINUTES') {
                    bat '''
                        python -m venv venv
                        venv\\Scripts\\pip install --trusted-host mirrors.aliyun.com -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat 'venv\\Scripts\\pytest V1/tests/ --junitxml=reports/junit.xml --alluredir=reports/allure-results'
            }
        }
    }
    post {
        always {
            junit 'reports/junit.xml'
            allure includeProperties: false, results: [[path: 'reports/allure-results']]
        }
    }
}