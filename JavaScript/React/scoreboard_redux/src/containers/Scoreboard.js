import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import * as PlayerActionCreators from '../actions/player';
import AddPlayerForm from '../components/AddPlayerForm';
import Player from '../components/Player';
import Header from '../components/Header';

const Scoreboard = ({ dispatch, players }) => {
  const addPlayer = bindActionCreators(
    PlayerActionCreators.addPlayer,
    dispatch
  );
  const removePlayer = bindActionCreators(
    PlayerActionCreators.removePlayer,
    dispatch
  );
  const updatePlayerScore = bindActionCreators(
    PlayerActionCreators.updatePlayerScore,
    dispatch
  );
  const selectPlayer = bindActionCreators(
    PlayerActionCreators.selectPlayer,
    dispatch
  );

  const playerComponents = players.map((player, index) => (
    <Player
      index={index}
      name={player.name}
      score={player.score}
      key={player.name}
      updatePlayerScore={updatePlayerScore}
      removePlayer={removePlayer}
      selectPlayer={selectPlayer}
    />
  ));

  return (
    <div className="scoreboard">
      <Header players={players} />
      <div className="players">{playerComponents}</div>
      <AddPlayerForm addPlayer={addPlayer} />
    </div>
  );
};

const mapStateToProps = state => ({
  players: state.players,
  selectedPlayerIndex: state.selectedPlayerIndex
});

Scoreboard.propTypes = {
  players: PropTypes.arrayOf(PropTypes.string).isRequired,
  dispatch: PropTypes.func.isRequired
};

export default connect(mapStateToProps)(Scoreboard);
