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

export default Content; // Don’t forget to use export default!
