import BASE_URL from "../helpers/baseUrl";

export async function modifyRating(username, track_name) {
  let body = {
    "username": username,
    "track_name":track_name
  };
  const response= await fetch(`${BASE_URL}/user_track_rate`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },  
    body: JSON.stringify(body),
  })
  .catch((error) => ({
    error,
  }));  
  if (response.error) {
    return { error: response.error };
  }
  return await response.json()
};

export default modifyRating;
