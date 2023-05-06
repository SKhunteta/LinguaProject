import React, { useState } from 'react';
import axios from 'axios';

function InputForm({ onNewMessage, onNewFeedback }) {
  const [inputText, setInputText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (inputText.trim()) {
      onNewMessage({ sender: 'user', content: inputText });
  
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/send-message', {
          message: inputText,
        });
  
        setInputText('');
        onNewFeedback(response.data.feedback);
        onNewMessage({ sender: 'ai', content: response.data.ai_response });
      } catch (error) {
        console.error('Error while sending message:', error);
      }
    }
  };  

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default InputForm;

