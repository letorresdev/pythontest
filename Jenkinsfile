pipeline {
  agent any

  environment {
    RUST_VERSION = '1.56.0'
  }
  
  stages {
    stage('Install Rust') {
      steps {
        sh "python3 --version"
        sh "pip3 list"
        sh "ls"
      }
    }
    
    stage('Build') {
      steps {
        sh ''
        sh './build_zip.sh'
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
