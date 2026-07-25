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
                        echo ========== 网路诊断 ==========
                        curl -I https://mirrors.aliyun.com/pypi/simple/ 2>&1
                        curl -I https://pypi.tuna.tsinghua.edu.cn/simple/ 2>&1
                        curl -I https://pypi.org/simple/ 2>&1
                        echo ========== Python版本 ==========
                        python --version
                        where python
                        echo ========== 创建虚拟环境 ==========
                        python -m venv venv
                        echo ========== 开始安装依赖 ==========
                        venv\\Scripts\\pip install -v --trusted-host mirrors.aliyun.com -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
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