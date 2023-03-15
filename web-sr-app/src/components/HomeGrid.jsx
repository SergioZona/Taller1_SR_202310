import React, { useState, useEffect } from "react";
import "../css/components/AlbumCartGrid.css";
import BASE_URL from "../helpers/baseUrl";
import SongCard from "./SongCard";
import { Container } from "@mui/material";

function HomeGrid() {
  var user_id = localStorage.getItem("username");
  const MAX = 20;

  const [topAlbums, setTopAlbums] = useState([]);
  const [topReproductions, setTopReproductions] = useState([]);
  const [uu, setUserUser] = useState([]);
  const [ii, setItemItem] = useState([]);

  const url_image =
    "https://cdn.discordapp.com/attachments/550845751417110548/1083932968990556240/nota-musical_1.png";
  //"https://cdn-icons-png.flaticon.com/512/876/876817.png";
  // "https://via.placeholder.com/150"

  // Popular songs
  useEffect(() => {
    var user_id = localStorage.getItem("username");
    console.log(user_id);

    if (user_id != null) {
      fetch(`${BASE_URL}/user_track_artist/songs/top/${MAX}`)
        .then((res) => res.json())
        .then((data) => {
          setTopAlbums(data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }, []);

  // Top reproductions by user_id
  useEffect(() => {
    var user_id = localStorage.getItem("username");

    if (user_id != null) {
      fetch(`${BASE_URL}/user_track_artist/${user_id}/${MAX}`)
        .then((res) => res.json())
        .then((data) => {
          setTopReproductions(data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }, []);

  // Item-Item
  useEffect(() => {
    var user_id = localStorage.getItem("username");

    if (user_id != null) {
      fetch(
        `${BASE_URL}/user_track_artist/recommendation/${user_id}/${MAX}/${"False"}`
      )
        .then((res) => res.json())
        .then((data) => {
          setItemItem(data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }, []);

  // User-User
  useEffect(() => {
    var user_id = localStorage.getItem("username");

    if (user_id != null) {
      fetch(
        `${BASE_URL}/user_track_artist/recommendation/${user_id}/${MAX}/${"True"}`
      )
        .then((res) => res.json())
        .then((data) => {
          setUserUser(data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }, []);

  return (
    <>
      <h1
        className="section-hading"
        style={{ marginTop: "0px", marginBottom: "10px" }}
      >
        Most popular songs
      </h1>

      <Container
        id="album-cart-grid"
        style={{ maxHeight: 220, overflowY: "scroll" }}
      >
        {topAlbums.length > 0 &&
          topAlbums.map(({ id, track_name, artist_name }) => {
            return (
              <div key={id}>
                <SongCard
                  songName={track_name}
                  artistName={artist_name}
                  imageUrl={url_image}
                  id={id}
                />
              </div>
            );
          })}
      </Container>

      <h1
        className="section-hading"
        style={{ marginTop: "0px", marginBottom: "10px" }}
      >
        My top songs
      </h1>

      <Container
        id="album-cart-grid"
        style={{ maxHeight: 220, overflowY: "scroll" }}
      >
        {topReproductions.length > 0 &&
          topReproductions.map(({ id, track_name, artist_name }) => {
            return (
              <div key={id}>
                <SongCard
                  songName={track_name}
                  artistName={artist_name}
                  imageUrl={url_image}
                  id={id}
                />
              </div>
            );
          })}
      </Container>

      <h1
        className="section-hading"
        style={{ marginTop: "0px", marginBottom: "10px" }}
      >
        My recommendations (Item-Item)
      </h1>

      <Container
        id="album-cart-grid"
        style={{ maxHeight: 220, overflowY: "scroll" }}
      >
        {ii.length > 0 &&
          ii.map(({ id, track_name, artist_name }) => {
            return (
              <div key={id}>
                <SongCard
                  songName={track_name}
                  artistName={artist_name}
                  imageUrl={url_image}
                  id={id}
                />
              </div>
            );
          })}
      </Container>

      <h1
        className="section-hading"
        style={{ marginTop: "0px", marginBottom: "10px" }}
      >
        My recommendations (User-User)
      </h1>

      <Container
        id="album-cart-grid"
        style={{ maxHeight: 220, overflowY: "scroll" }}
      >
        {uu.length > 0 &&
          uu.map(({ id, track_name, artist_name }) => {
            return (
              <div key={id}>
                <SongCard
                  songName={track_name}
                  artistName={artist_name}
                  imageUrl={url_image}
                  id={id}
                />
              </div>
            );
          })}
      </Container>
    </>
  );
}

export default HomeGrid;
