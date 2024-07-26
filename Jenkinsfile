pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/tejasdhatrika/Data_Analytics_App'
            }
        }
        
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
                    // Your Docker build steps here
                }
            }
        }
        
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Your Minikube deployment steps here
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
