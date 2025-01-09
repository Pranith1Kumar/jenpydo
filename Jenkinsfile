pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'calculator-app1'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Pranith1Kumar/jenpydo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").run('-d -p 5000:5000')
                }
            }
        }
    }
}
