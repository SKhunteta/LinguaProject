import React from 'react';

function Conversation({ messages = [] }) {
  return (
    <div>
      <h2>Conversation</h2>
      <ul>
        {messages.map((message, index) => (
          <li key={index}>{message}</li>
        ))}
      </ul>
    </div>
  );
}

export default Conversation;
