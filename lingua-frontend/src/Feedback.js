import React from "react";
import "./App.css";

function Feedback({ feedback }) {
  return feedback ? (
    <div className="feedback-container">
      <p className="feedback-text">{feedback}</p>
    </div>
  ) : null;
}

export default Feedback;
