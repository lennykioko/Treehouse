import React from 'react';
import PropTypes from 'prop-types';

import Counter from './Counter';

const Player = ({
  updatePlayerScore, index, score, selectPlayer, removePlayer, name,
}) => (
  <div className="player">
    <div className="player-name" onClick={() => selectPlayer(index)}>
      <a className="remove-player" onClick={() => removePlayer(index)}>
        ✖
      </a>
      {name}
    </div>
    <div className="player-score">
      <Counter index={index} updatePlayerScore={updatePlayerScore} score={score} />
    </div>
  </div>
);

Player.propTypes = {
  name: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  score: PropTypes.number.isRequired,
  removePlayer: PropTypes.func.isRequired,
  updatePlayerScore: PropTypes.func.isRequired,
  selectPlayer: PropTypes.func.isRequired,
};

export default Player;
