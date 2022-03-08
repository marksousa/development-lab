class HelloWorld extends React.Component {
  render() {
    return <h1 className="large">Hello World</h1>;
  }
}

// The JSX is translated to regular JavaScript at
// runtime. That component, after translation, looks like this:
// class HelloWorld extends React.Component {
//   render() {
//     return React.createElement("h1", { className: "large" }, "Hello World");
//   }
// }

// JSX looks like HTML
// The HTML that React writes to the DOM will look like this:
// <h1 class="large">Hello World</h1>

// In ES6, the class syntax might be translated as:
// var HelloWorld = function() {}
// Object.extends(HelloWorld, React.Component)
// HelloWorld.prototype.render = function() {}

// You can write pure javascript and not use JSX compiler. But look this example:

// JSX
// <div>
//     <img src="profile.jpg" alt="Profile photo" />
//     <h1>Welcome back Ari</h1>
// </div>

// Javascript sent to browser
// React.createElement("div", null,
//     React.createElement("img", {src: "profile.jpg", alt: "Profile photo"}),
//     React.createElement("h1", null, "Welcome back Ari")
// );

// JSX syntaz is well-suited for representing nested HTML elements.
