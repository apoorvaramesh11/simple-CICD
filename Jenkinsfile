pipeline {
    agent any
    
    environment {
        IMG_NAME = "apoorvar12/simple-cicd"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/apoorvaramesh11/simple-cicd.git'
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t ${IMG_NAME} . "
            }
        }
        stage('login to dockerhub') {
            steps {
              withCredentials([usernamePassword(
                  credentialsId: 'dockerhubcred', 
                  passwordVariable: 'DOCKER_PASS', 
                  usernameVariable: 'DOCKER_USER'
                )]) {
                sh '''
                echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                '''
                }  
            }
        }
        stage('Push to dockerhub') {
            steps {
                sh "docker push ${IMG_NAME} "
            }
        }
        stage('container creation') {
            steps {
                sh "docker run -d -p 5000:5000 ${IMG_NAME}"
            }
        }
    }
}

