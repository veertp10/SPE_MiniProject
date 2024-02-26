pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'calculator'
        GITHUB_REPO_URL = 'https://github.com/veertp10/SPE_MiniProject.git'
	OPTION = 1
	NUMBER = 2
	EXP = 3
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }

	
        stage('Run Main Application') {
            steps {
                script {
                    sh "echo '${OPTION}\n${NUMBER}\n${EXP}' | python3 calculator1.py"
                }
            }
        }


        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 test.py'
                }
            }
        }


        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCred') {
                    sh 'docker tag calculator veerendragoudatp10/calculator:latest'
                    sh 'docker push veerendragoudatp10/calculator'
                    }
                 }
            }
        }

   stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }

    }
}
