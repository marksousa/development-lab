# 03 - Building a Backend with MongoDB, Express and Node From Scratch

## Creating a MERN Skeleton Build

### 1. Create a package.json

Run

`yarn init`

### 2. Development Dependencies

Configure and install Babel, Webpack and Nodemon

#### 2.1 Babel

Install and configure Babel modules to convert ES6+ into older versions of JS so that it's compatible with the Node version being used.

Creates a .babelrc in root project's and paste:

    {
        "presets": [
        ["@babel/preset-env",
            {
            "targets": {
                "node": "current"
            }
            }
        ],
        "@babel/preset-react"
        ],
        "plugins": [
        "react-hot-loader/babel"
        ]
    }


First, we'll configure Babel in the .babelrc file with presets for the latest JS features and specify the current version of Node as the target environment.

Setting targets.node to current instructs Babel to compile against the current version of Node and allows us to use expressions such as async/await in our backend code.

Next, we need to install the Babel modules as devDependencies from the command line:

`yarn add --dev @babel/core babel-loader @babel/preset-env`

### 2.2 Webpack

`yarn add --dev webpack webpack-cli webpack-node-externals`

### 2.3 Nodemon

    {
        "verbose": false,
        "watch": ["./server"],
        "exec": "webpack --mode=development --config webpack.config.server.js && node ./dist/server.generated.js"
    }

### 3. Config Variables

**No arquivo config/config.js, definiremos algumas configurações de servidor relacionadas a variáveis ​​que serão usadas no código, mas não devem ser codificadas como uma prática recomendada, bem como para fins de segurança.**

    const config = {

        env: process.env.NODE_ENV || 'development',
        port: process.env.PORT || 3000,
        jwtSecret: process.env.JWT_SECRET || "YOUR_secret_key",
        mongoUri: process.env.MONGODB_URI ||
        process.env.MONGO_HOST ||
        'mongodb://' + (process.env.IP || 'localhost') + ':' +
        (process.env.MONGO_PORT || '27017') +
        '/mernproject'
    }

    export default config

The config variables that were defined are as follows: 
- env : To differentiate between development and production modes 
- port : To define the listening port for the server 
- jwtSecret : The secret key to be used to sign JWT 
- mongoUri : The location of the MongoDB database instance for the project

These variables will give us the flexibility to change values from a single file and use it across the backend code. Next, we will add the run scripts, which will allow us to run and debug the backend implementation.

### 4. Running scripts

add to package.json

    "scripts": {
        "development": "nodemon"
    }

### 5. Preparing the server

#### 5.1 Configuring Express

- create server/express.js

- install the express module `yarn add express`

- add to express.js
    {
        import express from "express";
        const app = express();
        /*... configure express ... */
        export default app;
    }

To handle HTTP requests and serve responses properly, we will use the following modules to configure Express:

- body-parser : Request body-parsing middleware to handle the
complexities of parsing streamable request objects so that we can simplify browser-server communication by exchanging JSON in the request body. To install the module, run `yarn add body-parser` from the command line. 

- cookie-parser : Cookie parsing middleware to parse and set cookies in request objects. To install the cookie-parser module, run `yarn add cookie-parser` from the command line.

- compression : Compression middleware that will attempt to compress response bodies for all requests that traverse through the middleware. To install the compression module, run `yarn add compression` from the command line.

- helmet : Collection of middleware functions to help secure Express apps by setting various HTTP headers. To install the helmet module, run `yarn add helmet` from the command line.

- cors : Middleware to enable cross-origin resource sharing (CORS). To install the cors module, run `yarn add cors` from the command line.

After the preceding modules have been installed, we can update express.js to import these modules and configure the Express app before exporting it for use in the rest of the server code.

    *express.js*
    import express from "express";
    import bodyParser from "body-parser";
    import cookieParser from "cookie-parser";
    import compress from "compression";
    import cors from "cors";
    import helmet from "helmet";

    const app = express();

    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({ extended: true }));
    app.use(cookieParser());
    app.use(compress());
    app.use(helmet());
    app.use(cors());

    export default app;

#### 5.2 Starting the server

With the Express app configured to accept HTTP requests, we can go ahead and use it to implement a server that can listen for incoming requests.

In the mern-skeleton/server/server.js file, add the following code to implement the server:

    import config from './../config/config'
    import app from './express'
    app.listen(config.port, (err) => {
        if (err) {
            console.log(err)
        }
        console.info('Server started on port %s.', config.port)
    })

#### 5.3 Setting up Mongoose and connecting to MongoDB

Mongoose is a MongoDB object modeling tool that provides a schema-based solution to model application data. It includes built-in type casting, validation, query building, and business logic hooks. Using Mongoose with this backend stack provides a higher layer over MongoDB with more functionality, including mapping object models to database documents. This makes it simpler and more productive to develop with a Node and MongoDB backend. To learn more about Mongoose, visit [mongoosejs](mongoosejs.com).

### 6. Serving an HTML template at a root URL
Create a template.js on root folder

mern-skeleton/template.js :

    export default () => {
        return `<!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>MERN Skeleton</title>
            </head>
            <body>
                <div id="root">Hello World</div>
            </body>
        </html>`
    }