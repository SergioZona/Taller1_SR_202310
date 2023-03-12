import BASE_URL from "../helpers/baseUrl";

export async function login(email, password) {
  let bodyCredientail = {
    "email": email,
    "password": password
  };
  const response= await fetch(`${BASE_URL}/user/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },  
    body: JSON.stringify(bodyCredientail),
  })
  .catch((error) => ({
    error,
  }));  
  if (response.error) {
    return { error: response.error };
  }
  return await response.json()
};

export default login;
