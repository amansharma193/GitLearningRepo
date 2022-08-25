pipeline {
    agent any
    stages {
        stage('test') {
            steps{
                build job: 'test2'
            }
        }
        stage('deploy') {
            steps {
                sh 'mvn -version'
            }
        }
    }
}