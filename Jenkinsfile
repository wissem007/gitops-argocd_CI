pipeline{
    agent any


    environment{
        DOCKERHUB_USERNAME= "wissem007"
        APP_NAME = "gitops-argocd_ci"
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGES_NAME = "${DOCKERHUB_USERNAME}" + "/" + "${APP_NAME}"
        REGISTRY_CREDS ='dockerHub'
    }
        
    
    stages{
        stage("clenup workspace"){
            steps{
                script {
                    // sh "rm -rf *"
                    cleanWs()

                }
               
            }
             
        }
        stage("checkout  SCM"){
                    steps{
                        script {
                            git credentialsId: 'github',
                            url: 'https://github.com/wissem007/gitops-argocd_CI.git',
                            branch: 'master'

                        }
                    
                    }
                    
                }
          stage("Docker build Image"){
                    steps{
                        script {
                            // docker_image = docker.build "${IMAGES_NAME}"
                            docker_image =  docker.build "${IMAGES_NAME}"
                            // (IMAGES_NAME, '-f ${DOCKERFILE_PATH} .')
         

                         }
                    
                    }
            }

             stage("Docker push Image"){
                    steps{
                        script {
                        docker.withRegistry('', REGISTRY_CREDS) {
                        // Poussez l'image Docker vers votre registre
                         app = docker_image.push("${BUILD_NUMBER}")
                        }
                        }
                    }
            }

           stage("Docker delete  Image"){
                    steps{
                        script {
                            sh "docker rmi ${IMAGES_NAME}:${IMAGE_TAG}"
                            sh "docker rmi ${IMAGES_NAME}:latest"
         

                         }
                    
                    }
            } 
            stage('Trigger ManifestUpdate') {
                steps{
                    script {
                        // test 
                echo "triggering updatemanifestjob"
                build job: 'gitops-argocd_CD', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
            }
            }
            }
}
}