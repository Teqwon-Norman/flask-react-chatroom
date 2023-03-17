import '../pages/static/Home.css';

function Home() {
    return (
        <form className="homepage">
            <h1 className="homepage_title">Enter The Chat Room</h1>
            <div className="name">
                <h4>Name:</h4>
                <input placeholder="Pick a name!"></input>
            </div>
            <div className="join_room">
                <input placeholder="Room Code"></input>
                <button>Join a Room</button>
            </div>
            <div className="create_button">
                <button>Create a Room</button>
            </div>
        </form>
    );
}

export default Home;