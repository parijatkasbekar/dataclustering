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
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                    // sh 'pytest test_app.py --junitxml=report.xml'
                }
            }
        }   

        stage('Run the unit tests ') {
            steps {
                script {
                    // Runnig the unit tests
                    sh "cd dataclustering && pytest "
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // sh "python3 -m unittest discover --pattern=test_app.py"
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


        stage('Run selenium tests') {
            steps {
                script {
                    // Execute selenium based testing
                    sh "cd dataclustering && python3 check_site_liveness.py"
                }
            }
        }


        stage('Send notification Email') {
            steps {
                script {
                    // Send notification Email via gmail
                    
                    sh 'python3 send_email.py'
                }
            }
        }
    }
}



