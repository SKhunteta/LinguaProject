import React from 'react';
import './App.css';

function Conversation({ messages }) {
  return (
    <div className="conversation-container">
      {messages.map((message, index) => (
        <div key={index} className={message.sender === 'user' ? 'text-right' : 'text-left'}>
          <div className={`message ${message.sender}-message`}>
            {message.content}
          </div>
        </div>
      ))}
    </div>
  );
}

export default Conversation;