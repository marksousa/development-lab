# Data-Driven Components

## Props

React allows us to send data to a component in the same syntax as HTML, using attributes or properties on a component.

We can access these properties inside a component as this.props .

on wrapper app

    <Header title="Linha do Tempo" />
    <Header title="Perfil" />
    <Header title="Configurações" />
    <Header title="Chat" />


on component son

    <div className="fa fa-more"></div>
    <span className="title">{this.props.title}</span>

We can pass besides strings, numbers, all sorts of objects and even functions

With this in mind, we can modify our content component to receive an activity object like:

    {
        timestamp: new Date().getTime(),
        text: "Ate lunch",
        user: {
            id: 1,
            name: 'Nate',
            avatar: "http://www.croop.cl/UI/twitter/images/doug.jpg"
            },
        comments: [
            { from: 'Ari', text: 'Me too!' }
        ]
    }


the content class can be modify to:

    class Content extends React.Component {
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