pipeline {
    agent any
    stages {
        stage('parameters'){
            steps{
                echo "PARAM = ${env.DEVELOPER}"
            }
        }
        stage('build') {
            steps {
                bat 'mvn -version'
            }
        }
    }
}
