pipeline {
  agent any

  properties([
    [$class: 'jenkins.model.BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '96']],
    pipelineTriggers([[$class:"SCMTrigger", scmpoll_spec:"M/2 * * * *"]]),
    ])

  environment {
    RUST_VERSION = '1.56.0'
  }
  
  stages {
    stage('Python3') {
      steps {
        sh "python3 --version"
        sh "pip3 list"
        sh "ls"
      }
    }
    
    stage('Test') {
      steps {
        sh './test.sh'
      }

    }

    stage('Build') {
      steps {
        sh ''
        sh './build_zip.sh'
        archiveArtifacts(artifacts: '**/*.zip', followSymlinks: false)
      }

    }
    
    // stage('Test') {
    //   steps {
    //     sh 'cargo test'
    //   }
    // }
    
    // stage('Run') {
    //   steps {
    //     sh 'cargo run'
    //   }
    // }
  }
  

}
