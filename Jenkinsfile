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
                powershell 'Write-Host "hello from powershell"'
                powershell 'whoami'
                powershell 'Get-Command python -ErrorAction SilentlyContinue'
                powershell 'Get-ChildItem'
            }
        }
    }
}