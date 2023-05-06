import React from 'react';

function Conversation({ messages }) {
  return (
    <div>
      <h2>Conversation</h2>
      <ul>
        {messages && messages.map((message, index) => (
          <li key={index} style={{ textAlign: message.sender === 'user' ? 'right' : 'left' }}>
            {message.content}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Conversation;
