pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Pranith1Kumar/jenpydo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t calculator-app1 .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name calculator-container1 calculator-app1'
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    sh 'curl http://localhost:5000/add?a=10&b=5'
                }
            }
        }
    }
}
