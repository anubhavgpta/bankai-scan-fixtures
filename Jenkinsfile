pipeline {
  agent any

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test') {
      steps {
        bat 'python -m pip install pytest'
        bat 'python -m pytest'
      }
    }
  }
}