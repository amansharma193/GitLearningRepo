pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                build job:'test2'
            }
            post{
                success {
                    echo '${env.Name}'
                }
                failure {
                    echo 'failure'
                }
            }x
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