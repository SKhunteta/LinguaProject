import React from 'react';
import './App.css';

function Feedback({ feedback }) {
  return feedback ? (
    <p className="feedback">{feedback}</p>
  ) : null;
}

export default Feedback;