import { useState, useRef, useEffect } from 'react';
import '../styles/Footer.css';
import { IoSend } from "react-icons/io5";



function Footer({ setMessage })
{

  const inputRef = useRef(null);


  const [inputValue, setInputValue] = useState("");

  const sendMessage = () => {
    setMessage(prevMessage => [...prevMessage, { content: inputValue, id: Date.now(), type: "user"}]);
    inputRef.current.value = "";
    setInputValue("");
  }


  return (
    <div className="Footer">
      <div id='chat-componant'>
        <input id='message-box' ref={inputRef} placeholder='Message' onChange={(e) => setInputValue(e.target.value)}/>
        <button id='sendMessage' ><IoSend id='sendMessageIcon' fill='RoyalBlue' onClick={sendMessage}/></button>
      </div>
    </div>
  )
}

export default Footer;