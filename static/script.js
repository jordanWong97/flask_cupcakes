'use strict';

const BASE_API_URL = "http://localhost:5001/api";

//query API to get cupcakes and add to page

async function getCupcakes() {
  const response = await axios.get(`${BASE_API_URL}/cupcakes`);

  console.log('response ', response);
  return response;
}


async function showCupcakes() {
  let response = await getCupcakes();
  let cupcakes = response.data.cupcakes;
  for (let i = 0; i < cupcakes.length; i++) {
    $('#cupcakes').append(
      `<li>${cupcakes[i].flavor}
          ${cupcakes[i].rating}
          ${cupcakes[i].size}
          <img class="img-thumbnail" src="${cupcakes[i].image}">
    </li>`);
  }
}


//handle form submission to send new cupcake to API and update list on page
//with new cupcake


