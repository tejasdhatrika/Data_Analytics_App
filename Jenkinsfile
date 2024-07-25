pipeline {
    agent any

    environment {
        // Add the path to the Python installation to the PATH variable
        PATH = "${env.PATH};C:\\Path\\To\\Python;C:\\Path\\To\\Python\\Scripts"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    bat '''
                    call venv\\Scripts\\activate
                    pytest
                    '''
                }
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
