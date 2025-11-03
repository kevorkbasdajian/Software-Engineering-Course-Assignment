pipeline {
    agent any

    triggers {
        // Poll GitHub every 2 minutes
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo "=== Checking out code from GitHub ==="
                git branch: 'master', url: 'https://github.com/kevorkbasdajian/Software-Engineering-Course-Assignment'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                @echo off
                echo === Switching Docker to Minikube Docker environment ===
                for /f "tokens=*" %%i in ('minikube docker-env --shell cmd') do call %%i

                echo === Building Django Docker image inside Minikube ===
                docker build -t mydjangoapp:latest .

                echo === Confirming image built successfully ===
                docker images mydjangoapp:latest
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                @echo off
                echo === Applying updated Kubernetes deployment ===
                kubectl apply -f deployment.yaml

                echo === Restarting deployment to refresh Pods with new image ===
                kubectl rollout restart deployment/django-deployment

                echo === Waiting for rollout to complete ===
                kubectl rollout status deployment/django-deployment

                echo === Checking running Pods ===
                kubectl get pods
                '''
            }
        }

        stage('Access Info') {
            steps {
                bat '''
                @echo off
                echo === Fetching application access URL ===
                minikube service django-service --url
                '''
            }
        }
    }
}
