import React, { useState } from 'react';
import './App.css';
import InputForm from './InputForm';
import Conversation from './Conversation';
import Feedback from './Feedback';

function App() {
  const [messages, setMessages] = useState([]);
  const [feedback, setFeedback] = useState('');

  const handleNewMessage = (newMessages) => {
    setMessages((prevMessages) => [...prevMessages, ...newMessages]);
  };  

  return (
    <div className="chat-container">
      <h1 className="chatbot-title">Lingua Language Learning Assistant</h1>
      <Conversation messages={messages} />
      <InputForm onNewMessage={handleNewMessage} onNewFeedback={setFeedback} />
      <Feedback feedback={feedback} />
    </div>
  );
}

export default App;