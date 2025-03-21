import React, { useEffect, useState } from "react";
import "./css/Register.css";
import signup from "./handlers/signup";
import login from "./handlers/login";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Cookies from "universal-cookie";
import { useStateValue } from "./StateProvider";

import registerMainContainer from "./assets/logo/spotify-icons-logos/logos/O1_RGB/O2_PNG/Spotify_Logo_RGB_White.png";

function Register({ history }) {
  const [showLoginForm, setShowLoginForm] = useState(true);
  const [signupErrors, setSignUpErrors] = useState({});
  const [loginError, setLoginError] = useState("");
  const cookies = new Cookies();
  const [{}, dispatch] = useStateValue();

  const toggleForms = () => {
    setShowLoginForm(!showLoginForm);
  };

  let signupData = {
    username: "",
    gender: "",
    age: "",
    country: "",
    password: "",
    passwordAgain: "",
  };

  let loginData = {
    username: "",
    password: "",
  };

  const submitSignup = async (e) => {
    e.preventDefault();
    var formEl = document.forms.SignupForm;
    var formData = new FormData(formEl);

    for (const [key] of Object.entries(signupData)) {
      signupData[key] = formData.get(key);
    }
    if (signupData.password == signupData.passwordAgain) {
      const result = await signup(signupData);
      if (result.message == "User created successfully!") {
        toast.info("SignUp Sucessfull 😍");

        cookies.set("loginToken", result.loginToken, { path: "/" });
        dispatch({
          type: "LOGIN_STATUS",
          item: true,
        });
        localStorage.setItem("username", signupData.username);
        history.push("/");
      } else {
        setSignUpErrors(result.error);
        toast.error("Resolve the errors to continue");
      }
    } else {
      toast.error("The passwords are not equals");
    }
  };

  const submitLogin = async (e) => {
    e.preventDefault();
    var formEl = document.forms.loginForm;
    var formData = new FormData(formEl);

    for (const [key] of Object.entries(loginData)) {
      loginData[key] = formData.get(key);
    }
    const result = await login(loginData.username, loginData.password);
    if (result.message == "LogIn successfully!") {
      toast.info("Login Sucessfull 😍");
      cookies.set("loginToken", result.token, { path: "/" });
      dispatch({
        type: "LOGIN_STATUS",
        item: true,
      });
      localStorage.setItem("username", loginData.username);
      history.push("/");
    } else {
      setLoginError(result.error);
      toast.error("Password or account invalid");
    }
  };

  return (
    <div className="register-main-container">
      <div className="right">
        <img src={registerMainContainer} />
      </div>
      <div className="left">
        <div className="button-container">
          <div
            id="activate-signup-form"
            onClick={toggleForms}
            className={showLoginForm ? "" : "active"}
          >
            <p>Sign Up</p>
          </div>
          <span
            id="activate-login-form"
            onClick={toggleForms}
            className={showLoginForm ? "active" : ""}
          >
            <p>Log In</p>{" "}
          </span>
        </div>
        <form
          id="SignupForm"
          method="POST"
          action="register.php"
          style={{ display: showLoginForm ? "none" : "flex" }}
        >
          <p>Username</p>
          <span className="show-error" id="input-field-email">
            {signupErrors?.email}
          </span>
          <input type="text" name="username" placeholder="Username" />
          <p>Gender</p>
          <select name="gender">
            <option value="">Please select one…</option>
            <option value="f">Female</option>
            <option value="m">Male</option>
            <option value="nb-binary">Non-Binary</option>
            <option value="o">Other</option>
            <option value="NA">Perfer not to Answer</option>
          </select>
          <p>Age</p>
          <input type="number" name="age" placeholder="Age" min={0} max={100} />
          <p>Country</p>
          <input type="text" name="country" placeholder="Country" />
          <p>Password</p>
          <span className="show-error">{signupErrors?.password}</span>
          <input type="password" name="password" placeholder="Password" />
          <p>Password Again</p>

          <input
            type="password"
            name="passwordAgain"
            placeholder="Password Again"
          />

          <br />
          <button
            type="submit"
            className="button-green signup-button"
            name="signup"
            onClick={submitSignup}
          >
            Sign Up
          </button>
        </form>

        <div>
          <form
            id="loginForm"
            action="register.php"
            method="POST"
            style={{ display: showLoginForm ? "flex" : "none" }}
          >
            <p>Username</p>
            <span className="show-error">{loginError}</span>
            <input type="text" name="username" placeholder="Username" />
            <p>Password</p>
            <input type="password" name="password" placeholder="Password" />
            <button
              type="submit"
              className="button-green login-button"
              name="login-submit"
              onClick={(e) => {
                submitLogin(e);
              }}
            >
              Log In
            </button>
            <a href="#" className="white-text">
              Forgotten Password
            </a>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Register;
