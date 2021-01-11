import * as PlayerActionTypes from '../actiontypes/player';

export const addPlayer = name => ({
  type: PlayerActionTypes.ADD_PLAYER,
  name,
});

export const removePlayer = index => ({
  type: PlayerActionTypes.REMOVE_PLAYER,
  index,
});

export const updatePlayerScore = (index, score) => ({
  type: PlayerActionTypes.UPDATE_PLAYER_SCORE,
  index,
  score,
});
