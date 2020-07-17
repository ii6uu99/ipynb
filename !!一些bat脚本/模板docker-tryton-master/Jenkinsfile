node {
    
    def customImage
        
    stage ('Checkout'){
        checkout scm
    }/*
    stage ('Build'){
        
        sh 'echo Deploying Env'
        sh 'docker run --name tryton-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=tryton -d postgres'
        sh 'docker run --link tryton-postgres:postgres -e DB_PASSWORD=mysecretpassword tryton/tryton trytond-admin -d tryton --all'
        sh 'docker run --name tryton -p 8000:8000 --link tryton-postgres:postgres -e DB_PASSWORD=mysecretpassword -d tryton/tryton'
    }*/
    stage ('Deploy') {
        
        sh 'echo Deploying Env'
        sh 'docker-compose up -d --build'
    }
    /*
    stage ('Configure') {
        sh 'docker run --link tryton-postgres:postgres -e DB_PASSWORD=password tryton/tryton trytond-admin -d tryton --all'
    }*/
}
