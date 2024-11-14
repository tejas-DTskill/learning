pipeline {
    agent none // No global agent, we will specify it in the stages

    environment {
        DOCKER_IMAGE = "gene-agent-service" // Name of the Docker image
        VERSION = "v${BUILD_NUMBER}" // Version based on Jenkins build number
    }

    stages {
        stage('Pull Code') {
            agent { label 'demo' } // Ensure this stage runs on the demo node
            steps {
                // Pull the code from the GitHub repository
                git 'https://github.com/tejas-DTskill/learning.git'
            }
        }
        stage('Build Docker Image') {
            agent { label 'demo' } // Ensure this stage runs on the demo node
            steps {
                // Build the Docker image and tag it with a unique version
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${VERSION} ."
                }
            }
        }
        stage('Run Docker Container') {
            agent { label 'demo' } // Ensure this stage runs on the demo node
            steps {
                // Stop and remove any existing container with the same name
                script {
                    sh 'docker ps -q --filter "name=gene-agent-service" | xargs -r docker stop | xargs -r docker rm'
                    // Run the new container from the newly created Docker image
                    sh "docker run -d -p 8000:8000 --name gene-agent-service-${VERSION} ${DOCKER_IMAGE}:${VERSION}"
                }
            }
        }
    }
}
