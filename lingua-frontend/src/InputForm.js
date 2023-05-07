import React, { useState } from 'react';
import axios from 'axios';

function InputForm({ onNewMessage, onNewFeedback }) {
  const [inputText, setInputText] = useState('');
  const [isSendingMessage, setIsSendingMessage] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (isSendingMessage) {
      return;
    }

    setIsSendingMessage(true);

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/send-message', {
        message: inputText,
      });

      setInputText('');

      const newMessages = response.data.conversation;

      // Ensure newMessages has the correct structure
      if (
        Array.isArray(newMessages) &&
        newMessages.every(
          (message) => typeof message === 'object' && 'sender' in message && 'content' in message
        )
      ) {
        onNewMessage(newMessages);
      } else {
        console.error('Invalid conversation data received from the server:', newMessages);
      }
    } catch (error) {
      console.error('Error while sending message:', error);
    }

    setIsSendingMessage(false);
  };

  const handleFeedback = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/request-feedback', {
        language_code: 'en',
      });

      const newFeedback = response.data.feedback;

      onNewFeedback(newFeedback);
    } catch (error) {
      console.error('Error while requesting feedback:', error);
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
        <button type="submit" disabled={isSendingMessage}>
          {isSendingMessage ? 'Sending...' : 'Send'}
        </button>
      </form>
      <button className="feedback-button" onClick={handleFeedback}>Request Feedback</button>
    </div>
  );
}

export default InputForm;
