pipeline {
    agent any

    environment {
        // Define environment variables for your project
        DOCKER_IMAGE_NAME = 'parijatkasbekar/capstonedataclustering'
        REPO_URL = 'https://github.com/parijatkasbekar/dataclustering.git'
        DIRECTORY_NAME = 'dataclustering'
    }

    stages {
 
         stage('Clone the repo') {
            steps {
                script {
                    // Build a Docker image and tag it
                    sh "rm -rf dataclustering && git clone ${REPO_URL}"
                }
            }
        }       

        stage('Build Docker Image') {
            steps {
                script {
                    // Build a Docker image and tag it
                    sh "cd dataclustering && docker build . -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh "docker --config ~/.docker login && docker push ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Deploy to Kubernetes using kubeconfig from Jenkins user's home directory
                    sh "sed -i 's/BUILD_NUMBER_PLACEHOLDER/${BUILD_NUMBER}/g' dataclustering/deployment/capstone.yaml"
                    sh 'kubectl apply -f dataclustering/deployment/capstone.yaml'
                }
            }
        }
    }
}
post {
changed {
script {
if (currentBuild.currentResult == 'FAILURE') {
emailext subject: '$DEFAULT_SUBJECT',
body: '$DEFAULT_CONTENT',
recipientProviders: [
[$class: 'CulpritsRecipientProvider'],
[$class: 'DevelopersRecipientProvider'],
[$class: 'RequesterRecipientProvider']
],
replyTo: '$DEFAULT_REPLYTO',
to: '$DEFAULT_RECIPIENTS'
}
}
}
}
}
