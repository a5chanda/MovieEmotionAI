import React, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import ReactPlayer from "react-player";

class App extends React.Component{
  constructor(props){
    super(props);

// http.post(localhost:5000){
// url: "youtube link" 
//}

    this.state = {
      inputValue : "",
      url:""
    }
  }

  handleChange = (event) => {
    //console.log(event.target.value);
    console.log("uhashdas");
    this.setState({inputValue : event.target.value})
  }

  handleSubmit = (data) =>{
    data.preventDefault();
    this.setState({url: this.state.inputValue})
    console.log(data);
    fetch('/', {
      mode: "no-cors",
      method: 'POST',
      headers: 
      { 'cache-control': 'no-cache',
        Connection: 'keep-alive',
        "Access-Control-Allow-Origin":"http://localhost:5000",
        'Content-Length': '',
        'Accept-Encoding': 'gzip, deflate',
        Host: 'localhost:5000',
        'Cache-Control': 'no-cache',
        Accept: '*/*',
      },
      body: JSON.stringify({})
    }).then((resp)=>{
      return resp.json();
    }).then(function(info){
      console.log(info);
    })
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
          <h1 style ={{margin:"20px"}}>Welcome to MindScape</h1>
          <img src={logo} className="App-logo" alt="logo" />
          <div>
            <form onSubmit={this.handleSubmit}>
            <input onChange={this.handleChange} style ={{margin:"20px"}} className = "form-control" type="text" placeholder="Input the video url here!"/>    
            </form>
          </div>
  
          <ReactPlayer url={this.state.url} controls={true} />
        </header>
      </div>
    );
  }
  
}

export default App;
