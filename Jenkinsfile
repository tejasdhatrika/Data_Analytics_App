pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                // Run Pytest tests here
                bat 'pytest'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    bat 'docker build -t my-python-app:latest .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy application using kubectl
                    bat 'kubectl apply -f k8s\\deployment.yaml'
                }
            }
        }
    }
}
