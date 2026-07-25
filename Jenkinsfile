pipeline {
    agent any

    environment {
        // 引用 Jenkins 凭据
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
                bat 'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest tests/ --junitxml=reports/junit.xml --alluredir=reports/allure-results'
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