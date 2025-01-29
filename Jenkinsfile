// // pipeline {
// //     agent any

// //     parameters {
// //         string(name: 'REPO_NAME', defaultValue: '', description: 'Repository Name')
// //         string(name: 'PIPELINE_NAME', defaultValue: '', description: 'Pipeline Name')
// //         string(name: 'APP_NAME', defaultValue: '', description: 'App Name')
// //         choice(name: 'APP_TYPE', choices: ['python', 'js'], description: 'App Type')
// //         string(name: 'BUSINESS_UNIT', defaultValue: 'flower', description: 'Business Unit')
// //     }

// //     environment {
// //         GITHUB_TOKEN = credentials('github-token')  // Ensure you have a GitHub token stored in Jenkins credentials
// //         JENKINS_URL = credentials('jenkins-url')     // Set these in Jenkins credentials
// //         JENKINS_USER = credentials('jenkins-user')   // Set these in Jenkins credentials
// //         JENKINS_PASSWORD = credentials('jenkins-password') // Set these in Jenkins credentials
// //     }

// //     stages {
// //         stage('Create Repositories') {
// //             steps {
// //                 script {
// //                     // Ensure the repo_create.py script is available in the workspace
// //                     sh """
// //                     python3 -m venv .venv
// //                     . .venv/bin/activate
// //                     pip install requests python-dotenv python-jenkins
// //                     python3 repo-create.py "${params.REPO_NAME}-app" "${params.REPO_NAME}-infra"
// //                     """
// //                 }
// //             }
// //         }

// //         stage('Create Pipelines') {
// //             steps {
// //                 script {
// //                     // Ensure the pipeline_create.py script is available in the workspace
// //                     sh """
// //                     python3 pipeline-create.py "${params.REPO_NAME}-app" "new-jenkinspipeline-app" "${params.REPO_NAME}" "app" "${JENKINS_URL}" "${JENKINS_USER}" "${JENKINS_PASSWORD}" "${GITHUB_TOKEN}"
// //                     python3 pipeline-create.py "${params.REPO_NAME}-infra" "new-jenkinspipeline-infra" "${params.REPO_NAME}" "infra" "${JENKINS_URL}" "${JENKINS_USER}" "${JENKINS_PASSWORD}" "${GITHUB_TOKEN}"
// //                     """
// //                 }
// //             }
// //         }

// //         stage('Complete Pipeline') {
// //             steps {
// //                 echo 'Pipeline setup complete!'
// //             }
// //         }
// //     }
// // }







// ////////
// pipeline {
//     agent any

//     parameters {
//         string(name: 'REPO_NAME', defaultValue: '', description: 'Repository Name ( my-project)')
//         string(name: 'PIPELINE_NAME', defaultValue: '', description: 'Pipeline Name (my-project-pipeline)')
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
//                     sh """
//                     . .venv/bin/activate
//                     python3 repo-create.py "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app" "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra"
//                     """
//                 }
//             }
//         }

//         stage('Create Pipelines') {
//             steps {
//                 script {
//                     sh """
//                     . .venv/bin/activate
//                     python3 pipeline-create.py "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app" "new-jenkinspipeline-app" "${params.REPO_NAME}" "app" "${env.JENKINS_URL}" "${env.JENKINS_USER}" "${env.JENKINS_PASSWORD}" "${env.GITHUB_TOKEN}"
//                     python3 pipeline-create.py "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra" "new-jenkinspipeline-infra" "${params.REPO_NAME}" "infra" "${env.JENKINS_URL}" "${env.JENKINS_USER}" "${env.JENKINS_PASSWORD}" "${env.GITHUB_TOKEN}"
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

////

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
                    def app_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app"
                    def infra_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra"
                    sh """
                    . .venv/bin/activate
                    python3 repo-create.py "${app_repo_name}" "${infra_repo_name}"
                    """
                }
            }
        }

        stage('Create Pipelines') {
            steps {
                script {
                    def app_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-app"
                    def infra_repo_name = "${params.BUSINESS_UNIT}-${params.APP_NAME}-${params.APP_TYPE}-infra"
                    sh """
                    . .venv/bin/activate
                    python3 pipeline-create.py "${app_repo_name}" "new-jenkinspipeline-app" "${params.APP_NAME}" "app" "${env.JENKINS_URL}" "${env.JENKINS_USER}" "${env.JENKINS_PASSWORD}" "${env.GITHUB_TOKEN}"
                    python3 pipeline-create.py "${infra_repo_name}" "new-jenkinspipeline-infra" "${params.APP_NAME}" "infra" "${env.JENKINS_URL}" "${env.JENKINS_USER}" "${env.JENKINS_PASSWORD}" "${env.GITHUB_TOKEN}"
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
