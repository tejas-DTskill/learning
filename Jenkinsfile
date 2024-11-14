pipeline {
    agent none // No global agent, we will specify it in the stages

    environment {
        DOCKER_IMAGE = "learning" // Name of the Docker image
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
                    sh """
                    container_id=\$(docker ps -q --filter "learning")
                    if [ -n "\$container_id" ]; then
                        docker stop \$container_id
                        docker rm \$container_id
                    fi
                    // Run the new container from the newly created Docker image
                    docker run -d -p 8000:8000 --name learning-${VERSION} ${DOCKER_IMAGE}:${VERSION}
                    """
                }
            }
        }
    }
}
