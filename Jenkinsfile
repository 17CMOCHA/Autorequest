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
                    powershell '''
                        & C:\\ProgramData\\anaconda3\\python.exe -m venv --clear venv
                        & venv\\Scripts\\pip install --proxy http://127.0.0.1:7897 -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                powershell 'if (!(Test-Path reports)) { New-Item -ItemType Directory reports }'
                powershell '''
                    $env:PYTHONPATH = $PWD.Path
                    & venv\\Scripts\\pytest V1/tests/ --junitxml=reports/junit.xml --alluredir=reports/allure-results
                '''
            }
        }
    }
    post {
        always {
            junit 'reports/junit.xml'
            powershell '''
                & allure generate reports/allure-results -o reports/allure-report --clean
            '''
            archiveArtifacts artifacts: 'reports/allure-report/**', allowEmptyArchive: true
        }
    }
}