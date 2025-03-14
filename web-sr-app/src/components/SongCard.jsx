import React, { useState } from "react";
import {
  Card,
  CardContent,
  CardMedia,
  Grid,
  IconButton,
  Snackbar,
  Typography,
  Tooltip,
} from "@mui/material";
import { PlayArrow } from "@mui/icons-material";
import imgAlbum from "../assets/images/albumartwork/nota-musical.png";
import playSong from "../handlers/playSong";
import { ToastContainer, toast } from "react-toastify";

const MAX_CHARS = 14;

const TextWithEllipsesAndHover = ({
  variant,
  component,
  height,
  style,
  text,
  maxChars,
  id,
}) => {
  const slicedText =
    text.length > maxChars ? text.slice(0, maxChars) + "..." : text;
  return (
    <Tooltip title={text} enterDelay={200} leaveDelay={200}>
      <Typography
        variant={variant}
        component={component}
        height={height}
        style={style}
      >
        {slicedText}
      </Typography>
    </Tooltip>
  );
};

const SongCard = ({ songName, artistName, imageUrl, id }) => {
  const [selected, setSelected] = useState(false);
  const [toastOpen, setToastOpen] = useState(false);

  const handleCardClick = () => {
    setSelected(!selected);
  };

  const handlePlayClick = async () => {
    // Modify the rating
    const result = await playSong(
      localStorage.getItem("username"),
      songName,
      artistName
    );
    if (result.message == "Data updated successfully") {
      setToastOpen(true);
    } else {
      toast.info("Please login to play a song");
    }
  };

  const handleToastClose = () => {
    setToastOpen(false);
  };

  return (
    <Grid item xs={12} sm={6} md={4} lg={3}>
      <Card
        sx={{
          display: "flex",
          flexDirection: "column",
          height: "100%",
        }}
        onClick={handleCardClick}
        raised={selected}
        style={{ borderRadius: "2vh", overflow: "hidden" }}
      >
        <CardMedia
          component="img"
          height="100vh"
          width="100vh"
          // cd={imageUrl}
          image={imgAlbum}
          alt={`${songName} - ${artistName}`}
          sx={{ paddingTop: "0%" }}
        />
        <CardContent
          sx={{ flexGrow: 1, alignItems: "center", justifyContent: "center" }}
        >
          <TextWithEllipsesAndHover
            variant="h6"
            component="h2"
            height="3vh"
            style={{ fontSize: "1rem", maxWidth: "100%" }}
            text={songName}
            maxChars={MAX_CHARS}
          ></TextWithEllipsesAndHover>

          <TextWithEllipsesAndHover
            variant="subtitle1"
            color="text.secondary"
            height="3vh"
            style={{ fontSize: "0.8rem", maxWidth: "100%" }}
            text={artistName}
            maxChars={MAX_CHARS}
          ></TextWithEllipsesAndHover>
        </CardContent>
        <IconButton aria-label="play" onClick={handlePlayClick} height="10vh">
          <PlayArrow />
        </IconButton>
      </Card>
      <Snackbar
        open={toastOpen}
        autoHideDuration={3000}
        onClose={handleToastClose}
        message={`${songName} - ${artistName}`}
      />
    </Grid>
  );
};

export default SongCard;
