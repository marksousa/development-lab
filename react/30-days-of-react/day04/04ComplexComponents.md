# Complex Components

Build an entire application in a single component is not a great idea as it can grow huge, complex, and difficult to test.
It's well-suited break down into multiple components. The first container we have to build is a container component. This container is going to be a "wrapper" (empacotador, embalagem) for the other two components.

## The Wrapper Component

```
class App extends React.Component {
    render() {
        return(
            <div className="notificationsFrame">
                <div className="panel">
                    { /* Content */}
                </div>
            </div>
        )
    }
}
```

It's necessary use `className` because `class` is a reserved word in JavaScript
We not modify directly the DOM directly (JSX)

## The Child Components

The Header
```
class Header extends React.Component {
  render() {
    return (
      <div className="header">
        <div className="fa fa-more"></div>
        <span className="title">Timeline</span>
        <input type="text" className="searchInput" placeholder="Search..." />
        <div className="fa fa-search searchIcon"></div>
      </div>
    );
  }
}

```
The Content
```
class Contentt extends React.Component {
  render() {
    return (
      <div className="content">
        <div className="line"></div>

        {/* Timeline Item*/}
        <div className="item">
          <div className="avatar">
            <img src="https://www.personality-database.com/profile_images/34568.png"></img>
            Doug
          </div>
          <span className="time">An hour ago</span>
          <p>Ate lunch</p>
          <div className="commentCount">2</div>
        </div>

        {/* ... */}
      </div>
    );
  }
}
```

## All Together Now 🚊

```
class App extends React.Component {
    render() {
        return(
            <div className="notificationsFrame">
                <div className="panel">
                    <Header />
                    <Content />
                </div>
            </div>
        )
    }
}
```



