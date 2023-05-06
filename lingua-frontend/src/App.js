import React, { useState } from 'react';
import './App.css';
import InputForm from './InputForm';
import Conversation from './Conversation';
import Feedback from './Feedback';

function App() {
  const [messages, setMessages] = useState([]);
  const [feedback, setFeedback] = useState('');

  const handleNewMessage = (newMessage) => {
    setMessages((prevMessages) => [...prevMessages, newMessage]);
  };

  return (
    <div className="App">
      <h1>Lingua Language Learning Assistant</h1>
      <InputForm onNewMessage={handleNewMessage} onNewFeedback={setFeedback} />
      <Conversation messages={messages} />
      <Feedback feedback={feedback} />
    </div>
  );
}


export default App;

