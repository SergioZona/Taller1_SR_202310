import BASE_URL from "../helpers/baseUrl";

export async function signup(signupData) {
  const data = {
    "username": signupData.username,
    "gender": signupData.gender,
    "age": signupData.age,
    "country": signupData.country,
    "password": signupData.password
  }
  const response = await fetch(`${BASE_URL}/user`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).catch((error) => ({
    error,
  }));
  if (response.error) {
    return { error: response.error };
  }

  return await response.json()

};

export default signup;
