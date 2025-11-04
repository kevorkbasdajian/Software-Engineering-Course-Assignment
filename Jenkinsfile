pipeline {
    agent any

    triggers {
        // Poll GitHub every 2 minutes
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/kevorkbasdajian/Software-Engineering-Course-Assignment.git'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                REM === Switch Docker to Minikube Docker ===
                for /f "delims=" %%i in ('minikube docker-env --shell=cmd') do %%i

                REM === Check which Docker instance Jenkins is using ===
                echo === Checking Docker context ===
                docker info
                REM === Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                REM === Apply the updated deployment manifest ===
                kubectl apply -f deployment.yaml

                REM === Ensure the rollout completes ===
                kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}
