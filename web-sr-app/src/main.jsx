import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

import * as serviceWorker from "./serviceWorker";
import { StateProvider } from "./StateProvider";
import reducer, { initialState } from "./reducer";
import { BrowserRouter } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <StateProvider initialState={initialState} reducer={reducer}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </StateProvider>
  </React.StrictMode>
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
