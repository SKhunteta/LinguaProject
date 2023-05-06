import React, { useState, useRef } from 'react';
import axios from 'axios';

function InputForm({ onNewMessage, onNewFeedback }) {
  const [inputText, setInputText] = useState('');
  const [isSending, setIsSending] = useState(false);
  const inputRef = useRef(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (isSending) {
      return;
    }

    setIsSending(true);

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/send-message', {
        message: inputText,
      });

      setInputText('');

      const newMessages = response.data.conversation;
      const newFeedback = response.data.feedback;

      // Ensure newMessages has the correct structure
      if (
        Array.isArray(newMessages) &&
        newMessages.every(
          (message) => typeof message === 'object' && 'sender' in message && 'content' in message
        )
      ) {
        onNewMessage(newMessages);
        onNewFeedback(newFeedback);
      } else {
        console.error('Invalid conversation data received from the server:', newMessages);
      }
    } catch (error) {
      console.error('Error while sending message:', error);
    } finally {
      setIsSending(false);
      inputRef.current.focus();
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="input-form-container">
          <input
            type="text"
            value={inputText}
            onChange={handleInputChange}
            placeholder="Type your message..."
            ref={inputRef}
            disabled={isSending}
          />
          <button type="submit" disabled={isSending}>
            {isSending ? 'Sending...' : 'Send'}
          </button>
        </div>
      </form>
    </div>
  );
}

export default InputForm;

