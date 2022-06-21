pipeline {
    agent any

    stages {
        stage('Chekout') {
            steps {
                git branch: 'main', url: 'https://github.com/Cryptonauts00/Beta/'
                echo 'Checkout Completed'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
