pipeline {
    agent any
    environment {
        // Define environment variables here
        DOCKER_IMAGE = 'parijatkasbekar/capstonedataclustering'
        DOCKER_TAG = 'latest'
    }
    stages {
        stage('Checkout') {
            steps {
                // Check out from version control
                git 'https://github.com/parijatkasbekar/dataclustering.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                // Setup a virtual environment and install dependencies
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                // Run pytest and generate a JUnit report
                sh 'pytest test_app.py --junitxml=report.xml'
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
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'sudo docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
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
        stage('Deploy') {
            steps {
                // Add steps to deploy your application
                echo 'Deploying Application...'
                // For example, pushing the Docker image to a registry could be a deployment step
                sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
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
