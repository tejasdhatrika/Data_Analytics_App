pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat 'call venv\\Scripts\\activate'
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    bat 'call venv\\Scripts\\activate'
                    bat 'pytest'  // Ensure pytest is in your requirements.txt
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
    
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            junit '**/target/test-*.xml'
        }
    }
}
