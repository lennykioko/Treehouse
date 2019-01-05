import React from 'react';
import PropTypes from 'prop-types';

import Stats from './Stats';
import Stopwatch from './Stopwatch';

const Header = ({ players }) => (
  <div className="header">
    <Stats players={players} />
    <h1>Scoreboard</h1>
    <Stopwatch />
  </div>
);

Header.propTypes = {
  players: PropTypes.arrayOf(PropTypes.string).isRequired,

};

export default Header;
