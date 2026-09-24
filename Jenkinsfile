pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Generate Report') {
            steps {
    
                bat """
                    echo Build Number: %BUILD_NUMBER%
                    echo Job Name: %JOB_NAME%
                    echo Workspace Path: %WORKSPACE%
                """
               
                bat 'python app.py'
            }
        }

        stage('Archive Report') {
            steps {
                
                archiveArtifacts artifacts: 'build_report.txt', fingerprint: true
            }
        }
    }
}
