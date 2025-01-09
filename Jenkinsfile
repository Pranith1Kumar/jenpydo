pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'calculator-app1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Run the Docker container
                    docker.image("${DOCKER_IMAGE}").run('-d -p 5000:5000')
                }
            }
        }
    }
}
