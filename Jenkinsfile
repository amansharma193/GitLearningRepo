pipeline {
    agent any
    stages {
        stage('params'){
            steps{
                echo "Name = ${env.NAME}"
            }
        }
        stage('build') {
            steps {
                build job:'test2', parameters: [string(name: 'Developer', value: "${env.NAME}")]
            }
            post{
                success {
                    echo 'success'
                }
                failure {
                    echo 'failure'
                }
            }
        }
        stage('test 2') {
            steps{
                build job: 'test 3', propagate: false
            }
            post{
                success {
                    echo 'success'
                }
                failure {
                    echo 'failure'
                }
            }
        }
        stage('post test 3'){
            steps{
                echo 'after test 3 =>'
            }
        }
        stage('test 4') {steps{
                build job: 'test 4'
            }
            post{
                success {
                    echo 'success'
                }
                failure {
                    echo 'failure'
                }
            }
        }
    }
}
