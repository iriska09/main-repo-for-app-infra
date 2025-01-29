// pipeline {
//     agent any

//     parameters {
//         string(name: 'APP_NAME', defaultValue: '', description: 'App Name')
//         choice(name: 'APP_TYPE', choices: ['python', 'js'], description: 'App Type')
//         string(name: 'BUSINESS_UNIT', defaultValue: 'flower', description: 'Business Unit')
//     }

//     environment {
//         GITHUB_TOKEN = credentials('github-token')
//         JENKINS_URL = credentials('jenkins-url')
//         JENKINS_USER = credentials('jenkins-user')
//         JENKINS_PASSWORD = credentials('jenkins-password')
//     }

//     stages {
//         stage('Create Virtual Environment and Install Dependencies') {
//             steps {
//                 sh """
//                 python3 -m venv .venv
//                 . .venv/bin/activate
//                 pip install requests python-dotenv python-jenkins
//                 """
//             }
//         }

//         stage('Create Repositories') {
//             steps {
//                 script {
//                     def app_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app"
//                     def infra_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra"
//                     sh """
//                     . .venv/bin/activate
//                     python3 repo-create.py "${app_repo_name}" "${infra_repo_name}"
//                     """
//                 }
//             }
//         }

//         stage('Create Pipelines') {
//             steps {
//                 script {
//                     def app_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app"
//                     def infra_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra"
//                     sh """
//                     . .venv/bin/activate
//                     python3 pipeline-create.py "${app_repo_name}" "new-jenkinspipeline-app" "${params.APP_NAME}" "app" "${env.JENKINS_URL}" "${env.JENKINS_USER}" "${env.JENKINS_PASSWORD}" "${env.GITHUB_TOKEN}"
//                     python3 pipeline-create.py "${infra_repo_name}" "new-jenkinspipeline-infra" "${params.APP_NAME}" "infra" "${env.JENKINS_URL}" "${env.JENKINS_USER}" "${env.JENKINS_PASSWORD}" "${env.GITHUB_TOKEN}"
//                     """
//                 }
//             }
//         }

//         stage('Complete Pipeline') {
//             steps {
//                 echo 'Pipeline setup complete!'
//             }
//         }
//     }
// }
pipeline {
    agent any

    parameters {
        string(name: 'APP_NAME', defaultValue: '', description: 'App Name')
        choice(name: 'APP_TYPE', choices: ['python', 'js'], description: 'App Type')
        string(name: 'BUSINESS_UNIT', defaultValue: 'flower', description: 'Business Unit')
    }

    environment {
        GITHUB_TOKEN = credentials('github-token')
        JENKINS_URL = credentials('jenkins-url')
        JENKINS_USER = credentials('jenkins-user')
        JENKINS_PASSWORD = credentials('jenkins-password')
    }

    stages {
        stage('Create Virtual Environment and Install Dependencies') {
            steps {
                sh """
                python3 -m venv .venv
                . .venv/bin/activate
                pip install requests python-dotenv python-jenkins
                """
            }
        }

        stage('Create Repositories') {
            steps {
                script {
                    sh """
                    . .venv/bin/activate
                    python3 repo-create.py "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app" "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra"
                    """
                }
            }
        }

        stage('Create Pipelines and Webhooks') {
            steps {
                script {
                    sh """
                    . .venv/bin/activate
                    python3 pipeline-create.py "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app" "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app-pipeline"
                    python3 pipeline-create.py "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra" "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra-pipeline"
                    """
                }
            }
        }

        stage('Complete Pipeline') {
            steps {
                echo 'Pipeline setup complete!'
            }
        }
    }
}
