import React, { useState, useEffect } from "react";
import AlbumCart from "./AlbumCart";
import "../css/components/AlbumCartGrid.css";
import BASE_URL from "../helpers/baseUrl";
import SongCard from "./SongCard";
import { Grid, Container } from "@mui/material";

function HomeGrid() {
  const [apiData, setapiData] = useState([]);
  const [artists, setArtists] = useState([]);
  const [users, setUsers] = useState([]);
  const url_image =
    "https://cdn.discordapp.com/attachments/550845751417110548/1083932968990556240/nota-musical_1.png";
  //"https://cdn-icons-png.flaticon.com/512/876/876817.png";
  // "https://via.placeholder.com/150"

  useEffect(() => {
    fetch(`${BASE_URL}/user_track_rate/max/${10}`)
      .then((res) => res.json())
      .then((data) => {
        setapiData(data.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  // useEffect(() => {
  //   fetch(`${BASE_URL}api.php`)
  //     .then((response) => response.json())
  //     .then((data) => {
  //       setapiData(data.albums);
  //       setArtists(data.artists);
  //     });
  // }, []);

  useEffect(() => {
    fetch(`${BASE_URL}/user`)
      .then((res) => res.json())
      .then((data) => {
        setUsers(data.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <>
      <h1
        className="section-hading"
        style={{ marginTop: "0px", marginBottom: "10px" }}
      >
        Most Popular Albums
      </h1>

      <Container
        id="album-cart-grid"
        style={{ maxHeight: 215, overflowY: "scroll" }}
      >
        {apiData.length > 0 &&
          apiData.map(({ id, track_name }) => {
            return (
              <div key={id}>
                <SongCard
                  songName={track_name}
                  artistName={track_name}
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
        style={{ maxHeight: 215, overflowY: "scroll" }}
      >
        {users.length > 0 &&
          users.map(({ id, user_id }, index) => {
            return (
              <div key={id ? "bb" + id : "default-key-" + index}>
                <SongCard
                  songName={user_id}
                  artistName={user_id}
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
        style={{ maxHeight: 215, overflowY: "scroll" }}
      >
        {users.length > 0 &&
          users.map(({ id, user_id }, index) => {
            return (
              <div key={id ? "bb" + id : "default-key-" + index}>
                <SongCard
                  songName={user_id}
                  artistName={user_id}
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
