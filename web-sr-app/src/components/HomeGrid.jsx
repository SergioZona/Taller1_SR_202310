import React, { useState, useEffect } from "react";
import AlbumCart from "./AlbumCart";
import "../css/components/AlbumCartGrid.css";
import BASE_URL from "../helpers/baseUrl";

function HomeGrid() {
  const [apiData, setapiData] = useState([]);
  const [artists, setArtists] = useState([]);
  const [users, setUsers] = useState([]);

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
      <h1 className="section-hading" style={{ marginTop: "20px" }}>
        Most Popular Albums
      </h1>
      <div id="album-cart-grid">
        {apiData.length > 0 &&
          apiData.map(({ id, title, discription, artPath }) => {
            return (
              <AlbumCart
                title={title}
                img={artPath}
                discription={discription}
                key={id}
                id={id}
              />
            );
          })}
      </div>
      <h1 className="section-hading">Popular Artists</h1>
      <div id="album-cart-grid">
        {artists.length > 0 &&
          artists.map(({ id, name, img }) => {
            return (
              <AlbumCart
                title={name}
                img={img}
                discription="Artist"
                key={id}
                id={id}
                isArtist={true}
              />
            );
          })}
        <div>
          {users.length > 0 &&
            users.map((d) => (
              <div key={d.user_id}>
                <p>Name: {d.user_id}</p>
              </div>
            ))}
        </div>
      </div>
    </>
  );
}

export default HomeGrid;
