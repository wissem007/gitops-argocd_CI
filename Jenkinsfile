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
                        docker_image.push("${BUILD_NUMBER}")
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

            stage("Update kubernates deploy file"){
                    steps{
                        script {
                            sh '''cat deployment.yml
sed -i "s#${APP_NAME}.*#${APP_NAME}:${IMAGE_TAG}#g" deployment.yml
cat deployment.yml
'''
                         }
                    
                    }
            }


            stage("Update GIT"){
                    steps{
                        script {
                            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {

                   
                        //withCredentials([string(credentialsId: 'github', variable: 'GIT_TOKEN')]) {
                        //def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
                        sh '''git config --global user.email "alouiwiss@gmail.com"
git config --global user.name "wissem007" 
git add deployment.yml
git commit -m \'Done by Jenkins Job changemanifest: ${env.BUILD_NUMBER}\'

'''
      withCredentials([gitUsernamePassword(credentialsId: 'jenkinstogithub', gitToolName: 'Default')]) {
       sh 'git push https://github.com/wissem007/gitops-argocd_CI.git HEAD:master'

                         }
                    
                    }
            }


            




    }
 
}
}
}