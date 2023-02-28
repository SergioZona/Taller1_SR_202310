import React from "react";
import "../css/components/AddToPlaylistModel.css";
import PlylistCart from "./PlylistCart";
import Hader from "./Hader";

import { useStateValue } from "../StateProvider";

function AddToPlaylistModel() {
  const [{}, dispatch] = useStateValue();
  const [{ user, userPlaylists, showAddToPlaylistModel, songOptionnsData }] =
    useStateValue();

  const closeModel = () => {
    dispatch({
      type: "SHOW_HIDE_ADD_TO_PLAYLIST_MODEL",
      item: false,
    });
  };

  return (
    <div
      id="add-to-palylist-model"
      style={{ display: showAddToPlaylistModel ? "flex" : "none" }}
    >
      {/* ¿div - Hader (importar componentes)? */}
      <div id="hader">
        <div className="close" onClick={closeModel}></div>
        <h1 className="white-text">Add to playlist</h1>
        <button className="white-text">new playlist</button>
      </div>
      <main id="palylist-container">
        {userPlaylists.map(({ title, id }) => {
          <PlylistCart key={id} title={title} id={id} />;
        })}
      </main>
    </div>
  );
}

export default AddToPlaylistModel;
