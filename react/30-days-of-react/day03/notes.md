# Babel

Babel is a library for transpiling ES6 to ES5.

    <script type="text/babel">

This signals to Babel that we would like it to handle the execution of the JavaScript inside this script body.

# The React app

The first argument to ReactDOM.render() is what to render and the second is where:

`ReactDOM.render(<what>, <where>)`

    <script type="text/babel">
      var app = <h1>Hello World!</h1>;
      var mountComponent = document.querySelector("#app");
      ReactDOM.render(app, mountComponent);
    </script>

# React Components

Write React Components as ES6 classes;

Ex:

    class App extends React.Component {
        render() {
            return <h1>Hello from our app component</h1>;
        }
    }

Another way using React.creatClass() function:

    var App = React.createClass({
        render: function() {
            return <h1>Hello from our app</h1>
        }
    });
    
    //  always need to use ReactDom.render(what, where)
    var mount = document.querySelector('#app');
    ReactDOM.render(<App />, mount);


All React components require at least a render() function. This render() function is expected to return a virtual DOM representation of the browser DOM element(s).

    Notice that we can render our React app using the App class as though it is a built-in DOM component type (like the <h1 /> and <div /> tags). Here we're using it as though it's an element with the angle brackets: <App /> .


