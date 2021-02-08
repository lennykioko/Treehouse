import React, { useContext } from 'react';
import { ScoreboardContext } from './Context';
import Player from './Player';

const PlayerList = () => {
  const { players } = useContext(ScoreboardContext);
  return (
    <>
      {players.map( (player, index) => 
        <Player 
          key={player.id} 
          index={index}
        />
      )}
    </>
  );
}

export default PlayerList;