pipeline {
    agent any
    options {
        timeout(time: 30, unit: 'MINUTES')  // 总超时
    }
    environment {
        // 若有凭据再启用
        // API_KEY = credentials('NONE')
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
                        venv\\Scripts\\python -m pip install --upgrade pip
                        venv\\Scripts\\pip install --no-cache-dir --timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat 'venv\\Scripts\\pytest tests/ --junitxml=reports/junit.xml --alluredir=reports/allure-results'
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