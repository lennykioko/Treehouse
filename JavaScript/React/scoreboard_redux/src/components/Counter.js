import React from 'react';
import PropTypes from 'prop-types';

const Counter = ({ updatePlayerScore, index, score }) => (
  <div className="counter">
    <button
      className="counter-action decrement"
      onClick={() => updatePlayerScore(index, -1)}
      type="button"
    >
      -
    </button>
    <div className="counter-score">
      {score}

    </div>
    <button
      className="counter-action increment"
      onClick={() => updatePlayerScore(index, 1)}
      type="submit"
    >
      +
    </button>
  </div>
);

Counter.propTypes = {
  updatePlayerScore: PropTypes.func.isRequired,
  index: PropTypes.number.isRequired,
  score: PropTypes.number.isRequired,
};

export default Counter;
