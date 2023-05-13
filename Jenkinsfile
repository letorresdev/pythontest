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
  
//   post {
//     always {
//       junit 'target/debug/deps/*.xml'
//       archiveArtifacts 'target/debug/*.wasm'
//     }
    
    success {
      mail to: 'letorres.dev@gmail.com',
           subject: 'Build successful',
           body: 'Good job team!'
    }
    
    failure {
      mail to: 'letorres.dev@gmail.com',
           subject: 'Build failed',
           body: 'Please investigate the issue and fix it ASAP.'
    }
  }
}
