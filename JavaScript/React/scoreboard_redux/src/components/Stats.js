import React from 'react';
import PropTypes from 'prop-types';

const Stats = ({ players }) => {
  const playerCount = players.length;
  const totalPoints = players.reduce((total, player) => total + player.score, 0);

  return (
    <table className="stats">
      <tbody>
        <tr>
          <td>Players:</td>
          <td>{playerCount}</td>
        </tr>
        <tr>
          <td>Total Points:</td>
          <td>{totalPoints}</td>
        </tr>
      </tbody>
    </table>
  );
};

Stats.propTypes = {
  players: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Stats;
