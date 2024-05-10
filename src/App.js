import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import MessageGround from './components/MessageGround';
import { useEffect, useState } from 'react';
import TypingIndigator from './components/TypingIndigator';


function App() {

  const [message, setMessage] = useState([])
  const [indigate, setIndigate] = useState(false);

  const handleMessage = (newMessage) => {
    setMessage(newMessage);
  }

  
  const jarebResponse = async (userQuery) => {
    const url = "http://192.168.1.133:5555/chat?u=" + userQuery;
    const response = await fetch(url);
    if (response.ok)
    {
      const response_data = await response.json();
      setIndigate(false);
      setMessage(prevMessage => [...prevMessage, {content: response_data['res'], id: Date.now(), type: "your message"}])
    } else {
      setMessage(prevMessage => [...prevMessage, {content: "Error", id: Date.now(), type: "bot"}])
    }
  }


  useEffect(() => {
    if (message != "")
    {
      var lastMessage = message[message.length - 1];
      if (lastMessage.type === "user")
      {
        
        setTimeout(() => {
          setIndigate(true);
          jarebResponse(lastMessage['content']);
        }, 1800);
      }
    }
  }, [message])

  return (
    <div className="App">
      <Header/>
      <MessageGround setMessageContent={message}/>
      <TypingIndigator Indigator={indigate}/>
      <Footer setMessage={handleMessage}/>
    </div>
  );
}

export default App;
